```
'''
Gestión de clientes
2025 Fabiana Victoria Sotillo
Programa CRUD para gestionar una clase
'''
```

---
La programación orientada a objetos nos permite dar mejor estructura y manejo a los datos, lo que es sumamente importante en la programación. Para ello es necesario comprender sus conceptos fundamentales, tales como las clases.

Una clase, es una plantilla que define las características y comportamientos de los objetos; a su vez, cada objeto es una instancia concreta de una clase, con valores propios en sus atributos, que representan sus propiedades.

Este ejercicio se centra en la creación de un programa de gestión de clientes que permite realizar las operaciones básicas de un sistema CRUD: Crear, Leer, Actualizar y Eliminar.  

Las listas [ ] permiten almacenar y organizar múltiples objetos, facilitando su acceso mediante índices numéricos, lo que nos servirá para añadir múltiples objetos a la clase.

Se hará uso del bucle while, que servirá para mantener activo un menú interactivo que ejecuta acciones repetitivas mientras el programa siga en funcionamiento. 

Finalmente, se hace uso de la función input() para permitir la entrada de datos por parte del usuario, haciendo posible la personalización de la información que el programa gestiona. Todos estos elementos se combinan para construir un sistema funcional que simula la administración básica de clientes.

Los objetivos principales del ejercicio son: definir una clase Cliente con los atributos email, nombre y direccion; implementar una lista clientes para almacenar los objetos creados; diseñar un menú interactivo que permita ejecutar las operaciones CRUD; y favorecer la comprensión de la estructura y lógica de un programa modular orientado a objetos.

---

Se ejemplificará el proceso de construcción del código paso a paso:

- Se define la clase Cliente con un método constructor ```__init__``` que inicializa los tres atributos principales. Cada vez que se crea un nuevo objeto Cliente, este almacena los datos proporcionados por el usuario (correo electrónico, nombre y dirección):
```
class Cliente():
    def __init__(self, email, nombre, direccion):
        self.email = email
        self.nombre = nombre
        self.direccion = direccion
```

- Se inicializa una lista vacía clientes donde se guardarán los objetos creados.
```
clientes = []
```

- El menú principal se ejecuta dentro de un bucle while True, que garantiza que el usuario pueda realizar varias operaciones seguidas hasta que decida salir:
```
while True:
    print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Actualizar un cliente")
    print("4.-Eliminar un cliente")
    opcion = int(input("Escoge una opción: "))
```

- Cada número del menú ejecuta una parte específica del programa, estructurados dentro de un bloque de condicionales if-elif:

    - Opción 1: Insertar un cliente: Solicita los datos del usuario, crea un objeto Cliente y lo agrega a la lista.

    - Opción 2: Listar clientes: Muestra todos los clientes con su ID (índice en la lista) y sus datos.

    - Opción 3: Actualizar un cliente: Permite modificar los atributos de un cliente existente seleccionando su ID.

    - Opción 4: Eliminar un cliente: Solicita confirmación antes de eliminar un cliente de la lista.
```
if opcion == 1:
        email = input("Introduce el email: ")
        nombre = input("Introduce el nombre: ")
        direccion = input("Introduce la dirección: ")
        clientes.append(Cliente(email, nombre, direccion))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID:", identificador)
            print(cliente.email, cliente.nombre, cliente.direccion)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el id para modificar: "))
        email = input("Introduce el nuevo email: ")
        nombre = input("Introduce el nuevo nombre: ")
        direccion = input("Introduce la nueva dirección: ")
        clientes[identificador].email = email
        clientes[identificador].nombre = nombre
        clientes[identificador].direccion = direccion

    elif opcion == 4:
        identificador = int(input("Introduce el ID para eliminar: "))
        confirmacion = input("¿Estás seguro? (S/N): ").lower()
        if confirmacion == "s":
            clientes.pop(identificador)
        elif confirmacion == "n":
            print("Cancelado")
        else:
            print("Opción no válida")
```

---
A continuación se muestra el código completo y funcional:
```
'''
Gestión de clientes
2025 Fabiana Victoria Sotillo
Programa CRUD para gestionar una clase
'''
class Cliente():
    def __init__(self, email, nombre, direccion):
        self.email = email
        self.nombre = nombre
        self.direccion = direccion


print("_________________________")
print("Gestión de clientes v0.1")
print("Fabiana Victoria Sotillo")
print("_________________________")

clientes = []

while True:
    print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Actualizar un cliente")
    print("4.-Eliminar un cliente")
    opcion = int(input("Escoge una opción: "))

    if opcion == 1:
        email = input("Introduce el email: ")
        nombre = input("Introduce el nombre: ")
        direccion = input("Introduce la dirección: ")
        clientes.append(Cliente(email, nombre, direccion))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID:", identificador)
            print(cliente.email, cliente.nombre, cliente.direccion)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el id para modificar: "))
        email = input("Introduce el nuevo email: ")
        nombre = input("Introduce el nuevo nombre: ")
        direccion = input("Introduce la nueva dirección: ")
        clientes[identificador].email = email
        clientes[identificador].nombre = nombre
        clientes[identificador].direccion = direccion

    elif opcion == 4:
        identificador = int(input("Introduce el ID para eliminar: "))
        confirmacion = input("¿Estás seguro? (S/N): ").lower()
        if confirmacion == "s":
            clientes.pop(identificador)
        elif confirmacion == "n":
            print("Cancelado")
        else:
            print("Opción no válida")
```

---

Este ejercicio permite aplicar los conceptos fundamentales de la programación orientada a objetos y el manejo de listas en Python.
La implementación del menú CRUD reforzó el uso de estructuras de control (while, if/elif) y la interacción con el usuario mediante input().

Además, este tipo de programa es una base ideal para comprender cómo funcionan sistemas de gestión más complejos (como bases de datos o interfaces gráficas), fomentando el pensamiento algorítmico y la organización modular del código, sentando las bases para el desarrollo de programas más complejos.