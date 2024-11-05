import os
import zipfile
import utils.operating_tools as ot


def decompress(path):
    # name with ext
    item_name = os.path.basename(path)
    # raw name without ext
    name, _ = os.path.splitext(item_name)

    parent_path = ot.get_parent_path(path)
    file = zipfile.ZipFile(path)
    file.extractall(os.path.join(parent_path, name))
    file.close()


def compress(path):
    with zipfile.ZipFile(path + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                new_name = os.path.relpath(file_path, start=path)
                zipf.write(file_path, new_name)
