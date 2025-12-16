from PIL import Image

# Open the image
imagen = Image.open("kermit.jpg")

# Get the first pixel (top-left corner)
pixel1 = imagen.getpixel((0, 0))

# Print the pixel tuple
print(pixel1)
