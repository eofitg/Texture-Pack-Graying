# abstract build units
import os
import shutil

import utils.grayscaling as gs


class Build(object):

    input_path = './input/'
    output_path = './output/'
    vanilla_path = ''

    def __init__(self, texture_path):
        self.texture_path = texture_path

        vanilla_list = []
        with open(self.vanilla_path + 'list.dat', 'r') as file:
            line = file.readline().replace('\n', '')
            while line:
                vanilla_list.append(line)
                line = file.readline().replace('\n', '')
        self.vanilla_list = vanilla_list

        temp = []
        for img in os.scandir(texture_path):
            if img.is_file() and img.name.endswith('.png'):
                if img.name in vanilla_list:
                    temp.append(img.name)
        self.texture_list = temp

    def build(self):
        check_list = self.vanilla_list
        path = self.texture_path

        for img in os.scandir(path):
            if img.is_file() and img.name.endswith('.png'):
                if img.name in check_list:
                    gs.build_file(img.path, img.name)
                    check_list.remove(img.name)
                    continue
            # files need to keep
            self.copy(img.path, self.output_path + path[len(self.input_path):])

        # return textures this pack didn't modify
        return check_list

    @classmethod
    def copy(cls, src, dst):
        if not os.path.exists(dst):
            os.makedirs(dst)
        shutil.copy(src, dst)

    @classmethod
    def copytree(cls, src, dst):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
