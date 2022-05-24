from pathlib import Path
import Recog.recog_module as mod

home = Path.home()
path_img = str(Path(home, "Projetos-Python", "OCR", "img", "Test3.png"))
print(home)
print(path_img)

config = 'tessdata-dir tessdata'

img = mod.read_image(path_img)
mod.view_image(img)

gray = mod.gray_escale(img)
mod.view_image(gray)

val, thresh = mod.otsu_thresholding(gray)
mod.view_image(thresh)
print("Threshold:", val)
