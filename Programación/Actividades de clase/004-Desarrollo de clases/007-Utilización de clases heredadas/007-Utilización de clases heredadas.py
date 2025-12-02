''' 
LatteArt y sus Artesanos
2025 Fabiana Victoria Sotillo
Programa de clases heredadas, 
para representar un negocio de café 
especializado en arte latte.
'''

class Cafe():
	def __init__(self,nombre,ubicacion,menu):
		self.nombre = nombre
		self.ubicacion = ubicacion
		self.menu = menu
		
class LatteArt(Cafe):
	def __init__(self, nombre, ubicacion, menu, artesanos):
		super().__init__(nombre,ubicacion,menu)    # Me traigo todo lo que tenga la clase superior
		self.artesanos = artesanos
   
	def mostrar_menu(self):	# Mostrar los elementos del menú
		print("Menú de ", self.nombre, ":")
		for elemento in self.menu:
			print("-",elemento)

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
