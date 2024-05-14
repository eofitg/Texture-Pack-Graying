import os
from PIL import Image

input_path = './input/'
output_path = './output/'


def build(dir):
    for item in os.scandir(dir):
        if item.is_dir():
            build(item)
        elif item.is_file() and item.path.endswith('.png'):
            img = Image.open(item.path).convert('RGBA')
            r, g, b, a = img.split()
            grey_img = Image.merge('RGB', (r, g, b)).convert('L')
            result_img = Image.merge('LA', (grey_img, a))

            path = output_path + item.path[len(input_path):-len(item.name)]
            if not os.path.exists(path):
                os.makedirs(path)
            result_img.save(output_path + item.path[8:])

