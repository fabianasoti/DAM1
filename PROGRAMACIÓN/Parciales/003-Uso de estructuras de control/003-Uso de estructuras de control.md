El objetivo de este ejercicio es desarrollar un programa en Python que genere un número secreto aleatorio entre 1 y 50 y permita al usuario adivinarlo en un máximo de 6 intentos, incorporando validación de entradas y pistas que faciliten el juego.

Los conceptos técnicos aplicados en este programa son:

Variables, condicionales (if/elif/else), bucles (while True), entrada de datos (input) y conversión (int), manejo de errores (try/except), operador módulo (%).

El programa sigue los siguientes pasos principales:

Importa el módulo random para generar numeros aleatorios:
```
import random
```

Se genera un número secreto aleatorio entre 1 y 50.
```
secreto = random.randint(1, 50)
assert 1 <= secreto <= 50, "El número secreto debe estar entre 1 y 50."
print(secreto)
intentos = 6
intentos_usados = 0
```

Solicita al usuario que ingrese un número, validando que sea un entero dentro del rango permitido.
```
    try:
        numero = input("Ingresa un número: ")
        numero = int(numero)

    except:
        print("Error: Debes escribir un número entero.")
        continue  # No gasta intento
```

Después del tercer intento, si aún no se acierta, proporciona una pista de paridad.
```
if intentos == 3:
        if secreto % 2 == 0:
            print("Pista: el número secreto es PAR.")
        else:
            print("Pista: el número secreto es IMPAR.")
```

Termina cuando el usuario acierta el número o se agotan los intentos.
```
 if intentos == 0:
        print("No lograste adivinarlo. El número era", secreto)
        break
```

A continuación, el bloque de código entero: 

```
'''
Adivina el número
v0.1 Fabiana Victoria Sotillo
Programa que genera un número secreto entre 1 y 50 y permite al usuario
adivinarlo en un máximo de 6 intentos, validando entradas y mostrando pistas.
'''

import random

# se genera número secreto
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
```
		
Este ejercicio permitió aplicar y reforzar los siguientes conceptos de programación:
- Variables y contadores para controlar los intentos y el número secreto.
- Condicionales y operadores (if/elif/else y %) para comparar valores y mostrar pistas.
- Bucles repetitivos (while) para iterar hasta cumplir condiciones de finalización.
- Manejo de errores (try/except) para garantizar que el programa no falle ante entradas inválidas.

La práctica demuestra cómo estructurar un juego sencillo en Python, con interacción del usuario y lógica condicional, preparando la base para desarrollar programas más complejos que incluyan menús, puntuaciones y niveles de dificultad.
