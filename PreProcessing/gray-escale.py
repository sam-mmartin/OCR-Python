import cv2
import numpy as np


def view_image(img):
    cv2.imshow("sample", img)
    cv2.waitKey(2000)


img = cv2.imread('C:\\Users\\samc3\\Pictures\\teste03.png')
view_image(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
view_image(img)
