from pathlib import Path
import pytesseract as pt
import cv2
import numpy as np


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


home = Path.home()
path_img = str(Path(home, "Projetos-Python", "OCR", "img", "Test3.png"))
print(home)
print(path_img)

config = 'tessdata-dir tessdata'

img = cv2.imread(path_img)
view_image(img)

gray = gray_escale(img)
view_image(gray)

val, thresh = otsu_thresholding(gray)
view_image(thresh)
print("Threshold:", val)
