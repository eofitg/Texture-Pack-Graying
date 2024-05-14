import os


def build(path):
    for folder in os.scandir(path):
        name = folder.name
        if folder.is_file() or name.startswith('.'):
            continue
        if name == 'block':
            pass
        elif name == 'item':
            pass
        else:
            pass

