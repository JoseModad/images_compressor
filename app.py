from PIL import Image

image = Image.open("images/3calidad.jpg")

quality = 50

image.save("images/imagen_reducida.jpg", optimize=True, quality=quality)