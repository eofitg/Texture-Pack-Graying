import os

import utils.operating_tools as ot
from utils import clean
from build_units import texture
from build_units import optifine
from build_units import model


building_message = True


input_path = './input/'
output_path = './output/'


if __name__ == '__main__':

    # clear output folder
    ot.clear()
    if building_message:
        print("Cleared output folder.")

    packs = ot.get_packs()
    for pack in packs:

        # ./input/{pack}/
        pack_path = ot.get_pack_path(pack)
        if building_message:
            print('Building ' + pack_path + ' ......')

        for file in os.scandir(pack_path):
            if file.is_file() and not file.name.startswith('.'):
                ot.copy(file.path, output_path + file.path[len(input_path):-len(file.name)])

        path = pack_path + '/assets/minecraft/'
        if not os.path.exists(path):
            error_message = 'Incorrect pack folder at \"' + path + '\".'
            print(error_message)
        # ./input/{pack}/assets/minecraft/
        for folder in os.scandir(path):
            name = folder.name
            if name.startswith('.'):
                continue
            if name == 'textures':
                texture.build(folder.path)
                continue
            elif name == 'mcpatcher':  # OptiFine folder, like sky and ctm textures
                optifine.build(folder.path)
                continue
            elif name == 'models':
                model.build(folder.path)
                continue

            # folders that never need to be greyed
            ot.build_anyway(folder.path)

    print("Done.")
