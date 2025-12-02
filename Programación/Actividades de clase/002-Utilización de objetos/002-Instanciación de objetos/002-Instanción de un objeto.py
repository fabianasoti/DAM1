import math

# Cálculo del volumen de una taza de café con forma cónica
radio_taza = 5  # en centímetros
altura_taza = 10  # en centímetros

volumen_cafe = (1/3) * math.pi * radio_taza**2 * altura_taza
print("El volumen de la taza es:", volumen_cafe, "cm³")

# Cálculo del área de la base de la taza
area_base_cafe = math.pi * radio_taza**2
print("El área de la base de la taza es: ", area_base_cafe, "cm²")

# Cálculo del volumen de leche restante en un latte artístico
volumen_total = 150  # en ml
volumen_figuras = 30  # en ml

volumen_leche = volumen_total - volumen_figuras
print("El volumen de leche para el latte artístico es: ", volumen_leche, "ml")