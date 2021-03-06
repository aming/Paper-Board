import logging
from . import data, render_engine
from PIL import ImageChops

def main():
    logging.warn("Pulling data")
    data.update()

def render():
    d = [
            data.get_data(0),
            data.get_data(1),
            data.get_data(2),
            ]
    red_image, black_image = render_engine.render(528, 880, d)
    image = ImageChops.darker(red_image, black_image)
    image.show()
