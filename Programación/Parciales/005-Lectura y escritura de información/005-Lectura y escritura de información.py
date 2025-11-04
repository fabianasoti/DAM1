'''
Gestión, lectura y escritura de datos con CRUD y Pickle
2025 Fabiana Victoria Sotillo
Mini aplicación CRUD, que almacena y gestiona la clase Cliente con la librería Pickle
'''

import pickle

class Cliente():	# mini-clase de Cliente, solo con propiedades, sin métodos
	def __init__(self, nombre, apellidos, email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email

# CRUD

print("_________________________")
print("Gestión de clientes v0.1")
print("Fabiana Victoria Sotillo")
print("_________________________")

clientes = []	# Crea una lista vacia de clientes

# Utiliza la libreria pickle para abrir los clientes, si existen, al abrir la aplicación 
# (es recomendable introducir ese intento de lectura en un try-except)
try:	
	archivo = open("clientes.bin",'rb')
	clientes = pickle.load(archivo)
	archivo.close()
except:
	print("No existe archivo de datos")

# Ofrece un menu, en el que el usuario podrá, crear clientes, o listar los clientes existentes 
# (dentro de un bucle infinito while, atrapa los dos casos con if-elif)
while True:	
	# Utiliza la librería pickle para guardar la lista de clientes cada vez que se crea uno
	archivo = open("clientes.bin",'wb')
	pickle.dump(clientes,archivo)	 
	archivo.close()
	
	print("Escoge una opción:")
	print("1.-Insertar un cliente")
	print("2.-Listar clientes")
	opcion = int(input("Escoge una opción: "))
	
	if opcion == 1:
		nombre = input("Introduce el nombre: ")
		apellidos = input("Introduce los apellidos: ")
		email = input("Introduce el email: ")
		clientes.append(Cliente(nombre,apellidos,email))
	elif opcion == 2:
		identificador = 0
		for cliente in clientes:
			print("Este es el cliente con ID:", identificador)
			print(cliente.nombre,cliente.apellidos,cliente.email)
			identificador += 1
	else:
			print("Opción no válida")
