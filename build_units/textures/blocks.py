import os

from build_units.build_texture import BuildTexture
import utils.grayscaling as gs
import utils.operating_tools as ot
import config_reader as cr


class Blocks(BuildTexture):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/blocks/'
        super().__init__(vanilla_path, texture_path)

        temp = []
        for img in os.scandir(texture_path):
            if img.is_file() and img.name.endswith('.png'):
                if img.name in self.vanilla_list:
                    temp.append(img.name)
        self.texture_list = temp

    # ./input/{pack}/assets/minecraft/textures/blocks
    def build(self):

        if not cr.get('texture.blocks'):
            return False

        texture_list = self.texture_list
        output_path = ot.get_output_path(self.resource_path)
        # print(output_path)

        # carpet
        if cr.get('whitelist.blocks.carpet') == cr.get('whitelist.blocks.wool'):
            # carpet can be same as wool, don't need to modify
            pass
        else:
            # change wool but not carpet
            if cr.get('whitelist.blocks.carpet'):
                png_src = './resource/1.8.9/assets/minecraft/textures/blocks/'
                png_dst = output_path + '/gray/'
                if 'wool_colored_white.png' in texture_list:  # use original texture or this pack's
                    png_src = self.resource_path

                # change carpets' json files to custom location
                json_src = './resource/1.8.9/assets/minecraft/gray/models/block/carpet/'
                # ./output/{pack}/assets/minecraft/models/block
                json_dst = self.resource_path[:-15] + 'models/block'
                ot.copytree(json_src, json_dst)

                for item in os.scandir(png_src):
                    if item.is_file() and item.name.startswith('wool'):
                        ot.copy(item.path, png_dst)

            # change carpet but not wool
            else:
                png_src = './resource/1.8.9/assets/minecraft/gray/textures/blocks/'
                png_dst = output_path + '/gray/'
                if 'wool_colored_white.png' in texture_list:
                    png_src = self.resource_path

                # change carpets' json files to custom location
                json_src = './resource/1.8.9/assets/minecraft/gray/models/block/carpet/'
                # ./output/{pack}/assets/minecraft/models/block
                json_dst = output_path[:-15] + 'models/block'
                # print(json_dst)
                ot.copytree(json_src, json_dst)

                for item in os.scandir(png_src):
                    if item.is_file() and item.name.startswith('wool') and item.name.endswith('.png'):
                        if 'wool_colored_white.png' not in texture_list:
                            ot.copy(item.path, png_dst)
                        else:
                            img = gs.build(item.path)
                            if not os.path.exists(png_dst):
                                os.makedirs(png_dst)
                            img.save(png_dst + item.name)

        self.whitelist_check()

        checklist = super().build()
        dynamic_blocks = ['fire_layer_0.png', 'fire_layer_1.png', 'lava_flow.png', 'lava_still.png', 'portal.png',
                          'prismarine_rough.png', 'sea_lantern.png', 'water_flow.png', 'water_still.png', ]
        # files this pack didn't modify but need to grayscale
        for item in checklist:
            ot.copy(self.vanilla_path + item, output_path)
            # dynamic blocks need .mcmeta files support
            if item in dynamic_blocks:
                meta = item + '.mcmeta'
                if not os.path.exists(output_path + '/' + meta):
                    ot.copy(self.vanilla_path + meta, output_path)

        return True
