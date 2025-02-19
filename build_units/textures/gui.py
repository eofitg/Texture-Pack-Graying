from build_units.build_texture import BuildTexture
import utils.grayscaling as gs
import config_reader as cr


class GUI(BuildTexture):

    def __init__(self, texture_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/textures/gui/'
        super().__init__(vanilla_path, texture_path)

    # ./input/{pack}/assets/minecraft/textures/gui
    def build(self):

        # if gui part does not need to grayscale
        if not cr.get('texture.gui'):
            return False

        self.whitelist_check()

        checklist = super().build()
        # files this pack didn't modify but need to grayscale
        for item in checklist:
            if item.endswith('.png'):
                gs.build_vanilla_file(self.vanilla_path, self.resource_path, item)
            else:
                gs.build_vanilla_dir(self.vanilla_path, self.resource_path, item)

        return True
