import os
from PIL import Image, ImageEnhance
import numpy as np

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
    custom_img = Image.open(src)
    result_img = build(src)
    if not compare_img(custom_img, result_img):
        save_from(result_img, src)


def build_vanilla_dir(vanilla_path, resource_path, item):
    vanilla_src = os.path.join(vanilla_path, item)
    custom_src = os.path.join(resource_path, item)

    for _item in os.scandir(vanilla_src):

        if _item.name == 'list.dat' or _item.name.startswith('.'):
            continue

        if _item.is_dir():
            build_vanilla_dir(vanilla_src, custom_src, _item.name)

        else:
            if _item.name.endswith('.png'):
                build_vanilla_file(vanilla_src, custom_src, _item.name)


# Graying an image
# From the vanilla resource
# To output folder
# vanilla_path: the parent dir of this item in the vanilla resource
# resource_path: the parent dir of this item in this pack (at the input folder)
# item: the name of this item, include ext
def build_vanilla_file(vanilla_path, resource_path, item):
    src = os.path.join(vanilla_path, item)
    dst = os.path.join(ot.turn_output_path(resource_path), item)

    vanilla_img = Image.open(src)
    result_img = build(src)
    if not compare_img(vanilla_img, result_img):
        save_to(result_img, dst)
        if os.path.exists(src + '.mcmeta'):
            ot.copy_file(src + '.mcmeta', ot.get_parent_path(dst))


# Compare two PIL images for exact equality
def compare_img(img_1: Image.Image, img_2: Image.Image):
    comp_1 = img_1.convert("RGBA")
    comp_2 = img_2.convert("RGBA")
    return np.array_equal(np.array(comp_1), np.array(comp_2))
