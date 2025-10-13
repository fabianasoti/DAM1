```
#Declaro constante PI######################
PI = 3.1415
#Muestro PI en pantalla 
print("El valor de PI es", PI)

#Declaro valor de radio
radio = 3
#Calculo el área del círculo
area_circulo = PI * radio ** 2
#Imprimo el área del círculo
print("El área del círculo es", area_circulo)
```

```
#Aplicación práctica LoL y personaje con número de vidas#########
#Declaro variable vidas
vidas = 10
#Defino función que reste 1 de vida a vidas
def recibirDanyo(vidas):
    vidas -= 1
    return vidas

#Llamo a la función varias veces
#Se imprime el número de vidas restante
print("Quedan", recibirDanyo(vidas), "vidas")
vidas = recibirDanyo(vidas)
print("Quedan", recibirDanyo(vidas), "vidas")
vidas = recibirDanyo(vidas)
print("Quedan", recibirDanyo(vidas), "vidas")
vidas = recibirDanyo(vidas)
print("Quedan", recibirDanyo(vidas), "vidas")
```

```
#Arte Latte###############
#Declarar variables
#Declaro la constante COLOR_MARRON con su valor hexadecimal
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
```


