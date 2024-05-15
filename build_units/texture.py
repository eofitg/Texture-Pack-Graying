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
        if name == 'blocks' and blocks.Blocks(folder.path).build():
            continue
        elif name == 'colormap' and colormap.Colormap(folder.path).build():
            continue
        elif name == 'entity' and entity.Entity(folder.path).build():
            continue
        elif name == 'environment' and environment.Environment(folder.path).build():
            continue
        elif name == 'gui' and gui.Gui(folder.path).build():
            continue
        elif name == 'items' and items.Items(folder.path).build():
            continue
        elif name == 'map' and map.Map(folder.path).build():
            continue
        elif name == 'armor' and armor.Armor(folder.path).build():
            continue
        elif name == 'painting' and painting.Painting(folder.path).build():
            continue
        elif name == 'particle' and particle.Particle(folder.path).build():
            continue

        ot.copytree(folder.path, ot.get_output_path(folder.path))
