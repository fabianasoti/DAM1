'''
Adivina el número
v0.1 Fabiana Victoria Sotillo
Programa que genera un número secreto entre 1 y 50 y permite al usuario
adivinarlo en un máximo de 6 intentos, validando entradas y mostrando pistas.
'''

import random

# Generar número secreto
secreto = random.randint(1, 50)
assert 1 <= secreto <= 50, "El número secreto debe estar entre 1 y 50."
print(secreto)
intentos = 6
intentos_usados = 0

print("Adivina el número")
print("Tienes 6 intentos para adivinar el número secreto entre 1 y 50.")

while True:
    try:
        numero = input("Ingresa un número: ")
        numero = int(numero)

    except:
        print("Error: Debes escribir un número entero.")
        continue  # No gasta intento

    # Validar rango
    if numero < 1 or numero > 50:
        print("El número debe estar entre 1 y 50.")
        continue  # No gasta intento

    # Aumentar contador de intentos válidos
    intentos -= 1
    print("Te quedan", intentos, "intentos.") 
    assert intentos_usados >= 0, "El contador de intentos no puede ser negativo."

    # Comparar con el secreto
    if numero == secreto:
        print("Adivinaste el número", secreto, "en,", 6 - intentos, "intentos.")
        break
    elif numero < secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")

    # Pista en el tercer intento
    if intentos == 3:
        if secreto % 2 == 0:
            print("Pista: el número secreto es PAR.")
        else:
            print("Pista: el número secreto es IMPAR.")
    if intentos == 0:
        print("No lograste adivinarlo. El número era", secreto)
        break
