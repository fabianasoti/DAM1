'''
Actividad de final de unidad - Desarrollo de clases
2025 Fabiana Victoria Sotillo

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
# Crea al menos un metodo set y un metodo get para una de las propiedades
		def setNombreCompleto(self, nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self, nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
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
cliente2.apellido = "García"
cliente2.email = "info@cliente2.com"
cliente2.direccion = "la calle del cliente 2"

cliente3 = Cliente()
cliente3.nombre = "Pacheco"
cliente3.apellido = "Santana"
cliente3.email = "info@cliente3.com"
cliente3.direccion = "la calle del cliente 3"
      

        
# Demuestra que los métodos set y get funcionan para cada una de las instancias
