import os
from PIL import Image, ImageEnhance

import config_reader as cr
import utils.operating_tools as ot


brightness = cr.get('brightness')  # float


def build(src):
    img = Image.open(src).convert('RGBA')
    r, g, b, a = img.split()

    # GRAYING
    gray_img = Image.merge('RGB', (r, g, b)).convert('L')

    # LIGHTING
    enhancer = ImageEnhance.Brightness(gray_img)
    dark_img = enhancer.enhance(brightness)

    result_img = Image.merge('LA', (dark_img, a))
    return result_img


# save image from an input path
def save_from(img, src):
    dst = ot.turn_output_path(src)
    save_to(img, dst)


# save image to certain path
def save_to(img, dst):
    parent = ot.get_parent_path(dst)
    if not os.path.exists(parent):
        os.makedirs(parent)
    img.save(dst)


# Graying a folder
# From a custom pack at the input folder
# To output folder
def build_dir(src):
    for item in os.scandir(src):

        if item.is_dir():
            build_dir(item)

        elif item.is_file() and item.path.endswith('.png'):
            result_img = build(item.path)
            save_from(result_img, item.path)

        else:
            ot.build_anyway(item.path)


# Graying an image
# From a custom pack at the input folder
# To output folder
def build_file(src):
    result_img = build(src)
    save_from(result_img, src)


# Graying an image
# From the vanilla resource
# To output folder
# vanilla_path: the parent dir of this item in the vanilla resource
# resource_path: the parent dir of this item in this pack (at the input folder)
# item: the name of this item, include ext
def build_vanilla_file(vanilla_path, resource_path, item):
    src = os.path.join(vanilla_path, item)
    dst = os.path.join(ot.turn_output_path(resource_path), item)
    result_img = build(src)
    save_to(result_img, dst)

