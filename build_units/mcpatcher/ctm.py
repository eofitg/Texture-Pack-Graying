from build_units.build_optfine import BuildOptfine

import config_reader as cr


class CTM(BuildOptfine):

    def __init__(self, texture_path):
        super().__init__(texture_path)

    # ./input/{pack}/assets/minecraft/mcpatcher/ctm
    def build(self):

        if not cr.get('texture.blocks'):
            return False

        check_list = ['carpet', 'wood', 'wool', 'tnt', 'glass', 'stained_glass',
                      'hardened_clay', 'stained_hardened_clay']
        for item in check_list:
            if cr.get('whitelist.blocks.' + item):
                self.whitelist.append(item)

        super().build()
        return True
