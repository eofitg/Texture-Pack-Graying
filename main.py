import os
import shutil
import importlib

import config_reader as cr
import utils.decompress as dec
import utils.grayscaling as gs
from utils import clean
from build_units import texture
from build_units import optfine
from build_units import model


input_path = './input/'
output_path = './output/'


def get_packs():
    dirs = []
    for item in os.scandir(input_path):
        if item.is_dir():
            dirs.append(item.path[len(input_path):])
        elif item.is_file() and item.name.endswith('.zip'):
            # decompress .zip files
            dec.build(item.name)
            dirs.append(item.path[len(input_path):-4])
    return list(set(dirs))


def copy(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copy(src, dst)


def copytree(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def build():
    packs = get_packs()

    for pack in packs:

        path = input_path + pack
        # ./{pack}/
        for file in os.scandir(path):
            if file.is_file() and not file.name.startswith('.'):
                copy(file.path, output_path + file.path[len(input_path):-len(file.name)])

        path = path + '/assets/minecraft/'
        if not os.path.exists(path):
            error_message = 'Incorrect pack folder at \"' + path + '\".'
            print(error_message)
        # ./{pack}/assets/minecraft/
        for folder in os.scandir(path):
            name = folder.name
            dst = output_path + folder.path[len(input_path):]
            if folder.is_file():
                if not name.startswith('.'):
                    copy(folder.path, dst[:-len(folder.name)])
                continue
            if name == 'textures':
                texture.build(folder.path)
                continue
            elif name == 'mcpatcher':  # optfine folder, like sky and ctm textures
                # optfine.build(folder.path)
                continue
            elif name == 'models':
                # model.build(folder.path)
                continue
            else:  # folders never need to build
                # print(folder.path)
                pass

            copytree(folder.path, dst)


build()
