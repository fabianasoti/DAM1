Este ejercicio tiene como objetivo demostrar los conocimientos adquiridos sobre constantes y funciones en Python.
Para ello se realizarán tres pequeños programas donde:

- Se definen variables
- Se definen constantes en el caso aplicable.
- Se declaran funciones.
- Se muestran en pantalla sus salidas.


- Para ilustrar el primer ejemplo de programa, se muestra a continuación el cálculo del área de un círculo, usando la fórmula de "Área de un círculo = PI * radio ** 2", estableciendo la constante PI, utilizada en trigonometría, para realizar cálculos la circunferencia y el área de círculos, y también en física, ingeniería, astronomía, estadística, y tecnología, donde es fundamental para entender fenómenos como ondas.
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


- En el tercer ejemplo de programa, el código define un color marrón y una función para "dibujar" un patrón de arte latte (dibujos hechos con espuma de leche en café), que simplemente imprime en pantalla qué patrón se está dibujando y con qué color. Luego llama a esa función con distintos patrones.

Se tiene este programa como ejemplo:
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
dibujarPatron("alcachofa")
```
El código anterior, muestra cómo se puede usar una función para manejar diferentes valores de patrones y un color constante, facilitando la reutilización del código.

Con esto se puede concluir que el uso de funciones es sumamnete útil a la hora de mantener un código, ya que reduce la redundancia y además se puede reutilizar en distintos apartados. 

En el caso del arte latte, ya que son procedimientos repetitivos como emulsionar la leche, realizar un espresso o calibrar la máquina, podrían realizarse funciones que engloben estas acciones y repetirlas en distintas preparaciones de café o diseños de arte latte. 

En Lol, y en el mundo de los videojuegos, hay acciones repetitivas, que pueden ser reutilizadas en distintos personajes y contextos, como perder puntuación de vidas en el personaje, o ganar maná o resistencia mágica/física. En estos casos, el uso de funciones estaría bastante justificado para que se activen bajo ciertos criterios en el juego y así no tener que reescribirlo cada vez.

