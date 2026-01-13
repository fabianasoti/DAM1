```
'''
Uso de matrices multidimensionales y archivos binarios con pickle
2026 Fabiana Sotillo
Programa que permite almacenar los ingredientes de diferentes tipos de café
mediante una matriz multidimensional y guardarlos en un archivo binario.
'''
```

---
En este ejercicio se trabaja con matrices multidimensionales y almacenamiento de información en archivos binarios utilizando Python. El uso de matrices permite organizar datos relacionados entre sí de forma estructurada, como los ingredientes necesarios para preparar diferentes tipos de café. 

A través del módulo pickle, es posible guardar esta información en un archivo y recuperarla posteriormente. El objetivo principal es comprender cómo gestionar información compleja mediante listas anidadas y cómo conservar estos datos para su uso futuro, simulando una situación real como el registro de ingredientes en una barra de cafetería.

El programa se basa en la creación de una matriz multidimensional representada mediante una lista de listas. Cada sublista contiene los ingredientes necesarios para preparar un tipo de café diferente. Esta estructura permite organizar la información de forma clara y accesible.

Una vez creada la matriz, se utiliza el módulo pickle para guardar los datos en un archivo binario. Este proceso se conoce como serialización y permite convertir la estructura de datos en un formato que puede almacenarse en un archivo.

Posteriormente, el archivo binario se abre en modo lectura y se recupera la información almacenada, que se vuelca nuevamente en una variable para poder recorrerla y mostrar su contenido por pantalla. Para mostrar los ingredientes, se utiliza un bucle for junto con la función enumerate, lo que permite numerar cada tipo de café y mostrar sus ingredientes correspondientes.

---
A continuación se muestra el código completo funcional:
```
'''
Uso de matrices multidimensionales y archivos binarios con pickle
2026 Fabiana Sotillo
Programa que permite almacenar los ingredientes de diferentes tipos de café
mediante una matriz multidimensional y guardarlos en un archivo binario.
'''

import pickle

# Se define la matriz multidimensional con los ingredientes de cada café
ingredientes_café = [
    ["Leche", "Expreso"],
    ["Expreso", "Azúcar", "Crema"],
    ["Expreso", "Sirope Caramelo", "Leche"],
    ["Doble Expreso", "Foam Leche"],
    ["Expreso", "Chocolate", "Foam Leche"]
]

# Se guarda la información en un archivo binario
with open("ingredientes_café.bin", "wb") as file:
    pickle.dump(ingredientes_café, file)

print("Datos guardados correctamente en el archivo ingredientes_café.bin")

# Se lee la información desde el archivo binario
with open("ingredientes_café.bin", "rb") as file:
    ingredientes_café = pickle.load(file)

# Se muestra los ingredientes almacenados
print("\nIngredientes guardados:")
for café, ingredientes in enumerate(ingredientes_café):
    print(f"Café {café + 1}: {', '.join(ingredientes)}")
```

---
El programa permite organizar los ingredientes de distintos tipos de café en una matriz multidimensional y almacenarlos en un archivo binario. Posteriormente, los datos se pueden recuperar y mostrar por pantalla, garantizando que la información se conserva entre ejecuciones del programa.

Este ejercicio permite aplicar de forma práctica el uso de matrices multidimensionales para organizar información relacionada y el almacenamiento persistente de datos mediante archivos binarios en Python. 

La combinación de listas anidadas y el módulo pickle facilita la gestión de información compleja, como el registro de ingredientes utilizados en una barra de cafetería. Estos conocimientos resultan fundamentales para el desarrollo de aplicaciones más avanzadas que requieren organizar grandes volúmenes de datos y conservarlos para su uso posterior, reforzando así la lógica de programación y el pensamiento algorítmico.
