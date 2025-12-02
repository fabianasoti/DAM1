```
''' 
Clase Matematicas
2025 Fabiana Victoria Sotillo
Programa que implementa una clase con métodos para realizar operaciones matemáticas
'''
```

---
En este ejercicio se desarrolla una clase llamada Matematicas, cuyo propósito es aplicar los principios de la programación orientada a objetos (POO) para resolver operaciones numéricas básicas sin recurrir a librerías externas. 

En POO, una clase es una plantilla que permite crear objetos con características y comportamientos definidos; el constructor ```__init__``` es un método especial que inicializa los atributos de cada objeto al crearse; y los métodos son funciones internas que describen las acciones que un objeto puede realizar. 

A través de estos conceptos, se busca reforzar la comprensión de la estructura de una clase en Python y aprender cómo implementar funciones matemáticas, construyendo métodos propios de manera lógica y manual.

---
Para desarrollar el código se realizaron los siguientes pasos:

- Se define la clase Matematicas, definiendo una constante PI  como uno de sus atributos, siendo esto posible gracias al método constructor ```__init__```, de esta manera, la constante PI queda disponible para todas las instancias.
```
class Matematicas:
    def __init__(self):
        # Inicialización de la constante PI
        self.PI = 3.14159265359
```

- Se construyen tres métodos principales que permiten realizar operaciones numéricas básicas. Los métodos implementados son:

	- redondeo(self, numero): redondea el número al entero más cercano según el valor decimal (menor de 0.5 redondea hacia abajo, igual o mayor redondea hacia arriba).
	```
			def redondeo(self, numero):
				# Redondea al entero más cercano según la parte decimal
				parte_entera = int(numero)
				decimal = numero - parte_entera
				if decimal < 0.5:
						return parte_entera
				else:
						return parte_entera + 1
	```

	- techo(self, numero): devuelve el entero inmediato superior.
	```
		def techo(self, numero):
			# Devuelve el entero inmediato superior si no es exacto
			parte_entera = int(numero)
			if numero > parte_entera:
					return parte_entera + 1
			else:
					return parte_entera
	```

	- suelo(self, numero): devuelve el entero inmediato inferior.
	```
	def suelo(self, numero):
		# Devuelve el entero inmediato inferior si no es exacto
		parte_entera = int(numero)
		if numero < parte_entera:
				return parte_entera - 1
		else:
				return parte_entera
	```

- Finalmente, se crea una instancia de la clase y se prueban los métodos con diferentes valores, observando los resultados esperados.
```
operaciones = Matematicas()

print("Redondeo de 3.2:", operaciones.redondeo(3.2))   # Resultado: 3
print("Redondeo de 5.8:", operaciones.redondeo(5.8))   # Resultado: 6
print("Techo de 4.1:", operaciones.techo(4.1))         # Resultado: 5
print("Suelo de 7.9:", operaciones.suelo(7.9))         # Resultado: 7
print("Valor de PI:", operaciones.PI)                   # Resultado: 3.14159265359
```

---
A continuación se muestra el código funcional completo:
```
''' 
Clase Matematicas
2025 Fabiana Victoria Sotillo
Programa que implementa una clase con métodos para realizar operaciones matemáticas
'''

class Matematicas:
    def __init__(self):
        # Inicialización de la constante PI
        self.PI = 3.14159265359

    def redondeo(self, numero):
        # Redondea al entero más cercano según la parte decimal
        parte_entera = int(numero)
        decimal = numero - parte_entera
        if decimal < 0.5:
            return parte_entera
        else:
            return parte_entera + 1

    def techo(self, numero):
        # Devuelve el entero inmediato superior si no es exacto
        parte_entera = int(numero)
        if numero > parte_entera:
            return parte_entera + 1
        else:
            return parte_entera

    def suelo(self, numero):
        # Devuelve el entero inmediato inferior si no es exacto
        parte_entera = int(numero)
        if numero < parte_entera:
            return parte_entera - 1
        else:
            return parte_entera

# Creación de una instancia de la clase
operaciones = Matematicas()

# Se realizan pruebas
print("Redondeo de 3.2:", operaciones.redondeo(3.2))   # Resultado: 3
print("Redondeo de 5.8:", operaciones.redondeo(5.8))   # Resultado: 6
print("Techo de 4.1:", operaciones.techo(4.1))         # Resultado: 5
print("Suelo de 7.9:", operaciones.suelo(7.9))         # Resultado: 7
print("Valor de PI:", operaciones.PI)                   # Resultado: 3.14159265359
```

---
Este ejercicio permitió aplicar los fundamentos de la programación orientada a objetos mediante la creación de métodos matemáticos personalizados, fortaleciendo el uso de constructores, atributos y métodos. La implementación manual de las funciones de redondeo, techo y suelo desarrolló el pensamiento algorítmico y demostró cómo la programación puede aplicarse a situaciones prácticas, como cálculos de diseño o medidas precisas en actividades creativas.
