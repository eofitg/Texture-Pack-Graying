from build_units.build import Build

import os

import utils.grayscaling as gs
import build_units.whitelist as wl
import utils.operating_tools as ot


# abstract build unit for textures
class BuildTexture(Build):

    def __init__(self, vanilla_path, texture_path):
        self.vanilla_path = vanilla_path
        super().__init__(texture_path)

        vanilla_list = []
        with open(self.vanilla_path + 'list.dat', 'r') as file:
            line = file.readline().replace('\n', '')
            while line:
                vanilla_list.append(line)
                line = file.readline().replace('\n', '')
        self.vanilla_list = vanilla_list

    # ./input/{pack}/assets/minecraft/textures
    def build(self):

        check_list = self.vanilla_list

        # parent dir exist but child not
        # e.g. '/textures/models/' path exist but '/textures/models/armor/' not
        if not os.path.exists(self.resource_path):
            # Add all the vanilla textures to checklist
            # also to avoid invalid path error crash
            return check_list

        # dir exist but empty
        if len(os.listdir(self.resource_path)) == 0:
            return check_list

        for item in os.scandir(self.resource_path):

            # files need to keep (prob in wl)
            if item.name not in check_list:
                ot.build_anyway(item.path)
                continue

            if item.is_file() and item.name.endswith('.png'):
                gs.build_file(item.path)
                check_list.remove(item.name)
            elif item.is_dir():
                gs.build_dir(item.path)
                check_list.remove(item.name)

        # return textures this pack didn't modify
        return check_list

    def whitelist_check(self):

        for t in self.vanilla_list[:]:
            if wl.exist(t):
                self.vanilla_list.remove(t)

