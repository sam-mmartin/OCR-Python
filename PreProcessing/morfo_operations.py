import ocr_module as mod


list = "Projetos-Python", "OCR", "img", "teste04.jpg"
path_img = mod.filepath(list)
print(path_img)

img = mod.read_image(path_img)
mod.view_image(img)

gray = mod.gray_escale(img)

i_tresh = mod.adapt_thresholding(gray)
mod.view_image(i_tresh)

invert = mod.color_invert(i_tresh)
mod.view_image(invert)

# Erosão, dilatação, abertura e fechamento
# Abertura
i_erode = mod.erosao(invert)
mod.view_image(i_erode)
i_dilate = mod.dilatacao(i_erode)
mod.view_image(i_dilate)
i_redimen = mod.redimension(i_dilate)
mod.view_image(i_redimen)

# Fechamento
i_dilate = mod.dilatacao(invert)
mod.view_image(i_dilate)
i_erode = mod.erosao(i_dilate)
mod.view_image(i_erode)
i_redimen = mod.redimension(i_dilate)
mod.view_image(i_redimen)
