import os
import shutil


input_path = './input/'
output_path = './output/'


def copy(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copy(src, dst)


def copytree(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


# No '/' at the end of path
def get_output_path(path):
    return output_path + path[len(input_path):]
