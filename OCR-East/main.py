from turtle import shape
import east_module as mod

w, h = 832, 480

list_path = ["Projetos-Python", "OCR", "img", "caneca.png"]
path = mod.filepath(list_path)
min_confiance = 0.9

img = mod.read_image(path)
mod.view_image(img)

# faz uma copia da imagem para posterior comparação
original = img.copy()

# Informa os atributos da imagem, como largura, altura e canais RGB
print(img.shape)

# calcula a proporção da imagem para realizar
# o preprocessamento para adequar a imagem a arquitetura east
height = img.shape[0]
width = img.shape[1]
w_ratio = width / float(w)
h_ratio = height / float(h)
print("Proporção da imagem:", w_ratio, h_ratio)

# redimensiona a imagem
img = mod.redimension(img, w, h)
print(img.shape)
mod.view_image(img)

# Carregamento da rede neural
layers = ['feature_fusion/Conv_7/Sigmoid', 'feature_fusion/concat_3']
list_path[2], list_path[3] = "OCR-East", "east"
list_path.append("frozen_east_text_detection.pb")
detector = mod.filepath(list_path)

neural = mod.neural_network(detector)

# converte a imagem para o formato suportado na arquitetura
blob = mod.convert_to_blob(img, w, h)

neural.setInput(blob)
scores, geometry = neural.forward(layers)

print("SCORES\n", scores)
print("GEOMETRY\n", geometry)

row, col = scores.shape[2:4]
boxs = []
confiances = []

for y in range(0, row):
    # print(y)
    data_scores = scores[0, 0, y]
    data_angles, x0, x1, x2, x3 = mod.geometry_data(geometry, y)

    for x in range(0, col):
        # print(x)
        if data_scores[x] < min_confiance:
            continue

        startX, startY, endX, endY = mod.geometry_calc(
            x, y, data_angles, x0, x1, x2, x3
        )

        confiances.append(data_scores[x])
        boxs.append((startX, startY, endX, endY))

print("CONFIANÇAS\n", confiances)
print("CAIXAS\n", boxs)

detection = mod.detections(boxs, confiances)
print("DETECÇÕES\n", detection)

origin_copy = original.copy()
cor = (255, 100, 0)
images = []

for (x, y, w, z) in detection:
    print(x, y, w, z)
    x = int(x * w_ratio)
    y = int(y * h_ratio)
    w = int(w * w_ratio)
    z = int(z * h_ratio)

    # region of interest
    roi = origin_copy[y:z, x:w]
    images.append(roi)
    mod.rectangle(original, x, y, w, z, cor)

mod.view_image(original)

for i in images:
    mod.view_image(i)
