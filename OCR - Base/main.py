import ocr_module as mod

config_tesseract = 'tessdata-dir tessdata'

# Ler a imagem
list = "Projetos-Python", "OCR", "img", "TesseractTest.jpg"
path_img = mod.filepath(list)
img = mod.read_image(path_img)

# Converte para padrão RGB
rgb = mod.convert_to_rgb(img)
mod.view_image(rgb)

# Extrai o texto de uma imagem
texto = mod.extract_text(rgb, "por", config_tesseract)
print(texto)
