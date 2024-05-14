import os
import shutil
import importlib

import config_reader as cr
import utils.decompress as dec
import utils.grayscaling as gs
from utils import clean
from build_units import textures
from build_units import mcpatcher
from build_units import models


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


def build():
    packs = get_packs()

    for pack in packs:
        path = input_path + pack + '/assets/minecraft'
        if not os.path.exists(path):
            error_message = 'Incorrect pack folder at \"' + path + '\".'
            print(error_message)

        for folder in os.scandir(path):
            name = folder.name
            if folder.is_file() or name.startswith('.'):
                continue
            if name == 'textures':
                textures.build(folder.path)
                continue
            elif name == 'mcpatcher':  # optfine folder, like sky and ctm textures
                mcpatcher.build(folder.path)
                continue
            elif name == 'models':
                models.build(folder.path)
                continue
            else:  # folders never need to build
                # print(folder.path)
                pass
            shutil.copytree(folder.path, output_path + folder.path[len(input_path):])


build()
