import pickle

menu =[]

while True:
	print("Opciones:")
	print("1.- Introducir nueva comida en el menú")
	print("2.- Listar nueva comida en el menú")
	print("3.- Guardar archivo")
	print("4.- Cargar datos de archivo")
	opcion = int(input("Selecciona una opción:"))
	if opcion == 1:
		comida = input("Introduce el nombre de la comida: ")
		menu.append(comida)
	elif opcion == 2:
		print("Tu comida hasta el momento es: ")
		for elemento in menu:
			print(elemento)
	elif opcion == 3:
		archivo = open("datos.bin","wb")	# Write Binary
		pickle.dump(menu,archivo)	# Primero lo que se guarda, luego en donde
		archivo.close()
		print("Se ha guardado con éxito ✅")
	elif opcion == 4:
		archivo = open("datos.bin","rb")	# Read Binary
		menu = pickle.load(archivo)	# Volcamos el archivo a la lista
		archivo.close()
