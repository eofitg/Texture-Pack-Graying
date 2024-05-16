import os

import utils.operating_tools as ot

from build_units.mcpatcher import sky
from build_units.mcpatcher import ctm
from build_units.mcpatcher import anim


# ./input/{pack}/assets/minecraft/mcpatcher
def build(path):

    for folder in os.scandir(path):
        name = folder.name
        if name.startswith('.'):
            continue
        if ((name == 'sky' or name == 'colormap')
                and sky.Sky(folder.path).build()):
            continue
        elif name == 'ctm' and ctm.CTM(folder.path).build():
            continue
        elif name == 'anim' and anim.Anim(folder.path).build():
            continue

        ot.build_anyway(folder.path)


