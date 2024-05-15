import os

from build_units.textures import blocks


# ./{pack}/assets/minecraft/textures
def build(path):
    for folder in os.scandir(path):
        name = folder.name
        if folder.is_file() or name.startswith('.'):
            continue
        if name == 'blocks':
            block_builder = blocks.Blocks(folder.path)
            block_builder.build()
            # print(block_builder.vanilla_path)
        elif name == 'colormap':
            pass
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
