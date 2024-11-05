import os
import zipfile


def decompress(path):
    # name with ext
    item_name = os.path.basename(path)
    parent_path = path[:-len(item_name)]
    # raw name without ext
    name, _ = os.path.splitext(item_name)

    file = zipfile.ZipFile(path)
    file.extractall(parent_path + name)
    file.close()


def compress(path):
    with zipfile.ZipFile(path + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=path)
                zipf.write(file_path, arcname)
