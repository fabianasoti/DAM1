#Arte Latte###############
#Declarar variables
#Declaro la variable COLOR_MARRON con su valor hexadecimal
COLOR_MARRON = "#562B05" #en hexadecimal
#Declarar la variable patron con un valor inicial
patron = "espuma"

#Definir función dibujarPatron
#Que imprima el patrón de arte latte
#Usando la variable patron
def dibujarPatron(patron):
    print("Dibujando patrón de arte latte con: ", patron, "y color", COLOR_MARRON)

# Llamar a la función varias veces con diferentes patrones
dibujarPatron(patron)
dibujarPatron("hoja")
dibujarPatron("corazón")
dibujarPatron("estrella")
