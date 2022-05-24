from distutils.command.config import config
from pathlib import Path
import pytesseract as pt
import cv2
import numpy as np


def filepath(list):
    temp = Path.home()
    for i in list:
        temp = Path(temp, i)
    return str(temp)


def read_image(path):
    return cv2.imread(path)


def view_image(img):
    cv2.imshow("sample", img)
    cv2.waitKey(2000)


def gray_escale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def simple_thresholding(img):
    print('limiarização simples')
    return cv2.threshold(
        img, 180, 255, cv2.THRESH_BINARY
    )


def otsu_thresholding(img):
    print("limiarização simples com método otsu")
    return cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY | cv2. THRESH_OTSU
    )


def invert(img):
    return 255 - img


def ocr(img, lang, config):
    print(pt.image_to_string(img, lang=lang, config=config))
