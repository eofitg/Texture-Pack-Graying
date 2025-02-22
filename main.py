import os

import utils.zip_tools as zt
import utils.operating_tools as ot
import utils.grayscaling as gs
import config_reader as cr
from utils import clean
from build_units import texture
from build_units import optifine
from build_units import model


building_message = True

build_cover_image = cr.get('build_cover_image')  # boolean


# if or not this path only has one dir
# True -> return the path of this dir
# False -> return ""
def nest_check(_path):
    count = False
    res_path = ""

    for item in os.scandir(_path):

        # ignore hidden items
        if item.name.startswith('.'):
            continue

        # should not have any files
        if item.is_file():
            return ""

        # found dir
        else:
            if not count:
                count = True
                res_path = item.path

            # found another dir while has counted one
            else:
                return ""

    # return the only directory's path
    return res_path


if __name__ == '__main__':

    # clear output folder
    ot.clear_output()
    if building_message:
        print("Cleared output folder.")

    packs = ot.get_packs()
    for pack in packs:

        is_zip = False
        if pack.endswith('.zip'):
            is_zip = True
            pack = os.path.splitext(pack)[0]

        # ./input/{pack}/
        pack_path = ot.get_pack_path(pack)
        pack_path_backup = pack_path
        if building_message:
            print('Building ' + pack_path + ' ......')

        # this pack may be nested like
        # ./input/XXX/{pack}
        # for this, recognize dirs with only 1 internal dir as a layer of nesting
        if nest_check(pack_path) != "":
            pack_path = nest_check(pack_path)
            if building_message:
                print("Building nested dir \"" + pack_path + "\" ......")

        # build files in ./input/{pack}/, like pack.png and pack.mcmeta
        for file in os.scandir(pack_path):
            if not file.is_file():
                continue
            if file.name == 'pack.png' and build_cover_image:
                gs.build_file(file.path)
                continue

            ot.build_anyway(file.path)

        # try to get assets dir
        path = os.path.join(pack_path, 'assets/minecraft/')
        if not os.path.exists(path):
            error_message = 'Invalid pack folder at \"' + path + '\".'
            print(error_message)
            continue

        # ./input/{pack}/assets/minecraft/
        for folder in os.scandir(path):
            name = folder.name
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

        # Compress output
        zt.compress(ot.turn_output_path(pack_path))
        if building_message:
            print("Compressed output files.")

        # Delete previously decompressed dirs in the "input" folder
        if is_zip:
            ot.delete_dir(pack_path_backup)
        # Delete building dirs in the "output" folder
        ot.delete_dir(ot.turn_output_path(pack_path))
        if building_message:
            print("Cleared extra files.")

    print("Done.")
