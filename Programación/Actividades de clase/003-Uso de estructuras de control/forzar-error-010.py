# Definición de variables
litros_leche = input("Cuántos litros de leche tiene la máquina?: ")          # litros disponibles
litros_leche = float(litros_leche)

temporizador_maximo = int(20)    # tiempo máximo permitido
temporizador = input("Cuánto tiempo se está demorando la máquina?: ")
temporizador = int(temporizador)

# Control de excepciones
try:
    # Verificar si hay suficiente leche
    litros_leche /0
    print(1 / 0)    # Provocar un error manualmente dividiendo por cero (solo para activar el except)
    
    print("Preparando café...")

except:
    litros_leche < 0.5
    print("No hay suficiente leche.")

try:
    temporizador /0
    print(1 / 0)
except:
    temporizador_maximo > 20
    print("El temporizador está fuera del límite.")
# Continuidad del programa
print("El programa sigue funcionando.")
