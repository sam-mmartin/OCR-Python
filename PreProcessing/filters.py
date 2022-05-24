import cv2
import numpy as np


def view_image(img):
    cv2.imshow("sample", img)
    cv2.waitKey(2000)


def gray_escale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def medium_blur(img):
    return cv2.blur(img, (5, 5))


def gaussian_blur(img):
    return cv2.GaussianBlur(img, (5, 5), 0)


def median_blur(img):
    return cv2.medianBlur(img, 3)


def bilateral_blur(img):
    return cv2.bilateralFilter(img, 15, 55, 45)


img = cv2.imread('C:\\Users\\samc3\\Pictures\\Test2.jpg')

view_image(img)
img = gray_escale(img)

med_img = medium_blur(img)
print("Medium blur filter")
view_image(med_img)

gauss_img = gaussian_blur(img)
print("Gaussian blur filter")
view_image(gauss_img)

median_img = median_blur(img)
print("Median blur filter")
view_image(median_img)

bi_img = bilateral_blur(img)
print("Bilateral blur filter")
view_image(bi_img)
