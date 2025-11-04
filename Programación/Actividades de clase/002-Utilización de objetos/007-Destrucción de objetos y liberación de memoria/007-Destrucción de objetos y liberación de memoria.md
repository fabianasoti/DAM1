```
''' 
    Calculadora de cuadras
    v0.1 2025 Fabiana Victoria Sotillo
    Programa que calcula número de cuadras a partir de los caballos
'''
```

---
En programación, el uso de métodos predefinidos permite realizar cálculos de manera eficiente sin necesidad de crear funciones o clases adicionales. En este ejercicio se utiliza el módulo math para resolver un problema práctico: determinar cuántas cuadras se necesitan para alojar un número determinado de caballos, considerando cuántos caben por cuadra. A través de operaciones básicas de división y el uso del método ceil() para redondear hacia arriba, se demuestra cómo los objetos y métodos preexistentes del lenguaje pueden aplicarse a situaciones cotidianas mediante la automatización de cálculos simples.

- Para el desarrollo de este programa se inicia importando el módulo math con el alias matematicas.
```
import math as matematicas
```

- Se definen las variables de inicio con las que se trabajarán en el código:
```
caballos = 0
cuadras = 0
caballos_por_cuadra = 0
```

- A continuación, se solicita al usuario los datos necesarios: el número de caballos y la cantidad de caballos que pueden ocupar una cuadra.
```
caballos_por_cuadra = int(input("Introduce el número de caballos por cuadra: "))
caballos = int(input("Introduce el número de caballos: "))
```

- Luego, se realiza la división entre ambos valores para obtener un número que representa las cuadras necesarias. Sin embargo, como el resultado puede ser decimal, se emplea el método ceil() del módulo math para redondear el resultado al número entero superior, garantizando que haya espacio suficiente para todos los caballos.
```
cuadras = caballos / caballos_por_cuadra
redondeoalza = matematicas.ceil(cuadras)
```

- Finalmente, se muestra el resultado al usuario mediante sentencias print(), estructurando la salida en mensajes claros y explicativos.
```
print("Si tienes", caballos, "caballos")
print("Y te caben", caballos_por_cuadra, "caballos por cuadra")
print("En ese caso necesitas", redondeoalza, "cuadras")
```

---
A continuación se ilustra el código funcional completo:
```
''' 
Calculadora de cuadras
v0.1 2025 Fabiana Victoria Sotillo
Programa que calcula número de cuadras a partir de los caballos
'''

import math as matematicas

# Datos de inicio
caballos = 0
cuadras = 0
caballos_por_cuadra = 0

# Entrada de información
caballos_por_cuadra = int(input("Introduce el número de caballos por cuadra: "))
caballos = int(input("Introduce el número de caballos: "))

# Realización de cálculos
cuadras = caballos / caballos_por_cuadra
redondeoalza = matematicas.ceil(cuadras)

# Salida de resultados
print("Si tienes", caballos, "caballos")
print("Y te caben", caballos_por_cuadra, "caballos por cuadra")
print("En ese caso necesitas", redondeoalza, "cuadras")
```

---
Este ejercicio permitió aplicar los conceptos de operaciones matemáticas básicas y el uso de métodos predefinidos en Python. El empleo del método ceil() del módulo math fue clave para redondear los resultados de manera lógica y práctica. Además de fortalecer la comprensión de la entrada y salida de datos mediante input() y print(), la actividad demuestra cómo los cálculos automatizados pueden emplearse para resolver situaciones reales, desarrollando habilidades esenciales para la programación.