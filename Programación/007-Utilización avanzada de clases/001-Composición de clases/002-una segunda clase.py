class Profesor():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email

class Alumno():
	def __init__(self,nombre,apellidos,email):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email

alumno1 = Alumno("Fabiana Victoria", "Sotillo", "info@fabiana.com")
print(alumno1)

profesor1 = Profesor("José Vicente", "Carratalá", "info@jocarsa.com")
print(profesor1)
