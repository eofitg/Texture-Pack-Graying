import os

from build_units.build import Build
import build_units.whitelist as wl
import utils.operating_tools as ot
import config_reader as cr


class Entity(Build):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/entity/'
        super(Entity, self).__init__(vanilla_path, texture_path)

        temp = []
        for img in os.scandir(texture_path):
            if img.is_dir() or img.name.endswith('.png'):
                if img.name in self.vanilla_list:
                    temp.append(img.name)
        self.texture_list = temp

    # ./{pack}/assets/minecraft/textures/entity
    def build(self):

        if not cr.get('texture.entity'):
            return

        vanilla_list = self.vanilla_list
        output_path = self.output_path + self.texture_path[len(self.input_path):]

        for t in vanilla_list:
            if wl.exist(t):
                vanilla_list.remove(t)
        self.vanilla_list = vanilla_list

        checklist = super().build()
        for item in checklist:
            if item.endswith('.png'):
                ot.copy(self.vanilla_path + item, output_path)
            else:
                ot.copytree(self.vanilla_path + item, output_path)

