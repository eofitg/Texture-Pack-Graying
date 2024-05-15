import os

from build_units.build import Build
import build_units.whitelist as wl
import utils.grayscaling as gs
import utils.operating_tools as ot
import config_reader as cr


class Blocks(Build):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/blocks/'
        super(Blocks, self).__init__(vanilla_path, texture_path)

        temp = []
        for img in os.scandir(texture_path):
            if img.is_file() and img.name.endswith('.png'):
                if img.name in self.vanilla_list:
                    temp.append(img.name)
        self.texture_list = temp

    # ./{pack}/assets/minecraft/textures/blocks
    def build(self):

        if not cr.get('texture.blocks'):
            return

        vanilla_list = self.vanilla_list
        texture_list = self.texture_list
        output_path = self.output_path + self.texture_path[len(self.input_path):]
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
                    png_src = self.texture_path

                # change carpets' json files to custom location
                json_src = './resource/1.8.9/assets/minecraft/gray/models/block/carpet/'
                # ./output/{pack}/assets/minecraft/models/block
                json_dst = self.texture_path[:-15] + 'models/block'
                ot.copytree(json_src, json_dst)

                for item in os.scandir(png_src):
                    if item.is_file() and item.name.startswith('wool'):
                        ot.copy(item.path, png_dst)

            # change carpet but not wool
            else:
                png_src = './resource/1.8.9/assets/minecraft/gray/textures/blocks/'
                png_dst = output_path + '/gray/'
                if 'wool_colored_white.png' in texture_list:
                    png_src = self.texture_path

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

        for t in vanilla_list:
            if wl.exist(t):
                vanilla_list.remove(t)
        self.vanilla_list = vanilla_list

        checklist = super().build()
        for item in checklist:
            ot.copy(self.vanilla_path + item, output_path)

