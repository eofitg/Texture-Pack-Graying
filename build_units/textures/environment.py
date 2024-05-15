from build_units.build import Build
import utils.operating_tools as ot
import config_reader as cr


class Environment(Build):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/environment/'
        super(Environment, self).__init__(vanilla_path, texture_path)

    # ./{pack}/assets/minecraft/textures/environment
    def build(self):

        if not cr.get('texture.environment'):
            return False

        output_path = self.output_path + self.texture_path[len(self.input_path):]
        checklist = super().build()

        for item in checklist:
            ot.copy(self.vanilla_path + item, output_path)

        return True
