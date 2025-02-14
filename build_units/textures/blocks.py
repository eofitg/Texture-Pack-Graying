import os

from build_units.build_texture import BuildTexture

import utils.grayscaling as gs
import utils.operating_tools as ot
import config_reader as cr


class Blocks(BuildTexture):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/textures/blocks/'
        super().__init__(vanilla_path, texture_path)

    # ./input/{pack}/assets/minecraft/textures/blocks
    def build(self):

        # if blocks part does not need to grayscale
        if not cr.get('texture.blocks'):
            return False

        output_path = ot.turn_output_path(self.resource_path)

        # carpet can be same as wool, don't need to modify
        if cr.get('whitelist.blocks.carpet') == cr.get('whitelist.blocks.wool'):
            pass

        # carpet need to modify
        else:

            # make carpet-json locate to modified carpet-texture path, not original wool anymore
            json_src = './resource/1.8.9/assets/minecraft/gray/models/block/carpet/'
            # ./output/{pack}/assets/minecraft/
            minecraft_path = ot.get_parent_path(output_path, 2)
            # ./output/{pack}/assets/minecraft/models/block
            json_dst = os.path.join(minecraft_path, 'models/block')
            ot.copy_dir(json_src, json_dst)

            wools = ['wool_colored_black.png', 'wool_colored_blue.png', 'wool_colored_brown.png',
                     'wool_colored_cyan.png', 'wool_colored_gray.png', 'wool_colored_green.png',
                     'wool_colored_light_blue.png', 'wool_colored_lime.png', 'wool_colored_magenta.png',
                     'wool_colored_orange.png', 'wool_colored_pink.png', 'wool_colored_purple.png',
                     'wool_colored_red.png', 'wool_colored_silver.png', 'wool_colored_white.png',
                     'wool_colored_yellow.png']

            # change wool but not carpet
            # i.e. keep carpet texture
            if cr.get('whitelist.blocks.carpet'):

                png_dst = os.path.join(output_path, 'gray/carpet')

                for wool in wools:

                    vanilla_wool = os.path.join(self.vanilla_path, wool)
                    custom_wool = os.path.join(self.resource_path, wool)

                    # if this pack modified this wool in its texture
                    if os.path.exists(custom_wool):
                        ot.copy_file(custom_wool, png_dst)

                    else:
                        ot.copy_file(vanilla_wool, png_dst)

            # change carpet but not wool
            # i.e. grayscale carpet texture
            else:

                png_dst = os.path.join(output_path, 'gray/carpet')

                for wool in wools:

                    vanilla_wool = os.path.join(self.vanilla_path, wool)
                    custom_wool = os.path.join(self.resource_path, wool)

                    # if this pack modified this wool in its texture
                    if os.path.exists(custom_wool):
                        img = gs.build(custom_wool)
                        if not os.path.exists(png_dst):
                            os.makedirs(png_dst)
                        img.save(os.path.join(png_dst, wool))

                    else:
                        img = gs.build(vanilla_wool)
                        if not os.path.exists(png_dst):
                            os.makedirs(png_dst)
                        img.save(os.path.join(png_dst, wool))

        self.whitelist_check()

        checklist = super().build()
        dynamic_blocks = ['fire_layer_0.png', 'fire_layer_1.png', 'lava_flow.png', 'lava_still.png', 'portal.png',
                          'prismarine_rough.png', 'sea_lantern.png', 'water_flow.png', 'water_still.png']
        # files this pack didn't modify but need to grayscale
        for item in checklist:
            gs.build_vanilla_file(self.vanilla_path, self.resource_path, item)
            # dynamic blocks need .mcmeta files support
            if item in dynamic_blocks:
                meta = item + '.mcmeta'
                meta_file = os.path.join(self.vanilla_path, meta)
                if not os.path.exists(os.path.join(output_path, meta)):
                    ot.copy_file(meta_file, output_path)

        return True
