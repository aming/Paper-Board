import logging
from . import data

def main():
    logging.warn("Pulling data")
    data.update()

