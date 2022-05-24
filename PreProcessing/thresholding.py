import cv2
import numpy as np


def view_image(img):
    cv2.imshow("sample", img)
    cv2.waitKey(2000)


img = cv2.imread('C:\\Users\\samc3\\Pictures\\teste03.png')
#img = cv2.imread('C:\\Users\\samc3\\Pictures\\Test1.jpg')
view_image(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
view_image(gray)

# inversão de cores
invert = 255 - gray
view_image(invert)

gray = invert

# limiarização simples
print('limiarização simples')
val, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
view_image(thresh)
print(val)

# metodo de OTSU
print('metodo de OTSU')
val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
view_image(otsu)
print(val)

# limiarização adaptativa
print('limiarização adaptativa')
adapt = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
view_image(adapt)

# limiarização adaptativa gaussiana
print('limiarização adaptativa gaussiana')
gauss = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9
)
view_image(gauss)
