```
'''
Gestión de un menú de comidas con listas y archivos binarios
2025 Fabiana Victoria Sotillo
Programa que permite gestionar un menú de comidas utilizando listas dinámicas
y guardar la información en un archivo binario con pickle.
'''
```

---
En este ejercicio se desarrolla un programa en Python que permite gestionar un menú de comidas utilizando listas dinámicas y almacenamiento en archivos binarios. El programa aplica conceptos fundamentales de programación como variables, listas, bucles, estructuras condicionales, entrada de datos por teclado y uso de módulos externos, concretamente el módulo pickle para la serialización de datos. A través de un menú interactivo, el usuario puede añadir comidas, visualizar el menú completo, guardar la información en un archivo y recuperarla posteriormente. El objetivo principal es practicar el uso de listas y el almacenamiento persistente de datos en archivos binarios.

El programa se basa en una estructura principal con un bucle while True, que mantiene activo un menú de opciones para que el usuario pueda interactuar con el sistema en todo momento. La información se almacena en una lista llamada menu, que contiene los nombres de las comidas introducidas.

Las funcionalidades del programa se organizan mediante una estructura condicional if-elif, donde cada opción ejecuta una acción concreta:

1. Introducir nueva comida: solicita al usuario el nombre de la comida y la añade a la lista menu.

2. Listar comidas: recorre la lista mediante un bucle for y muestra cada elemento almacenado.

3. Guardar en archivo: utiliza el módulo pickle para guardar la lista en un archivo binario llamado datos.bin.

4. Cargar datos: recupera los datos almacenados en el archivo binario y los vuelca nuevamente en la lista.

El uso del módulo pickle permite convertir la lista en un formato binario que puede almacenarse en un archivo y recuperarse más adelante, garantizando así la persistencia de los datos.

---
A continuación se muestra el código completo del programa, el cual implementa todas las funcionalidades mencionadas anteriormente:
```
'''
Gestión de un menú de comidas con listas y archivos binarios
2025 Fabiana Victoria Sotillo
Programa que permite gestionar un menú de comidas utilizando listas dinámicas
y guardar la información en un archivo binario con pickle.
'''

import pickle

menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  print("3.-Guardar en archivo")
  print("4.-Cargar datos de archivo")
  opcion = int(input("Selecciona una opción:"))

  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)

  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)

  elif opcion == 3:
    archivo = open("datos.bin","wb")  # Write Binary
    pickle.dump(menu,archivo)
    archivo.close()
    print("Se ha guardado con éxito ✅")

  elif opcion == 4:
    archivo = open("datos.bin","rb")
    menu = pickle.load(archivo)  # Volcamos el archivo a la lista
    archivo.close()
    print("Se ha cargado con éxito ✅")
```

---
El programa permite al usuario crear un menú de comidas personalizado, añadir nuevos platos, visualizar el menú completo y guardar la información en un archivo binario para recuperarla posteriormente. De esta forma, los datos no se pierden al cerrar el programa.

Este ejercicio permite reforzar el uso de listas dinámicas y el almacenamiento persistente de información mediante archivos binarios en Python. A través de un menú interactivo, el usuario puede gestionar un conjunto de datos de forma sencilla y eficiente, aplicando conceptos como bucles, condicionales, entrada de datos y uso de módulos externos. La utilización del módulo pickle introduce al estudiante en la serialización de datos, una técnica fundamental para el desarrollo de aplicaciones más complejas que requieren guardar y recuperar información entre ejecuciones del programa.
