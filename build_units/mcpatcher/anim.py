from build_units.build_optfine import BuildOptfine

import config_reader as cr


class Anim(BuildOptfine):

    def __init__(self, texture_path):
        super().__init__(texture_path)

    # ./input/{pack}/assets/minecraft/mcpatcher/anim
    def build(self):

        if not cr.get('texture.optfine.anim'):
            return False

        super().build()
        return True
