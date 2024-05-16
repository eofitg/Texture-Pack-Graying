import os

import utils.operating_tools as ot

from build_units.models import block
from build_units.models import item


# ./input/{pack}/assets/minecraft/models
def build(path):

    for folder in os.scandir(path):
        name = folder.name
        if name.startswith('.'):
            continue
        if name == 'block' and block.Block(folder.path).build():
            continue
        elif name == 'item' and item.Item(folder.path).build():
            continue

        ot.build_anyway(folder.path)


