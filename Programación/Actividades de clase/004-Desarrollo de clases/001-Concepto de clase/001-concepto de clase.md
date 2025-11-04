Construcción de clases y métodos

2025 Fabiana Victoria Sotillo

Programa que define clases, objetos con sus propiedades, métodos y constructores

---

En la programación orientada a objetos, existen conceptos fundamentales: clases, objetos, atributos, métodos y constructores. 

Una clase permite crear tipos de objetos con características y comportamientos específicos, mientras que un objeto representa una instancia concreta de esa clase. Los atributos o propiedades almacenan la información asociada a cada objeto, y los métodos son las funciones que determinan las acciones que este puede realizar. Finalmente, el constructor (__init__) es un método especial que se ejecuta automáticamente al crear un objeto, permitiendo inicializar sus atributos y garantizar su correcto funcionamiento desde el inicio.

A continuación se creará una clase en Python que modele un objeto de la vida real: un café o cafetería.
A través de esta práctica, se busca comprender cómo funcionan los atributos (propiedades) y los métodos (funciones dentro de una clase), así como la forma de instanciar objetos a partir de una clase.

Para ello, se explica el paso a paso de la construcción del código:

- Se define la clase Café con el método constructor __init__, que recibe los parámetros nombre y ubicación y se usa self para asignar estos valores a los atributos del objeto.
```
class Café:
  def __init__(self, nombre, ubicación):
    self.nombre = nombre
    self.ubicación = ubicación
```

- Se define el método preparar_café, que al llamarlo, imprime un mensaje que incluye el nombre del café donde se está preparando.
```
  def preparar_café(self):
    print("El café está siendo preparado en", self.nombre)
```

- Se crea un objeto mi_cafe con nombre y ubicación específicos, para luego ser usado cuando se llame al método preparar_café, que mostrará el mensaje correspondiente.
```
# Crear un objeto de la clase Café
mi_cafe = Café("Café DDL", "Av. San Vicente Martir")

# Llamar al método preparar_café
mi_cafe.preparar_café()
```

A continuación, se ilustra el código completo:
```
'''
Construcción de clases y métodos
2025 Fabiana Victoria Sotillo
Programa que define clases, objetos con sus propiedades, métodos y constructores
'''
class Café:
  def __init__(self, nombre, ubicación):
    self.nombre = nombre
    self.ubicación = ubicación
  
  def preparar_café(self):
    print("El café está siendo preparado en", self.nombre)

# Crear un objeto de la clase Café
mi_cafe = Café("Café DDL", "Av. San Vicente Martir")

# Llamar al método preparar_café
mi_cafe.preparar_café()
```

El mensaje que se muestra en pantalla después de ejecutar el código es:
```
El café está siendo preparado en Café DDL
```

En este ejercicio se aplicaron los conceptos fundamentales de la programación orientada a objetos (POO) en Python.
Se comprendió cómo definir una clase, crear atributos y métodos, y generar instancias que permiten modelar elementos dentro del código.

La práctica refuerza el pensamiento lógico al mostrar cómo los objetos pueden encapsular información y comportamientos, sentando las bases para trabajar con estructuras de código más complejos.