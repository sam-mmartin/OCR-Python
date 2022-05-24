import ocr_module as mod

list = "Projetos-Python", "OCR", "img", "teste03.png"
path_img = mod.filepath(list)
print(path_img)

img = mod.read_image(path_img)
mod.view_image(img)

gray = mod.gray_escale(img)
mod.view_image(gray)

# inversão de cores
invert = mod.color_invert(gray)
mod.view_image(invert)

# limiarização simples
val, thresh = mod.simple_thresholding(invert, 127)
mod.view_image(thresh)
print(val)

# metodo de OTSU
val, otsu = mod.otsu_thresholding(invert)
mod.view_image(otsu)
print(val)

# limiarização adaptativa
adapt = mod.adapt_thresholding(invert)
mod.view_image(adapt)

# limiarização adaptativa gaussiana
gauss = mod.gauss_thresholding(invert)
mod.view_image(gauss)
