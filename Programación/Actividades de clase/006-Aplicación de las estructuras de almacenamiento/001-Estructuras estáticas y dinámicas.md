```
'''
Gestión de una lista de la compra con listas dinámicas
2026 Fabiana Sotillo
Programa que permite gestionar una lista de la compra 
utilizando listas y diccionarios con CRUD interactivo
'''
```

---
En este ejercicio se desarrolla un programa en Python que permite gestionar una lista de la compra mediante el uso de estructuras dinámicas, concretamente listas y diccionarios. El programa aplica conceptos fundamentales de programación como variables, estructuras condicionales, bucles, entrada de datos por teclado y manipulación de listas. 

A través de un menú interactivo, el usuario puede añadir productos, visualizar la lista completa, eliminar un producto específico y modificar los datos de un elemento existente. 

El objetivo principal es practicar el uso de listas y recorrerlas dinámicamente para gestionar información de forma eficiente, simulando una situación cotidiana como la organización de una compra.

---
El programa se basa en una estructura principal compuesta por un bucle infinito while True, que permite que el menú se muestre de forma continua hasta que el usuario decida finalizar la ejecución manualmente. Para almacenar los datos se utiliza una lista llamada lista_de_la_compra, donde cada producto se representa mediante un diccionario con dos claves: nombre y cantidad.

El funcionamiento del programa se organiza mediante un menú de opciones que se gestiona con una estructura condicional if-elif. Cada opción ejecuta una funcionalidad distinta:

1. Añadir elemento a la lista: solicita al usuario el nombre y la cantidad del producto y los almacena en la lista.

2. Leer la lista: recorre la lista mediante un bucle for y muestra todos los productos registrados.

3. Eliminar un producto: permite seleccionar un producto por su índice y eliminarlo de la lista.

4. Modificar un producto: permite sobreescribir el nombre y la cantidad de un producto existente.

El uso de enumerate() permite mostrar los índices de los productos para que el usuario pueda identificarlos fácilmente al eliminarlos o modificarlos. Además, se incluyen comprobaciones para evitar errores cuando el usuario introduce un índice que no existe.

---
A continuación se muestra el código completo del programa, el cual implementa todas las funcionalidades anteriormente mencionadas:
```
'''
Gestión de una lista de la compra con listas dinámicas
2026 Fabiana Sotillo
Programa que permite gestionar una lista de la compra 
utilizando listas y diccionarios con CRUD interactivo
'''

print("Lista de la compra v0.1")

lista_de_la_compra = []

while True:
    print("\nSelecciona una opcion") 
    print("1.-Añadir elemento a la lista")
    print("2.-Leer la lista")
    print("3.-Eliminar elemento de la lista")
    print("4.-Modificar elemento de la lista") 
    
    opcion = int(input("Tu opción: "))
  
    if opcion == 1:
        print("Añadimos un elemento a la lista:")
        nombre = input("Indica el nombre del producto: ")
        cantidad = input("Indica la cantidad del producto: ")
        lista_de_la_compra.append("nombre: ",nombre, "cantidad: ", cantidad)
        
    elif opcion == 2:
        print("Listamos los elementos de la lista:")
        for producto in lista_de_la_compra:
            print("Producto:", producto['nombre'])
            print("Cantidad:", producto['cantidad'])
            print("##############################")

    elif opcion == 3: 
        print("Eliminamos un elemento de la lista:")
        for indice, producto in enumerate(lista_de_la_compra):
            print(indice, ".- Producto:", producto['nombre']) 
            print("    Cantidad:", producto['cantidad'])
        
        print("##############################")
        
        id_producto = int(input("Selecciona el id del producto a eliminar: "))
        
        if 0 <= id_producto < len(lista_de_la_compra):
            lista_de_la_compra.pop(id_producto)
            print("Producto eliminado.")
        else:
            print("ID incorrecto.")

    elif opcion == 4:
        print("Modificamos un elemento de la lista:")
        # 1. Mostramos la lista igual que en la opción 3 para saber el ID
        for indice, producto in enumerate(lista_de_la_compra):
            print(indice, ".- Producto:", producto['nombre']) 
            print("    Cantidad:", producto['cantidad'])
        
        print("##############################")

        # 2. Pedimos el ID
        indice = int(input("Introduce el índice del producto a modificar: "))

        # 3. Verificamos que el ID existe
        if 0 <= indice < len(lista_de_la_compra):
            nuevo_nombre = input("Nuevo nombre del producto: ")
            nueva_cantidad = input("Nueva cantidad: ")

            lista_de_la_compra[indice]["nombre"] = nuevo_nombre
            lista_de_la_compra[indice]["cantidad"] = nueva_cantidad
            print("Producto modificado correctamente.")
        else:
            print("Error: índice no válido.")
```

---
El programa permite al usuario gestionar una lista de la compra de forma dinámica, añadiendo productos, visualizándolos en pantalla, eliminando elementos concretos y modificando su contenido. Gracias al uso de bucles y condicionales, el menú se mantiene activo y permite realizar múltiples operaciones consecutivas.

Este ejercicio permite aplicar de forma práctica los conceptos fundamentales de programación en Python, como el uso de listas dinámicas, diccionarios, bucles, condicionales y entrada de datos por teclado. 

A través de la simulación de gestión de una lista de la compra, una actividad cotidiana, se refuerza el pensamiento algorítmico y la lógica de programación, ya que el usuario interactúa constantemente con estructuras de datos que se modifican en tiempo real. Este tipo de ejercicios resulta especialmente útil como base para el aprendizaje de estructuras más complejas y para el desarrollo de programas interactivos orientados a la gestión de información.
