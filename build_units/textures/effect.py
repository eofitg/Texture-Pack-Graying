from build_units.build_texture import BuildTexture
import utils.grayscaling as gs
import config_reader as cr


class Effect(BuildTexture):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/textures/effect/'
        super().__init__(vanilla_path, texture_path)

    # ./input/{pack}/assets/minecraft/textures/effect
    def build(self):

        # if entity part does not need to grayscale
        if not cr.get('texture.effect'):
            return False

        checklist = super().build()
        # files this pack didn't modify but need to grayscale
        for item in checklist:
            gs.build_vanilla_file(self.vanilla_path, self.resource_path, item)

        return True
