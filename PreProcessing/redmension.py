import cv2
import numpy as np


def view_image(img):
    cv2.imshow("sample", img)
    cv2.waitKey(2000)


def gray_escale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#img = cv2.imread('C:\\Users\\samc3\\Pictures\\teste03.png')
img = cv2.imread('C:\\Users\\samc3\\Pictures\\Test2.jpg')
view_image(img)
img = gray_escale(img)

maior = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
view_image(maior)

menor = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
view_image(menor)
