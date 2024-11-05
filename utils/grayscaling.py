import os
from PIL import Image, ImageEnhance

import config_reader as cr
import utils.operating_tools as ot


def build(src):
    # float number
    brightness = cr.get('brightness')

    img = Image.open(src).convert('RGBA')
    r, g, b, a = img.split()

    # GRATING
    gray_img = Image.merge('RGB', (r, g, b)).convert('L')

    # LIGHTING
    enhancer = ImageEnhance.Brightness(gray_img)
    dark_img = enhancer.enhance(brightness)

    result_img = Image.merge('LA', (dark_img, a))
    return result_img


def save(img, src):
    dst = ot.get_output_path(src)
    parent = ot.get_parent_path(dst)

    if not os.path.exists(parent):
        os.makedirs(parent)
    img.save(dst)


def build_dir(src):
    for item in os.scandir(src):

        if item.is_dir():
            build_dir(item)

        elif item.is_file() and item.path.endswith('.png'):
            result_img = build(item.path)
            save(result_img, item.path)

        else:
            ot.build_anyway(item.path)


def build_file(src):
    result_img = build(src)
    save(result_img, src)

