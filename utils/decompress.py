import zipfile

input_path = 'input/'


def dec(file_name):
    file = zipfile.ZipFile(input_path + file_name)
    file.extractall(input_path + file_name[:-4])
    file.close()
