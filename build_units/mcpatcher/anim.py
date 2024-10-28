from build_units.build_optifine import BuildOptiFine

import config_reader as cr


class Anim(BuildOptiFine):

    def __init__(self, texture_path):
        super().__init__(texture_path)

    # ./input/{pack}/assets/minecraft/mcpatcher/anim
    def build(self):

        if not cr.get('texture.optifine.anim'):
            return False

        super().build()
        return True
