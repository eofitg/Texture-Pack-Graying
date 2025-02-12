from build_units.build_texture import Build

import os

import utils.operating_tools as ot
import config_reader as cr


class Underwater(Build):

    def __init__(self, texture_path):
        super().__init__(texture_path)

    # ./input/{pack}/assets/minecraft/textures/misc/underwater.png
    def build(self):

        if not cr.get('texture.underwater'):
            return False

        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/misc/underwater.png'
        output_path = ot.turn_output_path(self.resource_path)
        ot.build_anyway(self.resource_path)
        ot.copy_file(vanilla_path, output_path)

        return True
