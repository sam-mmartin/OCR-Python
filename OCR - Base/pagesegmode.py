import ocr_module as mod

config_tesseract = '--tessdata-dir tessdata --psm 6'

# Ler a imagem
list = "Projetos-Python", "OCR", "img", "Test2.jpg"
path_img = mod.filepath(list)

img = mod.read_image(path_img)
mod.view_image(img)

# Converte para padrão RGB
rgb = mod.convert_to_rgb(img)

# Extrai o texto de uma imagem
texto = mod.extract_text(rgb)
print(texto)
