import os

from build_units.build_model import BuildModel

import utils.operating_tools as ot
import config_reader as cr


class Item(BuildModel):

    def __init__(self, json_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/models/item/'
        super().__init__(vanilla_path, json_path)

    # ./input/{pack}/assets/minecraft/models/item
    def build(self):
        if cr.get('isolate'):
            output_path = ot.get_output_path(self.resource_path)
            # change items' json files to custom location
            json_src = './resource/1.8.9/assets/minecraft/gray/models/item/'
            # ./output/{pack}/assets/minecraft/models/item
            json_dst = self.resource_path[:-len('textures/blocks')] + 'models/block'
            # png_src = './resource/1.8.9/assets/minecraft/gray/textures/blocks/'
            # png_dst = output_path + '/gray/'

        super().build()
        return True
