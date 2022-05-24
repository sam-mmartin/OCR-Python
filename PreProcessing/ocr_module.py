from pathlib import Path
import cv2
import numpy as np


def view_image(img):
    cv2.imshow("sample", img)
    cv2.waitKey(2000)


def filepath(list):
    temp = Path.home()
    for i in list:
        temp = Path(temp, i)
    return str(temp)


def read_image(path):
    return cv2.imread(path)


def gray_escale(img):
    print("Escala de cinza")
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def medium_blur(img):
    return cv2.blur(img, (5, 5))


def gaussian_blur(img):
    return cv2.GaussianBlur(img, (5, 5), 0)


def median_blur(img):
    return cv2.medianBlur(img, 3)


def bilateral_blur(img):
    return cv2.bilateralFilter(img, 15, 55, 45)


def color_invert(img):
    print("Inversão de cores")
    return 255 - img


def min_redimension(img, ratio):
    print("Redimensionamento menor")
    return cv2.resize(
        img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA
    )


def max_redimension(img, ratio):
    print("Redimensionamento maior")
    return cv2.resize(
        img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_CUBIC
    )


def simple_thresholding(img, thresh):
    print("limiarização simples")
    return cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)


def otsu_thresholding(img):
    print("limiarização simples com otsu")
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


def adapt_thresholding(img):
    print("limiarização adaptativa")
    return cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9
    )


def gauss_thresholding(img):
    print('limiarização adaptativa gaussiana')
    return cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9
    )


def erosao(img):
    print("Erosão")
    return cv2.erode(img, np.ones((2, 2), np.uint8))


def dilatacao(img):
    print("Dilatação")
    return cv2.dilate(img, np.ones((3, 3), np.uint8))
