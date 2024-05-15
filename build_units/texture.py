import os

import utils.operating_tools as ot

from build_units.textures import blocks
from build_units.textures import colormap
from build_units.textures import entity
from build_units.textures import environment
from build_units.textures import gui
from build_units.textures import items
from build_units.textures import map
from build_units.textures import armor
from build_units.textures import painting
from build_units.textures import particle


# ./{pack}/assets/minecraft/textures
def build(path):
    for folder in os.scandir(path):
        name = folder.name
        if folder.is_file() or name.startswith('.'):
            continue
        if name == 'blocks':
            blocks.Blocks(folder.path).build()
        elif name == 'colormap':
            colormap.Colormap(folder.path).build()
        elif name == 'entity':
            entity.Entity(folder.path).build()
        elif name == 'environment':
            environment.Environment(folder.path).build()
        elif name == 'gui':
            gui.Gui(folder.path).build()
        elif name == 'items':
            items.Items(folder.path).build()
        elif name == 'map':
            map.Map(folder.path).build()
        elif name == 'armor':
            armor.Armor(folder.path).build()
        elif name == 'painting':
            painting.Painting(folder.path).build()
        elif name == 'particle':
            particle.Particle(folder.path).build()
        else:
            ot.copytree(folder.path, ot.get_output_path(folder.path))
