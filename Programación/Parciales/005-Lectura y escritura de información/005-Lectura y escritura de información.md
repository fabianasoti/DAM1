```
'''
Gestión, lectura y escritura de datos con CRUD y Pickle
2025 Fabiana Victoria Sotillo
Mini aplicación CRUD, que almacena y gestiona la clase Cliente con  la librería Pickle
'''
```

---
La lectura y escritura de información en programación, especialmente en Python, es una habilidad esencial, ya que permite almacenar datos de forma permanente. Gracias a ello, los programas pueden conservar información incluso después de cerrarse, lo cual es fundamental para la persistencia de datos.

Para realizar estas operaciones, se utiliza la función open(), que permite abrir archivos y definir el modo de acceso:

- 'r' para lectura,

- 'w' para escritura.

Una vez abierto el archivo, se pueden emplear métodos como read(), readline() o readlines() para leer su contenido, y write() para escribir información en él. Finalmente, el método close() se usa para cerrar el archivo y liberar los recursos asociados.

Además, Python ofrece la biblioteca pickle, una herramienta muy útil para guardar el estado de un programa. Esta permite almacenar y recuperar objetos y clases completas en archivos, facilitando una gestión eficiente, estructurada y consistente de los datos.

El objetivo de este ejercicio es poner en práctica los conceptos previamente explicados mediante la creación de una clase llamada Cliente y el desarrollo de una miniaplicación CRUD (Create, Read, Update, Delete).
Esta aplicación permitirá crear, leer, actualizar y eliminar instancias de la clase de forma dinámica, implementando la biblioteca pickle para guardar los datos en archivos y recuperarlos posteriormente, garantizando así la persistencia de la información.

---
Para ello, se ejemplificará la construcción del código paso a paso:

- Se importa pickle.
```
import pickle
```

- Se crea una mini-clase de Cliente, solo con propiedades, sin métodos
```
class Cliente():	# mini-clase de Cliente, solo con propiedades, sin métodos
	def __init__(self, nombre, apellidos, email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
```

-Se crea una lista vacia de clientes
```
clientes = []	# Crea una lista vacia de clientes
```

- Se crea una mini-aplicacion CRUD con su pantalla de inicio y se muestra un menu, en el que el usuario podrá, crear clientes, o listar los clientes existentes (dentro de un bucle infinito while, atrapa los dos casos con if-elif)
```
print("_________________________")
print("Gestión de clientes v0.1")
print("Fabiana Victoria Sotillo")
print("_________________________")

while True:	
	archivo = open("clientes.bin",'wb')
	pickle.dump(clientes,archivo)	 
	archivo.close()
	
	print("Escoge una opción:")
	print("1.-Insertar un cliente")
	print("2.-Listar clientes")
	opcion = int(input("Escoge una opción: "))
```

- Luego se desarrolla cada una de las opciones para gestionar los datos de manera dinámica
```
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
```

-Se utiliza la librería pickle para guardar la lista de clientes cada vez que se crea uno
```
archivo = open("clientes.bin",'wb')
pickle.dump(clientes,archivo)	 
archivo.close()
```

- Se utiliza la libreria pickle para abrir los clientes, si existen, al abrir la aplicación. Se introduce ese intento de lectura en un try-except.
```
try:	
	archivo = open("clientes.bin",'rb')
	clientes = pickle.load(archivo)
	archivo.close()
except:
	print("No existe archivo de datos")
```

---
A continuación se ilustra el código funcional completo:


```
```
'''
Gestión, lectura y escritura de datos con CRUD y Pickle
2025 Fabiana Victoria Sotillo
Mini aplicación CRUD, que almacena y gestiona la clase Cliente con la librería Pickle
'''
```

---
La lectura y escritura de información en programación, especialmente en Python, es una habilidad esencial, ya que permite almacenar datos de forma permanente. Gracias a ello, los programas pueden conservar información incluso después de cerrarse, lo cual es fundamental para la persistencia de datos.

Para realizar estas operaciones, se utiliza la función open(), que permite abrir archivos y definir el modo de acceso:

- 'r' para lectura,

- 'w' para escritura.

Una vez abierto el archivo, se pueden emplear métodos como read(), readline() o readlines() para leer su contenido, y write() para escribir información en él. Finalmente, el método close() se usa para cerrar el archivo y liberar los recursos asociados.

Además, Python ofrece la biblioteca pickle, una herramienta muy útil para guardar el estado de un programa. Esta permite almacenar y recuperar objetos y clases completas en archivos, facilitando una gestión eficiente, estructurada y consistente de los datos.

El objetivo de este ejercicio es poner en práctica los conceptos previamente explicados mediante la creación de una clase llamada Cliente y el desarrollo de una miniaplicación CRUD (Create, Read, Update, Delete).
Esta aplicación permitirá crear, leer, actualizar y eliminar instancias de la clase de forma dinámica, implementando la biblioteca pickle para guardar los datos en archivos y recuperarlos posteriormente, garantizando así la persistencia de la información.

---
Para ello, se ejemplificará la construcción del código paso a paso:

- Se importa pickle.
```
import pickle
```

- Se crea una mini-clase de Cliente, solo con propiedades, sin métodos
```
class Cliente():	# mini-clase de Cliente, solo con propiedades, sin métodos
	def __init__(self, nombre, apellidos, email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
```

- Se crea una lista vacia de clientes
```
clientes = []	# Crea una lista vacia de clientes
```

- Se crea una mini-aplicacion CRUD con su pantalla de inicio y se muestra un menu, en el que el usuario podrá, crear clientes, o listar los clientes existentes (dentro de un bucle infinito while, atrapa los dos casos con if-elif)
```
print("_________________________")
print("Gestión de clientes v0.1")
print("Fabiana Victoria Sotillo")
print("_________________________")

while True:	
	archivo = open("clientes.bin",'wb')
	pickle.dump(clientes,archivo)	 
	archivo.close()
	
	print("Escoge una opción:")
	print("1.-Insertar un cliente")
	print("2.-Listar clientes")
	opcion = int(input("Escoge una opción: "))
```

- Luego se desarrolla cada una de las opciones para gestionar los datos de manera dinámica
```
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
```

- Se utiliza la librería pickle para guardar la lista de clientes cada vez que se crea uno
```
archivo = open("clientes.bin",'wb')
pickle.dump(clientes,archivo)	 
archivo.close()
```

- Se utiliza la libreria pickle para abrir los clientes, si existen, al abrir la aplicación. Se introduce ese intento de lectura en un try-except.
```
try:	
	archivo = open("clientes.bin",'rb')
	clientes = pickle.load(archivo)
	archivo.close()
except:
	print("No existe archivo de datos")
```

---
A continuación se ilustra el código funcional completo:


```
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
```

---
A lo largo de este ejercicio se aplicaron los conceptos fundamentales sobre lectura y escritura de archivos en Python, reforzando el uso de la biblioteca pickle para la persistencia de datos.

La creación de la clase Cliente y el desarrollo de una miniaplicación CRUD permitieron poner en práctica la gestión dinámica de objetos, mostrando cómo crear y leer  información de forma estructurada.

Además, el uso de estructuras de control como bucles e instrucciones condicionales, junto con el manejo de excepciones mediante try y except, contribuyó a un programa más funcional y bien estructurado

Este ejercicio permite consolidar los conocimientos sobre manejo de archivos y persistencia de datos, trabajando con los fundamentos de la programación orientada a objetos y la organización lógica de un sistema CRUD, habilidades esenciales para el desarrollo de aplicaciones más complejas y completas.
