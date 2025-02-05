from build_units.build_texture import BuildTexture
import utils.operating_tools as ot
import config_reader as cr


class Items(BuildTexture):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/items/'
        super().__init__(vanilla_path, texture_path)

    # ./input/{pack}/assets/minecraft/textures/items
    def build(self):

        if not cr.get('texture.items'):
            return False

        output_path = ot.get_output_path(self.resource_path)

        checklist = super().build()
        # files this pack didn't modify but need to grayscale
        for item in checklist:
            ot.copy_file(self.vanilla_path + item, output_path)

        return True
