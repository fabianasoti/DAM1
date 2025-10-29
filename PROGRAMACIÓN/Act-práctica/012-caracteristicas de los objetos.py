"""
Programa que utiliza objetos
v0.1 Fabiana Sotillo
Este programa realiza tres cálculos:
1. Altura de un cilindro dado su volumen y radio.
2. Probabilidad de obtener dos veces la misma cara al lanzar un dado.
3. Área de una taza asumida como un círculo.
"""

import math

#### Calcular la altura de un cilindro

volumen_cilindro = 50  # Ejemplo de volumen en cm³
radio_cilindro = 3    # Ejemplo de radio en cm

# Fórmula del volumen del cilindro: V = π * r² * h
# Despejando la altura: h = V / (π * r²)
altura_cilindro = volumen_cilindro / (math.pi * radio_cilindro**2)

print("La altura del cilindro es:", altura_cilindro)


#### Calcular la probabilidad de obtener dos veces la misma cara de un dado

numero_caras_dado = 6

# Al lanzar un dado justo, la probabilidad de obtener una cara específica es: 1/n
# Al querer repetir la misma cara dos veces seguidas: (1/n) * (1/n) = 1/n²
probabilidad_par = (1 / numero_caras_dado) * (1 / numero_caras_dado)

print("La probabilidad de obtener dos veces la misma cara del dado es:", probabilidad_par)


#### Calcular el área de una taza

radio_taza = 5  # Ejemplo de radio en cm

# Se asume la parte superior de la taza como un círculo
# Fórmula del área del círculo: A = π * r²
area_taza = math.pi * radio_taza**2

print("El área de la taza es:", area_taza)

