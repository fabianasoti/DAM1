'''
Batalla de dragones
v0.1 Fabiana Sotillo
Programa que ejemplifica una batalla entre dragones,
donde se les clasifica según su edad, fuerza y resistencia.
'''

# Entrada de datos con try-except
try:
    nombre_dragon_a = input("Dime el nombre del dragón A: ")
    edad_dragon_a = int(input("Dime la edad del dragón A: "))

    nombre_dragon_b = input("Dime el nombre del dragón B: ")
    edad_dragon_b = int(input("Dime la edad del dragón B: "))

except:
    print("Error: por favor, introduce un número válido para la edad.")
    exit()

# Clasificación de los dragones
# Menores de 50 años es Joven
if edad_dragon_a < 50:
    clasificacion_dragon_a = "Joven"
# Entre 50 y 199 años es Adulto
elif 50 <= edad_dragon_a <= 199:
    clasificacion_dragon_a = "Adulto"
# El resto, mayores de 199 años → Anciano
else:
    clasificacion_dragon_a = "Anciano"

if edad_dragon_b < 50:
    clasificacion_dragon_b = "Joven"
elif 50 <= edad_dragon_b <= 199:
    clasificacion_dragon_b = "Adulto"
else:
    clasificacion_dragon_b = "Anciano"

# Entrenamiento de los dragones
fuerza_dragon_a = 0
fuerza_dragon_b = 0

for dia in range(1, 4):
    print("Día", dia, "de entrenamiento para", nombre_dragon_a)
    if clasificacion_dragon_a == "Joven":
        fuerza_ganada = 2
    elif clasificacion_dragon_a == "Adulto":
        fuerza_ganada = 1
    else:
        fuerza_ganada = 1
    fuerza_dragon_a += fuerza_ganada
    print(nombre_dragon_a, "ganó", fuerza_ganada, "puntos de fuerza. Fuerza total:", fuerza_dragon_a)

for dia in range(1, 4):
    print("Día", dia, "de entrenamiento para", nombre_dragon_b)
    if clasificacion_dragon_b == "Joven":
        fuerza_ganada = 2
    elif clasificacion_dragon_b == "Adulto":
        fuerza_ganada = 1
    else:
        fuerza_ganada = 1
    fuerza_dragon_b += fuerza_ganada
    print(nombre_dragon_b, "ganó", fuerza_ganada, "puntos de fuerza. Fuerza total:", fuerza_dragon_b)

resistencia_dragon_a = edad_dragon_a
resistencia_dragon_b = edad_dragon_b

# Resultados finales
print("\nResultados finales:")
print(nombre_dragon_a, ":", clasificacion_dragon_a, ", Fuerza:", fuerza_dragon_a, ", Resistencia:", resistencia_dragon_a)
print(nombre_dragon_b, ":", clasificacion_dragon_b, ", Fuerza:", fuerza_dragon_b, ", Resistencia:", resistencia_dragon_b)
