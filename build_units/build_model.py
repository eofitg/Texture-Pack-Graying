from build_units.build import Build

import os
import utils.operating_tools as ot


# abstract build unit for models
class BuildModel(Build):

    def __init__(self, vanilla_path, json_path):
        self.vanilla_path = vanilla_path
        super().__init__(json_path)

        vanilla_list = []
        with open(self.vanilla_path + 'list.dat', 'r') as file:
            line = file.readline().replace('\n', '')
            while line:
                vanilla_list.append(line)
                line = file.readline().replace('\n', '')
        self.vanilla_list = vanilla_list

    # ./input/{pack}/assets/minecraft/models
    def build(self):
        output_path = ot.turn_output_path(self.resource_path)

        for mdl in os.scandir(self.resource_path):
            if not os.path.exists(ot.turn_output_path(mdl.path)):
                ot.copy_file(mdl.path, output_path)
