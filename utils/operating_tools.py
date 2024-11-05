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
    s = str(src)
    if s.endswith('/'):
        s = src[:-1]
    name = s.split('/')[-1]
    if name.find('.') < 0:  # dir
        copy_dir(src, dst)
    else:  # file
        copy_file(src, dst[:-len(name)])


def del_dir(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)


# Add this file / dir from 'input' to 'output' anyway
# means copy directly, without any manipulation
def build_anyway(src):
    copy(src, get_output_path(src))


# Get pack list
def get_packs():
    dirs = []
    for item in os.scandir(input_path):
        if item.is_dir():
            dirs.append(item.path[len(input_path):])
        elif item.is_file() and item.name.endswith('.zip'):
            # decompress .zip files
            zt.decompress(item.path)
            dirs.append(item.path[len(input_path):-4])
    return list(set(dirs))


# Get pack path by pack name
def get_pack_path(pack):
    return os.path.join(input_path, pack)


# Turn input_path into output_path (No '/' at the end of path)
def get_output_path(path):
    return output_path + path[len(input_path):]
