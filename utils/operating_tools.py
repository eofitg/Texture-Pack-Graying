import os
import shutil
import utils.zip_tools as zt


input_path = './input/'
output_path = './output/'


def clear_output():
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        return
    if len(os.listdir(output_path)) != 0:
        delete_dir(output_path)
        os.makedirs(output_path)


def delete_dir(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)


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
        copy_file(src, get_parent_path(dst))


# Add this file / dir from 'input' to 'output' anyway
# means copy directly, without any manipulation
def build_anyway(src):
    copy(src, turn_output_path(src))


# Get output_path from custom pack path
# means turn input_path into output_path (No '/' at the end of path)
# just like replace the string "./input/" with "./output/" in a path
def turn_output_path(path):
    return os.path.join(output_path, get_relative_path(path, input_path))


# Get relative path from start in path
def get_relative_path(path, start):
    return os.path.relpath(path, start=start)


# Get parent path
def get_parent_path(path, depth: int = 1):
    for _ in range(depth):
        path = os.path.dirname(path)
    return os.path.normpath(path)


# Get pack list
def get_packs():
    dirs = []

    for item in os.scandir(input_path):

        if item.name.startswith('.'):
            continue

        _, ext = os.path.splitext(item.name)

        if item.is_file() and ext == '.zip':
            # decompress .zip files
            zt.decompress(item.path)

        dirs.append(item.name)

    return list(set(dirs))


# Get pack path by pack name
def get_pack_path(pack):
    return os.path.join(input_path, pack)

