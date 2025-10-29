'''
Gestión de errores en arte latte
v0.1 Fabiana Victoria Sotillo
Este programa me ayuda a detectar y manejar errores comunes,
como la falta de leche o un temporizador fuera del rango permitido en una máquina de café.
'''

# Definición de variables
litros_leche = 0.3        # litros disponibles
temporizador_maximo = 20  # tiempo máximo permitido

# Control de excepciones
try:
    # Se verifica si hay suficiente leche
    if litros_leche < 0.5:
        resultado = 1 / 0   # Se fuerza un error para activar el except
    print("Cantidad de leche adecuada.")
except:
    print("No hay suficiente leche para preparar el café.")

try:
    # Se verifica si el temporizador está dentro del rango permitido
    if temporizador_maximo > 10:
        resultado = 1 / 0   # Se fuerza un error para activar el except
    print("Tiempo de preparación adecuado.")
except:
    print("El temporizador está fuera del rango permitido.")

# Continuidad del programa
print("El programa sigue funcionando correctamente")

'''
Este ejercicio demuestra cómo el uso del bloque try/except
permite detectar errores sin detener el programa.
En este caso, se controlan dos posibles fallos en la máquina:
la falta de leche y un temporizador fuera del rango permitido.
Así, el usuario de la máquina de café puede detectar los problemas y solucionarlos.
'''
