import pickle
agenda = []

while True:
	print("=====Gestión de listas=====")
	print("1.-Insertar un registro")
	print("2.-Leer registros")
	print("3.-Guardar registros")
	print("4.-Eliminar registros")
	opcion = int(input("Selecciona una opción: "))
	
	if opcion == 1:
	# Insertar
		nombre = input("Dime tu nombre: ")
		apellidos = input("Dime tu apellido: ")
		email = input("Dime tu email: ")
		telefono = input("Dime tu telefono: ")
		agenda.append([nombre,apellidos,email,telefono])
		
	elif opcion == 2:
		# Imprimir
		print(agenda)
	
	elif opcion == 3:
		# Guardar
		archivo = open("agenda.bin",'wb')
		pickle.dump(agenda,archivo)
		archivo.close()
	
	elif opcion == 4:
		dato = int(input("Indica el número del elemento de la lista a eliminar: "))
		if 0 <= dato < len(agenda):
			agenda.pop(dato)
			print(agenda)
		else:
			print("Índice fuera de rango")

