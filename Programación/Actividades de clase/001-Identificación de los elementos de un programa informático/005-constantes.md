Este ejercicio tiene como objetivo demostrar los conocimientos adquiridos sobre constantes y funciones en Python.
Para ello se realizarán tres pequeños programas donde:

- Se definen variables
- Se definen constantes en el caso aplicable.
- Se declaran funciones.
- Se muestran en pantalla sus salidas.


- Para ilustrar el primer ejemplo de programa, se muestra a continuación el cálculo del área de un círculo, usando la fórmula de "Área de un círculo = PI * radio ** 2", estableciendo la constante PI.
```
'''
Programa de cálculo del área de un círculo
(c) 2025 Fabiana Sotillo
Este programa calcula el área de un círculo usando la constante PI

'''
#Declaro constante PI
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
Aquí se puede demostrar el uso de una constante dentro de la resolución de una fórmula matemática.

- En el segundo ejemplo de programa, se tiene la aplicación práctica en el contexto de un videojuego, LoL, en el que se define una función que le restas vidas a la variable "vidas" a un personaje de un videojuego.
```
'''
Programa que resta vidas
(c) 2025 Fabiana Sotillo
Este programa crea una función que resta vidas a un personaje d eun videojuego
'''
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
De esta manera se ha ilustrado la implementación de una función aplicada al mundo de los videojuegos, y cómo hacer que cambie el resultado de la variable vidas a medida que el personaje recibe daño, con la función recibirDanyo.

- E
