import pytesseract
import cv2
from pytesseract import Output

# img = cv2.imread('C:\\Users\\samc3\\Pictures\\TesseractTest.jpg')
img = cv2.imread('C:\\Users\\samc3\\Pictures\\Test1.jpg')
# img = cv2.imread('C:\\Users\\samc3\\Pictures\\Test2.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = '--tessdata-dir tessdata'
result = pytesseract.image_to_data(
    rgb, config=config, lang='por', output_type=Output.DICT)

for k, v in result.items():
    print(k, v)

min_conf = 40


def text_box(text, img, cor=(255, 100, 0)):
    x = text['left'][i]
    y = text['top'][i]
    w = text['width'][i]
    h = text['height'][i]

    cv2.rectangle(img, (x, y), (x + w, y + h), cor, 2)

    return x, y, img


img_copy = rgb.copy()

for i in range(0, len(result['text'])):
    confiance = float(result['conf'][i])

    if confiance > min_conf:
        x, y, img = text_box(result, img_copy)
        print(x, y)

cv2.imshow("sample", img_copy)
cv2.waitKey(2000)
