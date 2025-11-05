En Python, los objetos poseen propiedades que almacenan información y métodos que permiten realizar acciones. Muchos de estos objetos ya vienen definidos en el propio lenguaje o en sus bibliotecas estándar, como math, que contiene funciones y valores matemáticos útiles.

En este ejercicio se emplea la propiedad pi del módulo math para acceder al valor del número π y mostrarlo en pantalla, reforzando la comprensión del uso de propiedades en objetos predefinidos y su aplicación en cálculos matemáticos.

---
- Para resolver este ejercicio, se comienza importando la biblioteca math con el alias matematicas
```
import math as matematicas. 
```

- Luego, se accede a la propiedad pi del objeto matematicas y se almacena su valor en una variable llamada numero_pi. 
```
numero_pi = matematicas.pi
```

- Finalmente, se utiliza la función print() para mostrar el valor en pantalla.
```
print(numero_pi)
```

---
A continuación se ilustra el código funcional completo:
```
# Importamos la biblioteca math con un alias
import math as matematicas

# Accedemos a la propiedad pi del objeto matematicas
numero_pi = matematicas.pi

# Imprimimos el valor de la propiedad
print(numero_pi)
```

---
Este proceso ilustra la manera en que Python permite acceder a las propiedades de objetos predefinidos sin necesidad de crear nuevas clases o métodos, en particular al acceder al valor de pi desde la biblioteca math. La práctica refuerza la importancia de conocer las herramientas que el lenguaje ofrece de forma nativa, permitiendo escribir programas más eficientes y consistentes.

Además, este tipo de ejercicios ayuda a consolidar la relación entre teoría y práctica, mostrando cómo el acceso a propiedades forma parte esencial del paradigma orientado a objetos y cómo estas pueden ser aplicadas en cálculos matemáticos, simulaciones y otros ámbitos más complejos de la programación.