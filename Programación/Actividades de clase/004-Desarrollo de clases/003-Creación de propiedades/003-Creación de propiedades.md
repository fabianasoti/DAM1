```
''' 
Aplicación de gestión de clientes
2025 Fabiana Victoria Sotillo
Esta aplicación gestiona clientes
'''
```

---
En programación orientada a objetos, las clases permiten representar entidades del mundo real mediante atributos y métodos. En este ejercicio se trabaja con una clase llamada Cliente, diseñada para almacenar información personal como nombre, edad y una lista de teléfonos. El objetivo es comprender cómo inicializar y manipular propiedades dentro de una clase, aprovechando listas (arrays) para gestionar múltiples datos relacionados con un mismo objeto. Este tipo de estructuras resulta fundamental en la gestión de información en programas que modelan usuarios o clientes en aplicaciones reales.

---
Para construir el programa se siguieron los siguientes pasos:

- La clase Cliente se define utilizando la palabra clave class, e incluye un método especial ```__init__()``` para inicializar sus atributos. 
```
class Cliente:
    def __init__(self):
```

- En este caso, las propiedades nombre, edad y telefonos se inicializan con valores vacíos o nulos: una cadena vacía para nombre, el valor 0 para edad y una lista vacía [ ] para telefonos.
```
     self.nombre = ""
        self.edad = 0
        self.telefonos = []  # lista para almacenar múltiples números de teléfono
```

- Posteriormente, se crea una instancia de la clase y se asignan valores personalizados a cada propiedad.
```
cliente1 = Cliente()

cliente1.nombre = "Fabiana Sotillo"
cliente1.edad = 23
cliente1.telefonos = ["663966930", "667077890"]
```

- Finalmente, se imprimen los datos almacenados para verificar el correcto funcionamiento del código.
```
print("Nombre del cliente:", cliente1.nombre)
print("Edad:", cliente1.edad)
print("Teléfonos:", cliente1.telefonos)
```

---
A continuación se muestra el código funcional completo:

```
''' 
Aplicación de gestión de clientes
2025 Fabiana Victoria Sotillo
Esta aplicación gestiona clientes
'''

# Definición de la clase Cliente
class Cliente:
    def __init__(self):
        # Inicialización de atributos con valores vacíos o nulos
        self.nombre = ""
        self.edad = 0
        self.telefonos = []  # lista para almacenar múltiples números de teléfono

# Creación de una instancia del objeto Cliente
cliente1 = Cliente()

# Asignación de valores a las propiedades
cliente1.nombre = "Fabiana Sotillo"
cliente1.edad = 23
cliente1.telefonos = ["663966930", "667077890"]

# Mostrar los valores asignados
print("Nombre del cliente:", cliente1.nombre)
print("Edad:", cliente1.edad)
print("Teléfonos:", cliente1.telefonos)
```

---
Este ejercicio refuerza el concepto de encapsulamiento y el uso de listas como estructuras para contener múltiples valores asociados a un mismo atributo.
 
Este ejercicio permite comprender cómo definir e inicializar atributos dentro de una clase, utilizando listas para manejar múltiples valores asociados a un mismo objeto. La clase Cliente representa un ejemplo práctico de modelado de datos personales, un concepto fundamental para sistemas de registro, bases de datos o aplicaciones comerciales. Además, refuerza la comprensión de la estructura interna de los objetos y el uso de propiedades para almacenar información compleja, sentando las bases para el desarrollo de programas más avanzados que gestionen clientes, pedidos o catálogos de manera eficiente.