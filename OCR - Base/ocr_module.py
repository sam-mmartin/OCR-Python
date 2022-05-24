from pathlib import Path

import cv2
import numpy as np
import pytesseract as pt


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


def convert_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def rectangle(img, x, y, w, h, cor):
    cv2.rectangle(img, (x, y), (x + w, y + h), cor, 2)


def text_box(i, text, img, cor):
    x = text['left'][i]
    y = text['top'][i]
    w = text['width'][i]
    h = text['height'][i]

    rectangle(img, x, y, w, h, cor)

    return x, y, img


def extract_text(img, lang, config):
    return pt.image_to_string(img, lang=lang, config=config)


def extract_as_dict(img, lang, config):
    return pt.image_to_data(
        img, config=config, lang=lang, output_type=pt.Output.DICT
    )
