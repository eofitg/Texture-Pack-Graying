from build_units.build_optfine import BuildOptfine

import config_reader as cr


class Sky(BuildOptfine):

    def __init__(self, texture_path):
        super().__init__(texture_path)

    # ./input/{pack}/assets/minecraft/mcpatcher/sky
    # ./input/{pack}/assets/minecraft/mcpatcher/colormap
    def build(self):

        if not cr.get('texture.optfine.sky'):
            return False

        super().build()
        return True
