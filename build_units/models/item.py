from build_units.build_model import BuildModel


class Item(BuildModel):

    def __init__(self, json_path):
        vanilla_path = './resource/1.8.9/assets/minecraft/gray/models/item/'
        super().__init__(vanilla_path, json_path)

    # ./input/{pack}/assets/minecraft/models/item
    def build(self):
        return super().build()
