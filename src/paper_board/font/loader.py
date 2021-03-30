import importlib.resources
from PIL import ImageFont

def load(font_name, size):
    with importlib.resources.path("paper_board.font", font_name) as font_path:
        return ImageFont.truetype(str(font_path), size)
