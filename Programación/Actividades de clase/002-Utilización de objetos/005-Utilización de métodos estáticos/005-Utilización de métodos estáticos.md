```
'''
Métodos estáticos
2025 Fabiana Victoria Sotillo
Programa que crea un método estático dentro de una clase
'''
```

---
En la programación orientada a objetos, los métodos estáticos permiten ejecutar funciones directamente desde una clase sin crear instancias, lo que optimiza la estructura del código. En Python, se definen con el decorador @staticmethod, lo que los convierte en herramientas útiles para realizar cálculos o tareas comunes. En este ejercicio, se implementa un método estático dentro de la clase Café que calcula la cantidad de leche necesaria para preparar un latte, aplicando el uso de funciones predefinidas y principios de modularidad.

La clase Café contiene el método estático calcularLeche(tamanyo), que recibe el tamaño de la taza en mililitros y devuelve la cantidad de leche necesaria, calculando el 50% del volumen total.

Para garantizar precisión en los resultados, se utiliza la función math.ceil() del módulo math, un método estático predefinido que redondea hacia arriba.

El método se llama directamente desde la clase, demostrando cómo los métodos estáticos permiten ejecutar operaciones sin crear objetos.

---

- Para realizar este código, primero se importa la biblioteca math para acceder al método estático ceil().
```
import math
```

- Se define la clase Café con el método estático calcularLeche(tamanyo). Se usa la etiqueta @staticmethod para indicar explícitamente que el método no depende de la clase ni de sus instancias. Dentro del método, se calcula el 50% del tamaño de la taza y se redondea hacia arriba. El método se invoca directamente desde la clase.
```
class Café:
    @staticmethod
    def calcularLeche(tamanyo):
        # Calcula el 50% del tamaño de la taza como cantidad de leche
        leche_necesaria = tamanyo * 0.5
        # Redondea el resultado hacia arriba
        return math.ceil(leche_necesaria)
```

- Se define el tamaño de la taza en mililitros
```
tamanyo_taza = 240
```

- Se realia la llamada al método estático directamente desde la clase
```
leche = Café.calcularLeche(tamanyo_taza)
```

- Finalmente, se imprime la cantidad de leche necesaria.
```
print("Cantidad de leche necesaria: ", leche, "ml")
```

---
A continuación se muestra el código funcional completo:
```
'''
Métodos estáticos
2025 Fabiana Victoria Sotillo
Programa que crea un método estático dentro de una clase
'''

# Importamos la biblioteca math para utilizar su método estático ceil()
import math

# Definimos la clase Café con un método estático
class Café:
    @staticmethod
    def calcularLeche(tamanyo):
        # Calcula el 50% del tamaño de la taza como cantidad de leche
        leche_necesaria = tamanyo * 0.5
        # Redondea el resultado hacia arriba
        return math.ceil(leche_necesaria)

# Tamaño de la taza en mililitros
tamanyo_taza = 240

# Llamada al método estático directamente desde la clase
leche = Café.calcularLeche(tamanyo_taza)

# Muestra el resultado
print("Cantidad de leche necesaria: ", leche, "ml")
```

---
Este ejercicio permite comprender cómo aplicar métodos estáticos en Python para realizar operaciones sin instanciar clases. El uso del decorador @staticmethod y del método math.ceil() refuerza la importancia de las herramientas predefinidas del lenguaje y su integración con la programación orientada a objetos.

Además, esta práctica mostró cómo los métodos estáticos pueden emplearse para resolver tareas cotidianas, como calcular proporciones o ingredientes, favoreciendo la claridad, la eficiencia y la modularidad en el desarrollo de programas.