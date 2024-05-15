from build_units.build import Build
import utils.operating_tools as ot
import config_reader as cr


class Items(Build):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/items/'
        super(Items, self).__init__(vanilla_path, texture_path)

    # ./{pack}/assets/minecraft/textures/items
    def build(self):

        if not cr.get('texture.items'):
            return

        output_path = self.output_path + self.texture_path[len(self.input_path):]
        checklist = super().build()

        for item in checklist:
            ot.copy(self.vanilla_path + item, output_path)

