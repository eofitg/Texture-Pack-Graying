import os
import shutil


input_path = './input/'
output_path = './output/'


def clear():
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        return
    if len(os.listdir(output_path)) != 0:
        del_dir(output_path)
        os.makedirs(output_path)


def copy(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copy(src, dst)


def copytree(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


# Copy this file/folder to dst path anyway
def copy_anyway(src, dst):
    s = str(src)
    if s.endswith('/'):
        s = src[:-1]
    name = s.split('/')[-1]
    if name.find('.') < 0:  # dirs
        copytree(src, dst)
    else:  # files
        copy(src, dst[:-len(name)])


def del_dir(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)


# Add this file/folder from 'input' to 'output' anyway
# means copy directly, without any manipulation
def build_anyway(src):
    copy_anyway(src, get_output_path(src))


# Turn input_path into output_path (No '/' at the end of path)
def get_output_path(path):
    return output_path + path[len(input_path):]
