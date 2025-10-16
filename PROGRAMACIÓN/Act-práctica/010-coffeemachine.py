# Definición de variables
litros_leche = 0.3        # litros disponibles
temporizador_maximo = 20    # tiempo máximo permitido

# Control de excepciones
try:
    # Verificar condiciones normales
    litros_leche >= 0.5
    print("Cantidad de leche adecuada")
except:
    litros_leche < 0.5
    print("No hay suficiente leche.")

try:
    temporizador_maximo <= 20
    print("Tiempo de preparación adecuada")
except:
    temporizador_maximo > 20
    print("El temporizador está fuera del rango permitido.")

# Continuidad del programa
print("El programa sigue funcionando.")
