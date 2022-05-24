import ocr_module as mod

config = 'tessdata-dir tessdata'

list = "Projetos-Python", "OCR", "img", "Test1.jpg"
path_img = mod.filepath(list)

img = mod.read_image(path_img)
mod.view_image(img)

rgb = mod.convert_to_rgb(img)
mod.view_image(rgb)

result = mod.extract_as_dict(rgb, "por", config)

for k, v in result.items():
    print(k, v)

min_conf = 40
cor = (255, 100, 0)
img_copy = rgb.copy()

for i in range(0, len(result['text'])):
    confiance = float(result['conf'][i])

    if confiance > min_conf:
        x, y, img = mod.text_box(i, result, img_copy, cor)
        print(x, y)

mod.view_image(img_copy)
