from build_units.build_optifine import BuildOptiFine

import config_reader as cr


class Sky(BuildOptiFine):

    def __init__(self, texture_path):
        super().__init__(texture_path)

    # ./input/{pack}/assets/minecraft/mcpatcher/sky
    # ./input/{pack}/assets/minecraft/mcpatcher/colormap
    def build(self):

        if not cr.get('texture.optifine.sky'):
            return False

        super().build()
        return True
