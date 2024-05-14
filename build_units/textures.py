import os


def build(path):
    for folder in os.scandir(path):
        name = folder.name
        if folder.is_file() or name.startswith('.'):
            continue
        if name == 'blocks':
            pass
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
