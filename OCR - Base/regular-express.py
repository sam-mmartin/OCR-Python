import pytesseract as pt
import numpy as np
import cv2
import re

img = cv2.imread('C:\\Users\\samc3\\Pictures\\teste03.png')
cv2.imshow("sample", img)
cv2.waitKey(2000)

config = 'tessdata-dir tessdata'
result = pt.image_to_data(img, config=config, lang="por",
                          output_type=pt.Output.DICT)

for k, v in result.items():
    print(k, v)

expression = r"\b\w[OCR]"
min_conf = 40
img_copy = img.copy()


def text_box(text, img, cor=(255, 100, 0)):
    x = text['left'][i]
    y = text['top'][i]
    w = text['width'][i]
    h = text['height'][i]

    cv2.rectangle(img, (x, y), (x + w, y + h), cor, 2)

    return x, y, img


words = []
for i in range(0, len(result['text'])):
    confiance = float(result['conf'][i])
    if (confiance > min_conf):
        text = result['text'][i]

        if re.match(expression, text):
            print("expressão encontrada: ", text)
            x, y, img = text_box(result, img_copy)
            words.append(text)

print(words)
cv2.imshow("sample", img_copy)
cv2.waitKey(2000)
