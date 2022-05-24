# import pytesseract
# import numpy as np
# import cv2

# config_tesseract = '--tessdata-dir tessdata'
# # Ler a imagem
# img = cv2.imread('C:\\Users\\samc3\\Pictures\\TesseractTest.jpg')
# # Converte para padrão RGB
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("sample", rgb)
# cv2.waitKey(2000)
# # Extrai o texto de uma imagem
# texto = pytesseract.image_to_string(rgb, lang="por", config=config_tesseract)
# print(texto)
