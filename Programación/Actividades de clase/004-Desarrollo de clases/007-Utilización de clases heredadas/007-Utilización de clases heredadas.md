```
''' 
LatteArt y sus Artesanos
2025 Fabiana Victoria Sotillo
Programa de clases heredadas, 
para representar un negocio de café 
especializado en arte latte.
'''
```

---
En la programación orientada a objetos (POO), el concepto de herencia es un mecanismo que permite a una clase hija reutilizar los atributos y métodos de una clase padre, extendiendo su funcionalidad

Este ejercicio tiene como propósito reforzar la comprensión de estos conceptos al modelar una situación práctica, mostrando cómo una subclase puede ampliar las características de otra para adaptarse a un contexto más específico.

- Inicialmente se ha definido la clase base Cafe, con los atributos nombre, ubicacion y menu, inicializados en su constructor.
```
class Cafe():
	def __init__(self,nombre,ubicacion,menu):
		self.nombre = nombre
		self.ubicacion = ubicacion
		self.menu = menu
```

- A partir de esta clase se creó la subclase LatteArt, que hereda sus atributos mediante el uso de ```super().__init__()```. A esta subclase se añadió un nuevo atributo, artesanos, que almacena los nombres de las personas encargadas de elaborar los cafés.
```
class LatteArt(Cafe):
	def __init__(self, nombre, ubicacion, menu, artesanos):
		super().__init__(nombre,ubicacion,menu)    # Me traigo todo lo que tenga la clase superior
		self.artesanos = artesanos
```

- Dentro de LatteArt se implementaron dos métodos:

	- mostrar_menu(), que recorre e imprime los elementos del menú del café.
	```
	def mostrar_menu(self):	# Mostrar los elementos del menú
			print("Menú de ", self.nombre, ":")
			for elemento in self.menu:
				print("-",elemento)
	```

	- listar_artesanos(), que muestra los nombres de los baristas o artesanos especializados.
	```
	def listar_artesanos(self):	# Mostrar los nombres de los artesanos del café
			print("Artesanos del arte latte:")
			for artista in self.artesanos:
				print("-", artista)
	```

- Por último, se creó una instancia de la clase LatteArt con datos representativos de un café real y se ejecutaron ambos métodos para comprobar su funcionalidad.
```
mi_cafe = LatteArt(
    "Café DDL",
    "Centro de la ciudad",
    ["Capuchino", "Latte Vainilla", "Mocha"],
    ["Susana", "Pacheco", "Liliana"]
)

# Se prueban los métodos
mi_cafe.mostrar_menu()
mi_cafe.listar_artesanos()
```

---
A continuación se muestra el código funcional completo:

```
''' 
LatteArt y sus Artesanos
2025 Fabiana Victoria Sotillo
Programa de clases heredadas, 
para representar un negocio de café 
especializado en arte latte.
'''

class Cafe():
	def __init__(self, nombre, ubicacion, menu):
		self.nombre = nombre
		self.ubicacion = ubicacion
		self.menu = menu
		
class LatteArt(Cafe):
	def __init__(self, nombre, ubicacion, menu, artesanos):
		super().__init__(nombre, ubicacion, menu)    # Me traigo todo lo que tenga la clase superior
		self.artesanos = artesanos
   
	def mostrar_menu(self):	# Mostrar los elementos del menú
		print("Menú de", self.nombre, ":")
		for elemento in self.menu:
			print("-", elemento)

	def listar_artesanos(self):	# Mostrar los nombres de los artesanos del café
		print("Artesanos del arte latte:")
		for artista in self.artesanos:
			print("-", artista)
    

mi_cafe = LatteArt(
    "Café DDL",
    "Centro de la ciudad",
    ["Capuchino", "Latte Vainilla", "Mocha"],
    ["Susana", "Pacheco", "Liliana"]
)

# Prueba de los métodos
mi_cafe.mostrar_menu()
mi_cafe.listar_artesanos()
```

---
Este ejercicio permitió comprender y aplicar el concepto de herencia dentro de la programación orientada a objetos, observando cómo una subclase puede ampliar y especializar los atributos de una clase base. 

Mediante la implementación de Cafe y LatteArt, se logró modelar un ejemplo realista de un negocio de café, integrando organización jerárquica y reutilización de código. 

Esta práctica refuerza la importancia de las clases y la herencia como herramientas fundamentales para estructurar programas más claros, escalables y adaptables.


