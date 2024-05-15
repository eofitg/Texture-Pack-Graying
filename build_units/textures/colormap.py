from build_units.build import Build
import config_reader as cr


class Colormap(Build):

    vanilla_path = './resource/1.8.9/assets/minecraft/gray/textures/colormap/'

    def __int__(self, texture_path):
        super(Colormap, self).__init__(texture_path)

    # ./{pack}/assets/minecraft/textures/colormap
    def build(self):

        if not cr.get('texture.blocks'):
            return

        output_path = self.output_path + self.texture_path[len(self.input_path):]
        checklist = super().build()

        for item in checklist:
            self.copy(self.vanilla_path + item, output_path)

