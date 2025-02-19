import os

import utils.operating_tools as ot
import utils.grayscaling as gs
import config_reader as cr

from build_units.textures import blocks
from build_units.textures import colormap
from build_units.textures import effect
from build_units.textures import entity
from build_units.textures import environment
from build_units.textures import font
from build_units.textures import gui
from build_units.textures import items
from build_units.textures import map
from build_units.textures import misc
from build_units.textures import armor
from build_units.textures import painting
from build_units.textures import particle


# ./input/{pack}/assets/minecraft/textures
def build(path):

    vanilla_path = './resource/1.8.9/assets/minecraft/textures/'
    textures = ['blocks', 'colormap', 'effect', 'entity', 'environment', 'font', 'gui',
                'items', 'map', 'misc', 'models', 'painting', 'particle']
    check = textures

    for folder in os.scandir(path):
        name = folder.name

        if name == 'blocks' and blocks.Blocks(folder.path).build():
            check.remove(name)
            continue
        elif name == 'colormap' and colormap.Colormap(folder.path).build():
            check.remove(name)
            continue
        elif name == 'effect' and effect.Effect(folder.path).build():
            check.remove(name)
            continue
        elif name == 'entity' and entity.Entity(folder.path).build():
            check.remove(name)
            continue
        elif name == 'environment' and environment.Environment(folder.path).build():
            check.remove(name)
            continue
        elif name == 'font' and font.Font(folder.path).build():
            check.remove(name)
            continue
        elif name == 'gui' and gui.GUI(folder.path).build():
            check.remove(name)
            continue
        elif name == 'items' and items.Items(folder.path).build():
            check.remove(name)
            continue
        elif name == 'map' and map.Map(folder.path).build():
            check.remove(name)
            continue
        elif name == 'misc' and misc.Misc(folder.path).build():
            check.remove(name)
            continue
        elif name == 'models' and armor.Armor(os.path.join(folder.path, 'armor')).build():
            check.remove(name)
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

        if not cr.get('texture.' + texture):
            continue

        if texture not in check:
            continue

        gs.build_vanilla_dir(vanilla_path, path, texture)
