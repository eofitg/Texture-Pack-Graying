import os

from build_units.build_model import BuildModel

import utils.grayscaling as gs
import utils.operating_tools as ot
import config_reader as cr


class Item(BuildModel):

    def __init__(self, json_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/models/item/'
        super().__init__(vanilla_path, json_path)

    # ./input/{pack}/assets/minecraft/models/item
    def build(self):

        block_state = cr.get('texture.blocks')
        item_state = cr.get('texture.items')

        if cr.get('isolate') and block_state != item_state:

            png_dst = ot.get_output_path(self.resource_path)[:-len('models/item')] + 'textures/blocks/gray/'
            if block_state:  # change block but not item
                self.build_json()
                # modify texture
                png_van_src = './resource/1.8.9/assets/minecraft/textures/blocks/'
                png_pack_src = self.resource_path[:-len('models/item')] + 'textures/blocks/'
                for item in os.scandir(png_van_src):
                    if not item.name.endswith('.png'):
                        continue
                    if os.path.exists(png_pack_src + item.name):
                        png_src = png_pack_src + item.name
                    else:
                        png_src = item.path
                    print(png_src)
                    print(png_dst)
                    ot.copy(png_src, png_dst)

                    # dynamic check
                    if os.path.exists(png_src + '.mcmeta'):
                        ot.copy(png_src + '.mcmeta', png_dst)

            else:  # change item but not block
                self.build_json()
                # modify texture
                png_van_src = './resource/1.8.9/assets/minecraft/textures/blocks/'
                png_gray_src = './resource/1.8.9/assets/minecraft/gray/textures/blocks/'
                png_pack_src = self.resource_path[:-len('models/item')] + 'textures/blocks/'
                for item in os.scandir(png_van_src):
                    if not item.name.endswith('.png'):
                        continue
                    if os.path.exists(png_pack_src + item.name):
                        png_src = png_pack_src + item.name
                        img = gs.build(png_src)
                        if not os.path.exists(png_dst):
                            os.makedirs(png_dst)
                        img.save(png_dst + item.name)
                    else:
                        png_src = png_gray_src + item.name
                        ot.copy(png_src, png_dst)

                    # dynamic check
                    if os.path.exists(png_src + '.mcmeta'):
                        ot.copy(png_src + '.mcmeta', png_dst)

        super().build()
        return True

    def build_json(self):
        output_path = ot.get_output_path(self.resource_path)
        # make item-json locate to modified block-json path
        item_json_src = './resource/1.8.9/assets/minecraft/gray/models/item/'
        # ./output/{pack}/assets/minecraft/models/item
        item_json_dst = output_path
        for item in os.scandir(item_json_src):
            if item.name.endswith('.json'):
                ot.copy(item.path, item_json_dst)

        # make block-json locate to modified block-texture path
        block_json_src = './resource/1.8.9/assets/minecraft/gray/models/block/'
        # ./output/{pack]/assets/minecraft/models/block/gray
        block_json_dst = output_path[:-len('item')] + 'block/gray'
        for item in os.scandir(block_json_src):
            if item.name.endswith('.json'):
                ot.copy(item.path, block_json_dst)
