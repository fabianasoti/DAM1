```
'''
Evaluación de final de unidad - Desarrollo de clases
2025 Fabiana Victoria Sotillo
Programa que crea clase, define constructor, crea instancias y hace uso del método set y get
'''
```

---
En la programación orientada a objetos, existen conceptos fundamentales: clases, objetos, atributos, métodos y constructores. 

Una clase permite crear tipos de objetos con características y comportamientos específicos, mientras que un objeto representa una instancia concreta de esa clase. 

Los atributos o propiedades almacenan la información asociada a cada objeto, y los métodos son las funciones que determinan las acciones que este puede realizar. 

El constructor (__init__) es un método especial que se ejecuta al crear un objeto, permitiendo definir sus atributos y garantizar su correcto funcionamiento desde el inicio.

Los métodos get y set en Python se utilizan para controlar el acceso a los atributos de una clase. Los métodos get (obtener) devuelven el valor de un atributo, mientras que los métodos set (establecer) permiten modificar o asignar un nuevo valor.

El propósito del ejercicio es demostrar cómo se pueden encapsular datos y manipular propiedades de un objeto de forma controlada, garantizando una estructura organizada y reutilizable del código. Además, se crean tres instancias independientes de la clase para comprobar el funcionamiento de los métodos y validar el correcto manejo de la información de cada cliente.

A través de esta práctica, se busca comprender cómo crear clases de manera íntegra y estructurada.

---
Para ello, se explica el paso a paso de la construcción del código:

- Se crea una clase Cliente.
```
class Cliente(): 
```

- Se crea un constructor con parámetros (nombre, apellidos etc en la instanciación del objeto)
```
def _init_(self,nombre,apellido,email,direccion):
```

- Se añaden propiedades (nombre, apellidos, email, etc)
```
def _init_(self,nombre,apellido,email,direccion):
	self.nombre = ""
	self.apellido = ""
	self.email = "" 
	self.direccion = ""
```

- Se crea al menos un metodo set y un metodo get para una de las propiedades
```
def setDireccion(self, nuevadireccion):
	self.direccion = nuevadireccion
def getDireccion(self):
	return self.direccion

def setEmail(self, nuevoemail):
	self.email = nuevoemail
def getEmail(self):
	return self.email
```

- Una vez creada la clase, se crean tres instancias de la clase, cada una de ellas con sus propias propiedades
```
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
```

- Se demuestra que los métodos set y get funcionan para cada una de las instancias
```
print(cliente1.getDireccion()) 
print(cliente1.getEmail()) 

print(cliente2.getDireccion()) 
print(cliente2.getEmail()) 

print(cliente3.getDireccion()) 
print(cliente3.getEmail()) 
```

---
A continuación, se ilustra el código completo:
```
'''
Evaluación de final de unidad - Desarrollo de clases
2025 Fabiana Victoria Sotillo
Programa que crea clase, define constructor, crea instancias y hace uso del método set y get
'''

# Crea una clase Cliente
class Cliente(): 
	# Se añaden propiedades (nombre, apellidos, email, etc)
	# Se crea un constructor con parámetros (nombre, apellidos etc en la instanciación del objeto)
	def _init_(self,nombre,apellido,email,direccion):
		self.nombre = ""
		self.apellido = ""
		self.email = "" 
		self.direccion = ""
	
	def setDireccion(self, nuevadireccion):
		# Se crea al menos un metodo set y un metodo get para una de las propiedades
		self.direccion = nuevadireccion
	def setEmail(self, nuevoemail):
		self.email = nuevoemail
    
	def getDireccion(self):
		return self.direccion
	def getEmail(self):
		return self.email
      
# Una vez creada la clase, se crean tres instancias de la clase, cada una de ellas con sus propias propiedades
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
        
# Se demuestra que los métodos set y get funcionan para cada una de las instancias
print(cliente1.getDireccion()) 
print(cliente1.getEmail()) 

print(cliente2.getDireccion()) 
print(cliente2.getEmail()) 

print(cliente3.getDireccion()) 
print(cliente3.getEmail()) 
```

---
A través de este ejercicio se expresa la importancia de los constructores y los métodos de acceso (set y get) dentro de la programación orientada a objetos.

La clase Cliente permitió representar entidades con atributos propios y modificar sus valores mediante métodos,

Finalmente, el programa se ejecuta de manera correcta, junto con la creación de múltiples instancias, y se evidencia la capacidad de aplicar los principios básicos de la creación de clases de manera práctica y estructurada.
