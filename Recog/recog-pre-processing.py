from pathlib import Path
import recog_module as mod

list = "Projetos-Python", "OCR", "img", "Test3.png"
path_img = mod.filepath(list)
print(path_img)

config = 'tessdata-dir tessdata'

img = mod.read_image(path_img)
mod.view_image(img)

gray = mod.gray_escale(img)
mod.view_image(gray)

val, thresh = mod.otsu_thresholding(gray)
mod.view_image(thresh)
print("Threshold:", val)

inv = mod.invert(thresh)
mod.view_image(inv)

mod.ocr(inv, "por", config)
