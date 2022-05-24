import ocr_module as mod

list = "Projetos-Python", "OCR", "img", "Test2.jpg"
path_img = mod.filepath(list)
print(path_img)

img = mod.read_image(path_img)
mod.view_image(img)

img = mod.gray_escale(img)
mod.view_image(img)

maior = mod.max_redimension(img, 1.5)
mod.view_image(maior)

menor = mod.min_redimension(img, 0.5)
mod.view_image(menor)
