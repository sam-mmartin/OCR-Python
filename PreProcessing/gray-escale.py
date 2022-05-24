import ocr_module as mod

list = "Projetos-Python", "OCR", "img", "teste03.png"
path_img = mod.filepath(list)
print(path_img)

img = mod.read_image(path_img)
mod.view_image(img)

gray = mod.gray_escale(img)
mod.view_image(img)
