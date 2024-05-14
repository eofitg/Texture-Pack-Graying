import cv2

input_path = 'input/'


def gs(path):
    im = cv2.imread(input_path + path)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return gray


def img_gs(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

