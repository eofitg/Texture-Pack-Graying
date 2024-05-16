from build_units.build_optfine import BuildOptfine

import config_reader as cr


class CTM(BuildOptfine):

    def __init__(self, texture_path):
        super().__init__(texture_path)

    # ./input/{pack}/assets/minecraft/mcpatcher/ctm
    def build(self):

        if not cr.get('texture.block'):
            return False

        super().build()
        return True
