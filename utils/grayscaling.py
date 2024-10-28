import os
from PIL import Image

import utils.operating_tools as ot


input_path = './input/'
output_path = './output/'


def build(src):
    img = Image.open(src).convert('RGBA')
    r, g, b, a = img.split()
    grey_img = Image.merge('RGB', (r, g, b)).convert('L')
    result_img = Image.merge('LA', (grey_img, a))
    return result_img


def save(img, src, name):
    # "name" includes file extension
    path = output_path + src[len(input_path):-len(name)]
    if not os.path.exists(path):
        os.makedirs(path)
    img.save(output_path + src[len(input_path):])


def build_dir(src):
    for item in os.scandir(src):
        if item.is_dir():
            build_dir(item)
        elif item.is_file() and item.path.endswith('.png'):
            result_img = build(item.path)
            save(result_img, item.path, item.name)
        else:
            ot.build_anyway(item.path)


def build_file(src, name):
    # "name" includes file extension
    result_img = build(src)
    save(result_img, src, name)

