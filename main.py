import os

import utils.decompress as decom
import utils.grayscaling
import utils.clean

input_path = 'input/'
output_path = 'output/'


def get_index(dirs):
    count = 0
    for item in os.scandir(input_path):
        if item.is_dir():
            dirs.append(item.path)
            count += 1
        elif item.is_file():
            # decompress .zip files
            if item.name.endswith('.zip'):
                decom.dec(item.name)
                count += 1
    return count


def read():
    dirs = []
    files = dirs
    n = get_index(dirs)


def build():
    pass


read()
