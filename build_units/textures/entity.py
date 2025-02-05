import os

from build_units.build_texture import BuildTexture
import utils.operating_tools as ot
import config_reader as cr


class Entity(BuildTexture):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/entity/'
        super().__init__(vanilla_path, texture_path)

        temp = []
        for img in os.scandir(texture_path):
            if img.is_dir() or img.name.endswith('.png'):
                if img.name in self.vanilla_list:
                    temp.append(img.name)
        self.texture_list = temp

    # ./input/{pack}/assets/minecraft/textures/entity
    def build(self):

        if not cr.get('texture.entity'):
            return False

        output_path = ot.get_output_path(self.resource_path)
        self.whitelist_check()

        checklist = super().build()
        # files this pack didn't modify but need to grayscale
        for item in checklist:
            if item.endswith('.png'):
                ot.copy_file(self.vanilla_path + item, output_path)
            else:
                ot.copy_dir(self.vanilla_path + item, output_path)

        return True
