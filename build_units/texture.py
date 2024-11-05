import os

import utils.operating_tools as ot
import config_reader as cr

from build_units.textures import blocks
from build_units.textures import colormap
from build_units.textures import entity
from build_units.textures import environment
from build_units.textures import gui
from build_units.textures import items
from build_units.textures import underwater
from build_units.textures import map
from build_units.textures import armor
from build_units.textures import painting
from build_units.textures import particle


# ./input/{pack}/assets/minecraft/textures
def build(path):

    textures = ['blocks', 'colormap', 'entity', 'environment', 'gui', 'items', 'underwater', 'map', 'armor', 'painting', 'particle']
    check = textures

    for folder in os.scandir(path):
        name = folder.name

        if name == 'blocks' and blocks.Blocks(folder.path).build():
            check.remove(name)
            continue
        elif name == 'colormap' and colormap.Colormap(folder.path).build():
            check.remove(name)
            continue
        elif name == 'entity' and entity.Entity(folder.path).build():
            check.remove(name)
            continue
        elif name == 'environment' and environment.Environment(folder.path).build():
            check.remove(name)
            continue
        elif name == 'gui' and gui.GUI(folder.path).build():
            check.remove(name)
            continue
        elif name == 'items' and items.Items(folder.path).build():
            check.remove(name)
            continue
        elif name == 'misc' and underwater.Underwater(folder.path).build():
            check.remove('underwater')
            continue
        elif name == 'map' and map.Map(folder.path).build():
            check.remove(name)
            continue
        elif name == 'models' and armor.Armor(folder.path).build():
            check.remove('armor')
            continue
        elif name == 'painting' and painting.Painting(folder.path).build():
            check.remove(name)
            continue
        elif name == 'particle' and particle.Particle(folder.path).build():
            check.remove(name)
            continue

        ot.build_anyway(folder.path)

    # folders this pack didn't modify but need to grayscale
    for texture in textures:
        if cr.get('texture.' + texture) and texture in check:
            vanilla = './resource/1.8.9/assets/minecraft/gray/textures/'
            src = os.path.join(vanilla, texture)
            dst = ot.get_output_path(os.path.join(path, texture))
            ot.copy_dir(src, dst)
