from PIL import Image

imagen = Image.open("kermit.jpg")

anchura,altura = imagen.size	# Cojo altura y anchura

for x in range(0,anchura):	# Repaso la anchura
	for y in range(0,altura):	# Repaso la altura
		pixel = imagen.getpixel((x,y))	# Cojo cada pixel
		# Primero leo los componentes de color
		rojo = pixel[0]
		verde = pixel[1]
		azul = pixel[2]
		# Ahora le subo el tono de color (aclaro)
		rojo += 20
		verde += 20
		azul += 20
		# Y sobreescribo el valor
		imagen.putpixel((x, y), (rojo, verde, azul))

imagen.save("modificado.jpg")

