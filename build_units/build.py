# abstract build units
import os

import utils.grayscaling as gs
import utils.operating_tools as ot


class Build(object):

    input_path = './input/'
    output_path = './output/'

    def __init__(self, vanilla_path, texture_path):
        self.vanilla_path = vanilla_path
        self.texture_path = texture_path

        vanilla_list = []
        with open(self.vanilla_path + 'list.dat', 'r') as file:
            line = file.readline().replace('\n', '')
            while line:
                vanilla_list.append(line)
                line = file.readline().replace('\n', '')
        self.vanilla_list = vanilla_list

    def build(self):
        check_list = self.vanilla_list
        path = self.texture_path

        for img in os.scandir(path):
            if img.name in check_list:
                if img.is_file() and img.name.endswith('.png'):
                    gs.build_file(img.path, img.name)
                    check_list.remove(img.name)
                    continue
                elif img.is_dir():
                    gs.build_dir(img.path)
                    check_list.remove(img.name)
                    continue
                else:
                    pass
            # files need to keep
            if img.is_file():
                ot.copy(img.path, ot.get_output_path(path))
            elif img.is_dir():
                # print(img.path)
                # print(self.output_path + path[len(self.input_path):] + img.name)
                ot.copytree(img.path, ot.get_output_path(path) + '/' + img.name)

        # return textures this pack didn't modify
        return check_list

