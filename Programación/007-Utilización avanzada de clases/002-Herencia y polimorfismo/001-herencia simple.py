class Persona():
	def __init__(self,nombre,apellidos,email,direccion):
		self.nombre = nombre
		self.apellidos = apellidos
	def dameDatos(self):
			return self.nombre+self.apellidos		
		
class Profesor(Persona):
	def __init__(self,nombre,apellidos):
		super().__init__(nombre,apellidos)
		
class Alumno(Persona):
	def __init__(self,nombre,apellidos):
		super().__init__(nombre,apellidos)
				
alumno1 = Alumno("Fabiana Victoria", "Sotillo")
print(alumno1.dameDatos())

profesor1 = Profesor("José Vicente", "Carratalá")
print(profesor1.dameDatos())
