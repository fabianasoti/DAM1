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




#######################
# Definición de variables
litros_leche = 0.3          # litros disponibles
temporizador_maximo = 15    # tiempo máximo permitido

# Control de excepciones
try:
    # Verificar si hay suficiente leche
    if litros_leche < 0.5:
        # Provocar un error manualmente dividiendo por cero (solo para activar el except)
        1 / 0
    # Verificar si el temporizador está fuera del rango permitido
    if temporizador_maximo > 20:
        1 / 0
    
    print("Preparando café... ☕")

except:
    if litros_leche < 0.5:
        print("⚠️ No hay suficiente leche.")
    elif temporizador_maximo > 20:
        print("⚠️ El temporizador está fuera del límite.")

# Continuidad del programa
print("El programa sigue funcionando. ✅")

