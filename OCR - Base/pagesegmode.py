import pytesseract
import numpy as np
import cv2

config_tesseract = '--tessdata-dir tessdata --psm 6'
# Ler a imagem
img = cv2.imread('C:\\Users\\samc3\\Pictures\\Test2.jpg')
# Converte para padrão RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Extrai o texto de uma imagem
texto = pytesseract.image_to_string(rgb, lang="por", config=config_tesseract)
print(texto)
