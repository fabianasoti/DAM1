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
