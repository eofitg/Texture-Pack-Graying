from build_units.build import Build
import utils.operating_tools as ot
import config_reader as cr


class Gui(Build):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/gui/'
        super(Gui, self).__init__(vanilla_path, texture_path)

    # ./{pack}/assets/minecraft/textures/gui
    def build(self):

        if not cr.get('texture.gui'):
            return False

        output_path = ot.get_output_path(self.texture_path)

        checklist = super().build()
        for item in checklist:
            if item.endswith('.png'):
                ot.copy(self.vanilla_path + item, output_path)
            else:
                ot.copytree(self.vanilla_path + item, output_path)

        return True
