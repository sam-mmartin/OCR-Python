import cv2
import numpy as np


def view_image(img):
    cv2.imshow("sample", img)
    cv2.waitKey(2000)


def gray_escale(img):
    print("Escala de cinza")
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def color_invert(img):
    print("Inversão de cores")
    return 255 - img


def redimension(img):
    print("Redimensionamento")
    return cv2.resize(
        img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA
    )


def adapt_thresholding(img):
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


img = cv2.imread('C:\\Users\\samc3\\Pictures\\teste04.jpg')
view_image(img)
gray = gray_escale(img)

i_tresh = adapt_thresholding(gray)
view_image(i_tresh)

invert = color_invert(i_tresh)
view_image(invert)

# Erosão, dilatação, abertura e fechamento
# Abertura
i_erode = erosao(invert)
view_image(i_erode)
i_dilate = dilatacao(i_erode)
view_image(i_dilate)
i_redimen = redimension(i_dilate)
view_image(i_redimen)

# Fechamento
i_dilate = dilatacao(invert)
view_image(i_dilate)
i_erode = erosao(i_dilate)
view_image(i_erode)
i_redimen = redimension(i_dilate)
view_image(i_redimen)
