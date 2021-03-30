import logging
from .waveshare.epd7in5b_HD import EPD, EPD_HEIGHT, EPD_WIDTH

HEIGHT = EPD_HEIGHT
WIDTH = EPD_WIDTH

epd = EPD()

def clear(data):
    logging.warn("Display Initializing")
    epd.init()
    logging.warn("Display Initialized")
    epd.Clear()
    logging.warn("Cleared Display")
    epd.sleep()
    logging.warn("Display Slept")

def print(red_image, black_image):
    logging.warn("Display Initializing")
    epd.init()
    logging.warn("Display Initialized and Image Printing")
    epd.display(epd.getbuffer(black_image), epd.getbuffer(red_image))
    logging.warn("Image Printed")
    epd.sleep()
    logging.warn("Display Slept")
