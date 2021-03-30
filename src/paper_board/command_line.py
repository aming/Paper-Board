import logging
from . import board, data, render_engine

def main():
    d = data.get_data()
    title = "    AMing Display Board   "
    title_image, data_image = render_engine.render(board.HEIGHT, board.WIDTH, title, d)
    board.print(title_image, data_image)
