import importlib, os
from PIL import Image, ImageDraw
from datetime import datetime
from . import font

def render(height, width, title, data):
    title_font = font.load("Font.ttc", 40)
    small_font = font.load("Font.ttc", 16)
    main_font = font.load("Font.ttc", 35)
    title_image = Image.new('1', (height, width), 255)  # 255: clear the frame
    title_draw = ImageDraw.Draw(title_image)
    title_draw.text((2, 0), title, font = title_font, fill = 0)
    lastUpdate = 'last updated at {0}'.format(datetime.now().strftime("%b-%d-%Y %H:%M:%S"))
    title_draw.text((220, 50), lastUpdate, font = small_font, fill = 0)
    data_image = Image.new('1', (height, width), 255)  # 255: clear the frame
    data_draw = ImageDraw.Draw(data_image)
    y = 75
    i = 1
    for d in data:
        text = '{0:02d} {1}'.format(i, d)
        data_draw.text((2, y), text, font = main_font, fill = 0)
        y += 50
        i += 1
    if os.path.isfile("paper_board/font/image.jpg"):
        with importlib.resources.path("paper_board.font", 'image.jpg') as img_path:
            pic_image = Image.open(img_path)
            pic_image = pic_image.convert('L')
            data_image.paste(pic_image, (0, 618))
    return title_image, data_image
