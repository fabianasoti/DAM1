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
		rojo = 255 - rojo	# Rojo a negativo
		verde = 255 - verde	# verde a negativo
		azul = 255 - azul	# azul a negativo
		# Y sobreescribo el valor
		imagen.putpixel((x, y), (rojo, verde, azul))

imagen.save("modificado.jpg")

