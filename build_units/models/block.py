import os

import utils.operating_tools as ot


class Block(object):

    def __init__(self, json_path):
        self.vanilla_path = './resource/1.8.9/assets/minecraft/gray/models/block/'
        self.json_path = json_path

    # ./{pack}/assets/minecraft/models/block
    def build(self):

        output_path = ot.get_output_path(self.json_path)

        for mdl in os.scandir(self.json_path):
            if not os.path.exists(ot.get_output_path(mdl.path)):
                ot.copy(mdl.path, output_path)

        return True
