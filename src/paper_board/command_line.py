import logging
from . import board, data, render_engine

def main():
    d = [
            data.get_data(0),
            data.get_data(1),
            data.get_data(2),
            ]
    title_image, data_image = render_engine.render(board.HEIGHT, board.WIDTH, d)
    board.print(title_image, data_image)
