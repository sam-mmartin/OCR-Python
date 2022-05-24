import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
from pathlib import Path


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


def redimension(img, w, h):
    print("Redimensionamento de imagem")
    return cv2.resize(img, (w, h))


def rectangle(img, x, y, w, h, cor):
    cv2.rectangle(img, (x, y), (w, h), cor, 2)


def neural_network(file):
    return cv2.dnn.readNet(file)


def convert_to_blob(img, w, h):
    return cv2.dnn.blobFromImage(img, 1.0, (w, h), swapRB=True, crop=False)


def geometry_data(geo, y):
    xData0 = geo[0, 0, y]
    xData1 = geo[0, 1, y]
    xData2 = geo[0, 2, y]
    xData3 = geo[0, 3, y]
    angleData = geo[0, 4, y]

    return angleData, xData0, xData1, xData2, xData3


def geometry_calc(x, y, angleData, xData0, xData1, xData2, xData3):
    (offsetX, offsetY) = (x * 4.0, y * 4.0)
    angle = angleData[x]
    cos = np.cos(angle)
    sin = np.sin(angle)
    h = xData0[x] + xData2[x]
    w = xData1[x] + xData3[x]
    endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
    endY = int(offsetY + (sin * xData1[x]) + (cos * xData2[x]))
    startX = int(endX - w)
    startY = int(endY - h)

    return startX, startY, endX, endY


def detections(box, confiance):
    return non_max_suppression(np.array(box), probs=confiance)
