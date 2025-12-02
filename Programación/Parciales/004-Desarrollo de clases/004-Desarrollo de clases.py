'''
Actividad de final de unidad - Desarrollo de clases
2025 Fabiana Victoria Sotillo
Programa que crea clase, define constructor, crea instancias y hace uso del método set y get
'''

# Crea una clase Cliente
class Cliente(): 
	# Añadele propiedades (nombre, apellidos, email, etc)
	# Crea un constructor con parametros (nombre, apellidos etc en la instanciación del objeto)
	def _init_(self,nombre,apellido,email,direccion):
		self.nombre = ""
		self.apellido = ""
		self.email = "" 
		self.direccion = ""
	
	def setDireccion(self, nuevadireccion):
		# Crea al menos un metodo set y un metodo get para una de las propiedades
		self.direccion = nuevadireccion
	def setEmail(self, nuevoemail):
		self.email = nuevoemail
    
	def getDireccion(self):
		return self.direccion
	def getEmail(self):
		return self.email
      
# Una vez creada la clase, crea tres instancias de la clase, cada una de ellas con sus propias propiedades
cliente1 = Cliente()
cliente1.nombre = "Fabiana Victoria"
cliente1.apellido = "Sotillo"
cliente1.email = "info@fabiana.com"
cliente1.direccion = "calle de Fabiana"

cliente2 = Cliente()
cliente2.nombre = "Juan"
cliente2.apellido = "López"
cliente2.email = "info@juan.com"
cliente2.direccion = "la calle de Juan"

cliente3 = Cliente()
cliente3.nombre = "Pacheco"
cliente3.apellido = "Santana"
cliente3.email = "info@pacheco.com"
cliente3.direccion = "la calle de Pacheco"
        
# Demuestra que los métodos set y get funcionan para cada una de las instancias
print(cliente1.getDireccion()) 
print(cliente1.getEmail()) 

print(cliente2.getDireccion()) 
print(cliente2.getEmail()) 

print(cliente3.getDireccion()) 
print(cliente3.getEmail()) 
