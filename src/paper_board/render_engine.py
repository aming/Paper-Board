import importlib, os
import logging
from PIL import Image, ImageDraw
from datetime import datetime
from . import font
from . import config

MARGIN=8
WIDGET_HEIGHT=200
MAIN_HEIGHT=400
STATUS_HEIGHT=40

def render_widget(height, width, data):
    size=25
    f = font.load("Font.ttc", size)
    image = Image.new('1', (height, width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    y = 0
    for d in data:
        draw.text((2, y), d, font = f, fill = 0)
        y += size
    return image

def render_main(height, width, data):
    f = font.load("Font.ttc", 25)
    image = Image.new('1', (height, width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    y = 0
    i = 1
    for d in data:
        text = '{0:02d} {1}'.format(i, d)
        draw.text((2, y), text, font = f, fill = 0)
        y += 50
        i += 1
    return image

def render_photo(height, width, photo_file):
    image = Image.new('1', (height, width), 255)  # 255: clear the frame
    try:
        pic_image = Image.open(photo_file)
        pic_image = pic_image.convert('L')
        image.paste(pic_image, (0, 0))
    except FileNotFoundError:
        f = font.load("Font.ttc", 35)
        draw = ImageDraw.Draw(image)
        draw.text((0,0), "Image not found", font=f, fill=0)
    return image

def render_status_line(height, width):
    f = font.load("Font.ttc", 14)
    image = Image.new('1', (height, width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    lastUpdate = 'last updated at {0}'.format(datetime.now().strftime("%b-%d-%Y %H:%M:%S"))
    draw.text((140, 10), lastUpdate, font=f, fill=0)
    return image

def render(height, width, data):
    logging.warn("Rendering " + str(height) + " x " + str(width) + " image")
    height_ptr=0
    image = Image.new('1', (height, width), 255)  # 255: clear the frame
    image.paste(render_widget(int(height/2), WIDGET_HEIGHT, data[0]), (0, height_ptr))
    image.paste(render_widget(int(height/2), WIDGET_HEIGHT, data[1]), (int(height/2), height_ptr))
    height_ptr += WIDGET_HEIGHT
    image.paste(render_main(height-(MARGIN*2), MAIN_HEIGHT, data[2]), (MARGIN, height_ptr))
    height_ptr += MAIN_HEIGHT
    image.paste(render_photo(height-(MARGIN*2), WIDGET_HEIGHT, config.config_dir + '/image.jpg'), (MARGIN, height_ptr))
    height_ptr += WIDGET_HEIGHT
    image.paste(render_status_line(height, STATUS_HEIGHT), (0, width-STATUS_HEIGHT))
    return Image.new('1', (height, width), 255), image
