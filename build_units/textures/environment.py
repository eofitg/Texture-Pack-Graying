from build_units.build_texture import BuildTexture
import utils.operating_tools as ot
import config_reader as cr


class Environment(BuildTexture):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/environment/'
        super().__init__(vanilla_path, texture_path)

    # ./input/{pack}/assets/minecraft/textures/environment
    def build(self):

        if not cr.get('texture.environment'):
            return False

        output_path = ot.get_output_path(self.resource_path)

        checklist = super().build()
        for item in checklist:
            ot.copy(self.vanilla_path + item, output_path)

        return True
