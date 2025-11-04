'''
Métodos estáticos
2025 Fabiana Victoria Sotillo
Programa que crea un método estático dentro de una clase
'''

# Importamos la biblioteca math para utilizar su método estático ceil()
import math

# Definimos la clase Café con un método estático
class Café:
    @staticmethod
    def calcularLeche(tamanyo):
        # Calcula el 50% del tamaño de la taza como cantidad de leche
        leche_necesaria = tamanyo * 0.5
        # Redondea el resultado hacia arriba
        return math.ceil(leche_necesaria)

# Tamaño de la taza en mililitros
tamanyo_taza = 240

# Llamada al método estático directamente desde la clase
leche = Café.calcularLeche(tamanyo_taza)

# Muestra el resultado
print("Cantidad de leche necesaria: ", leche, "ml")