import os
import shutil
import utils.zip_tools as zt


input_path = './input/'
output_path = './output/'


def clear():
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        return
    if len(os.listdir(output_path)) != 0:
        del_dir(output_path)
        os.makedirs(output_path)


# dst: parent folder path
def copy_file(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copy(src, dst)


# dst: this folder path
def copy_dir(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


# Copy this file / dir to dst path
def copy(src, dst):
    if os.path.isdir(src):  # dir
        copy_dir(src, dst)
    elif os.path.isfile(src):  # file
        copy_file(src, get_parent(dst))


# Get parent folder
def get_parent(path: str):
    if path.endswith(os.sep):
        path = path[:-1]

    return os.path.dirname(path)


# Add this file / dir from 'input' to 'output' anyway
# means copy directly, without any manipulation
def build_anyway(src):
    copy(src, get_output_path(src))


def del_dir(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)


# Get pack list
def get_packs():
    dirs = []

    for item in os.scandir(input_path):

        raw_name, ext = os.path.splitext(item.name)

        if item.is_dir():
            dirs.append(get_rela_path(item.path, input_path))

        elif item.is_file() and ext == '.zip':
            # decompress .zip files
            zt.decompress(item.path)
            dirs.append(raw_name)

    return list(set(dirs))


# Get pack path by pack name
def get_pack_path(pack):
    return os.path.join(input_path, pack)


# Get relative path from start in path
def get_rela_path(path, start):
    return os.path.relpath(path, start=start)


# Turn input_path into output_path (No '/' at the end of path)
def get_output_path(path):
    return os.path.join(output_path, get_rela_path(path, input_path))
