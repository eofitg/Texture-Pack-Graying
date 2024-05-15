import os

from build_units.textures import blocks
from build_units.textures import colormap
from build_units.textures import entity


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
            pass
        elif name == 'environment':
            pass
        elif name == 'gui':
            pass
        elif name == 'items':
            pass
        elif name == 'map':
            pass
        elif name == 'armor':
            pass
        elif name == 'painting':
            pass
        elif name == 'particle':
            pass
