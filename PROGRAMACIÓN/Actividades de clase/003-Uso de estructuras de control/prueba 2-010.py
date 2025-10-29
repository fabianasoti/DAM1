'''
Gestión de errores en arte latte
v0.1 Fabiana Victoria Sotillo
Este programa me ayuda a detectar y manejar errores comunes,
como la falta de leche o un temporizador fuera del rango permitido en una máquina de café.
'''

"""
🎨 Programa: Gestión de errores en arte latte

Contexto:
Soy una artista latte y mi máquina de café a veces presenta fallos.
Este programa me ayuda a detectar y manejar errores comunes,
como la falta de leche o un temporizador fuera del rango permitido.
El objetivo es aplicar el uso de try/except para controlar estos errores
sin interrumpir la ejecución del programa.
"""

# Definición de variables
litros_leche = 0.3        # litros disponibles
temporizador_maximo = 20  # tiempo máximo permitido

print("☕ Iniciando preparación de arte latte...")

# Control de excepciones
try:
    # Verificar si hay suficiente leche
    if litros_leche < 0.5:
        resultado = 1 / 0   # Forzamos un error para activar el except
    print("Cantidad de leche adecuada.")
except:
    print("⚠️ No hay suficiente leche para preparar el café.")

try:
    # Verificar si el temporizador está dentro del rango permitido
    if temporizador_maximo > 10:
        resultado = 1 / 0   # Forzamos un error para activar el except
    print("Tiempo de preparación adecuado.")
except:
    print("⚠️ El temporizador está fuera del rango permitido.")

# Continuidad del programa
print("\nEl programa sigue funcionando correctamente ☕")
print("Gracias por usar el sistema de control de errores de tu máquina latte.")

"""
🧩 Conclusión:
Este ejercicio demuestra cómo el uso del bloque try/except
permite manejar errores sin detener por completo el programa.
En este caso, se controlan dos posibles fallos en la máquina:
la falta de leche y un temporizador fuera del rango permitido.
Así, la artista latte puede detectar los problemas y continuar trabajando
sin interrumpir su proceso creativo.
"""
