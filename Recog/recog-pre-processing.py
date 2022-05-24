import pytesseract as pt
import cv2
import numpy as np


def view_image(img):
    cv2.imshow("sample", img)
    cv2.waitKey(2000)


def gray_escale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


config = 'tessdata-dir tessdata'

img = cv2.imread('C:\\Users\\samc3\\Pictures\\Test2.jpg')
text = pt.image_to_string(img, lang='por', config=config)
view_image(img)
print(text)

gray = gray_escale(img)
