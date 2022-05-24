import ocr_module as mod

list = "Projetos-Python", "OCR", "img", "Test2.jpg"
path_img = mod.filepath(list)
print(path_img)

img = mod.read_image(path_img)

mod.view_image(img)
img = mod.gray_escale(img)

med_img = mod.medium_blur(img)
print("Medium blur filter")
mod.view_image(med_img)

gauss_img = mod.gaussian_blur(img)
print("Gaussian blur filter")
mod.view_image(gauss_img)

median_img = mod.median_blur(img)
print("Median blur filter")
mod.view_image(median_img)

bi_img = mod.bilateral_blur(img)
print("Bilateral blur filter")
mod.view_image(bi_img)
