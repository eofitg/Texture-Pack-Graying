from build_units.build import Build

import os

import utils.grayscaling as gs
import utils.operating_tools as ot


# abstract build unit for opfine files
class BuildOptfine(Build):

    def __init__(self, resource_path):
        super().__init__(resource_path)

    # ./input/{pack}/assets/minecraft/mcpatcher/
    def build(self):

        for item in os.scandir(self.resource_path):
            if item.name.startswith('.'):
                continue
            if item.is_file() and item.name.endswith('.png'):
                gs.build_file(item.path, item.name)
                continue
            elif item.is_dir():
                gs.build_dir(item.path)
                continue
            else:
                pass

            # files need to keep
            ot.build_anyway(item.path)


