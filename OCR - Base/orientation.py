from PIL import Image
import matplotlib.pyplot as plt
import pytesseract
from ocr_module import filepath

list = "Projetos-Python", "OCR", "img", "Test2.jpg"
image = filepath(list)
print(pytesseract.image_to_osd(image))

img = Image.open(image)
plt.imshow(img)
plt.waitforbuttonpress()
