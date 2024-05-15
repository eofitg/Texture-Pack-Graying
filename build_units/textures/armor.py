from build_units.build import Build
import utils.operating_tools as ot
import config_reader as cr


class Armor(Build):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/models/armor/'
        super(Armor, self).__init__(vanilla_path, texture_path)

    # ./{pack}/assets/minecraft/textures/models/armor
    def build(self):

        if not cr.get('texture.armor'):
            return False

        output_path = ot.get_output_path(self.texture_path)

        checklist = super().build()
        for item in checklist:
            ot.copy(self.vanilla_path + item, output_path)

        return True
