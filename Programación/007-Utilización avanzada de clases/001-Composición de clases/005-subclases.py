class Persona():
	def __init__(self,nombre,apellidos,email,direccion):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.direccion = direccion
	def dameDatos(self):
			return self.nombre+self.apellidos		
		
class Profesor(Persona):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)
		
class Alumno(Persona):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)
		
class AlumnoOnline(Alumno):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)
		
class AlumnoPresencial(Alumno):
	def __init__(self,nombre,apellidos,email,direccion):
		super().__init__(nombre,apellidos,email,direccion)

				
alumno1 = Alumno("Fabiana Victoria", "Sotillo", "info@fabiana.com","Calle de Fabiana")
print(alumno1.dameDatos())

profesor1 = Profesor("José Vicente", "Carratalá", "info@jocarsa.com","Calle de Jose")
print(profesor1.dameDatos())
