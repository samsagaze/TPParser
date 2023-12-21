from PIL import Image

hauteur, largeur = 10, 10
new_image = Image.new("L", (largeur, hauteur), 0)
pixels = new_image.load()
for y in range(hauteur):
    for x in range(largeur):
        gray_value = int((x + y) / 2)
        pixels[x, y] = gray_value
new_image.show()
new_image.close()

