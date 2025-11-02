La programación orientada a objetos (POO) es una forma de organizar el código basada en ideas del mundo real. En POO, una clase funciona como un plano que define qué características y acciones tendrán los objetos creados a partir de ella. Por ejemplo, podríamos tener una clase llamada Café, que incluya atributos como intensidad y temperatura, y métodos como servir() o mezclar(). A partir de esa plantilla, se pueden crear objetos concretos: un espresso, un capuchino o un latte, cada uno con sus propias características, pero todos pertenecen a la clase Café.

En programación es muy importante aprender a utilizar los objetos predeterminados que ya existen en el lenguaje, porque están probados, optimizados y listos para ser reutilizados. Esto nos evita reescribir código complejo y nos ayuda a programar de forma más eficiente y correcta.

En este ejercicio utilizamos el objeto predeterminado math, que contiene herramientas matemáticas avanzadas. Gracias a él, podemos usar el objeto pi ya definido y reutilizarlo para realizar cálculos de geometría de manera precisa, como el área de la parte superior de una taza o la altura de un cilindro a partir de su volumen. Estos conceptos se aplicarán en los cálculos que se mostrarán a continuación, relacionados con situaciones reales como preparaciones de café o el azar en juegos.

Para ello:

- Se importa math
```
import math
```

- Se definen los valores para hacer el primer cálculo:
```
#### Calcular la altura de un cilindro

volumen_cilindro = 50  # Ejemplo de volumen en cm³
radio_cilindro = 3    # Ejemplo de radio en cm
```

- Se insta el objeto pi predefinido en math dentro de la fórmula matemática:
```
math.pi
```

- Gracias a la librería math se puede hacer uso de fórmulas matemáticas, entonces se expresan para resolver el cálculo requerido:
```
# Fórmula del volumen del cilindro: V = π * r² * h
# Despejando la altura: h = V / (π * r²)
altura_cilindro = volumen_cilindro / (math.pi * radio_cilindro**2)
```

- Se muestra en pantalla el resultado de lo calculado.
```
print("La altura del cilindro es:", altura_cilindro)
```

A continuación se muestra el bloque de código entero:
```
"""
Programa que utiliza objetos
v0.1 Fabiana Sotillo
Este programa realiza tres cálculos:
1. Altura de un cilindro dado su volumen y radio.
2. Probabilidad de obtener dos veces la misma cara al lanzar un dado.
3. Área de una taza asumida como un círculo.
"""

import math

#### Calcular la altura de un cilindro

volumen_cilindro = 50  # Ejemplo de volumen en cm³
radio_cilindro = 3    # Ejemplo de radio en cm

# Fórmula del volumen del cilindro: V = π * r² * h
# Despejando la altura: h = V / (π * r²)
altura_cilindro = volumen_cilindro / (math.pi * radio_cilindro**2)

print("La altura del cilindro es:", altura_cilindro)


#### Calcular la probabilidad de obtener dos veces la misma cara de un dado

numero_caras_dado = 6

# Al lanzar un dado justo, la probabilidad de obtener una cara específica es: 1/n
# Al querer repetir la misma cara dos veces seguidas: (1/n) * (1/n) = 1/n²
probabilidad_par = (1 / numero_caras_dado) * (1 / numero_caras_dado)

print("La probabilidad de obtener dos veces la misma cara del dado es:", probabilidad_par)


#### Calcular el área de una taza

radio_taza = 5  # Ejemplo de radio en cm

# Se asume la parte superior de la taza como un círculo
# Fórmula del área del círculo: A = π * r²
area_taza = math.pi * radio_taza**2

print("El área de la taza es:", area_taza)
```

El aprendizaje del uso de objetos en programación es fundamental porque nos permite aprovechar herramientas ya creadas, optimizadas y probadas, evitando así tener que desarrollar soluciones complejas desde cero. Gracias a módulos como math, podemos utilizar objetos matemáticos como pi sin necesidad de definirlo manualmente, lo que garantiza precisión en los cálculos y ahorra tiempo en el desarrollo del código. Esto mejora la eficiencia de nuestros programas y nos permite enfocarnos en resolver problemas reales con mayor claridad, manteniendo un código más limpio, confiable y fácil de mantener.
