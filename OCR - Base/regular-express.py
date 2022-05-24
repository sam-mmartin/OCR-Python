import re
import ocr_module as mod

config = 'tessdata-dir tessdata'

list = "Projetos-Python", "OCR", "img", "teste03.png"
path_img = mod.filepath(list)

img = mod.read_image(path_img)
mod.view_image(img)

result = mod.extract_as_dict(img, "por", config)

for k, v in result.items():
    print(k, v)

expression = r"\b\w[OCR]"
min_conf = 40
img_copy = img.copy()
words = []
cor = (255, 100, 0)

for i in range(0, len(result['text'])):
    confiance = float(result['conf'][i])
    if (confiance > min_conf):
        text = result['text'][i]

        if re.match(expression, text):
            print("expressão encontrada: ", text)
            x, y, img = mod.text_box(i, result, img_copy, cor)
            words.append(text)

print(words)
mod.view_image(img_copy)
