```
'''
Gestión de recetas de latte con listas y diccionarios
2026 Fabiana Sotillo
Programa que almacena recetas de latte utilizando una lista de diccionarios
y permite acceder a información concreta de cada receta.
'''
```

---
En este ejercicio se trabaja con colecciones de datos en Python, concretamente con listas y diccionarios, que permiten organizar información de forma estructurada y accesible. 

En el contexto del arte latte, se simula una situación real en la que un barista desea almacenar distintas recetas de café, cada una con su nombre, ingredientes y pasos de preparación. 

El objetivo principal es comprender cómo representar información mediante estructuras de datos anidadas y cómo acceder a sus elementos utilizando índices y claves.

---
El programa se basa en la creación de una lista llamada recetas_latte, que contiene varios diccionarios. Cada diccionario representa una receta distinta y almacena la siguiente información:
- nombre: nombre de la receta de latte.
- ingredientes: lista de ingredientes necesarios para su preparación.
- pasos: lista de pasos para elaborar la bebida.

Esta estructura permite organizar los datos de forma jerárquica y facilita su consulta posterior. Para acceder a una receta concreta se utilizan índices sobre la lista, y para acceder a la información interna de cada receta se emplean las claves del diccionario.

El acceso a elementos anidados se realiza combinando ambos conceptos: primero se selecciona la receta por su índice y después se accede a los datos mediante la clave correspondiente.

---
A continuación se muestra el código funcional completo:
```
'''
Gestión de recetas de latte con listas y diccionarios
2026 Fabiana Sotillo
Programa que almacena recetas de latte utilizando una lista de diccionarios
y permite acceder a información concreta de cada receta.
'''

recetas_latte = [
    {
        "nombre": "Latte americano",
        "ingredientes": ["Café espresso", "Agua caliente", "Leche"],
        "pasos": [
            "Preparar un café espresso",
            "Añadir agua caliente",
            "Agregar leche caliente"
        ]
    },
    {
        "nombre": "Macchiato",
        "ingredientes": ["Café espresso", "Espuma de leche"],
        "pasos": [
            "Preparar un café espresso",
            "Añadir una pequeña cantidad de espuma de leche"
        ]
    },
    {
        "nombre": "Cappuccino",
        "ingredientes": ["Café espresso", "Leche", "Espuma de leche"],
        "pasos": [
            "Preparar un café espresso",
            "Añadir leche caliente",
            "Coronar con espuma de leche"
        ]
    }
]

# Mostrar el nombre de la segunda receta
print("Nombre de la segunda receta:")
print(recetas_latte[1]["nombre"])

# Mostrar los ingredientes del Cappuccino
print("\nIngredientes del Cappuccino:")
print(recetas_latte[2]["ingredientes"])
```

---
El programa muestra por pantalla el nombre de la segunda receta almacenada en la lista, que corresponde al Macchiato, y posteriormente muestra los ingredientes de la receta Cappuccino, accediendo correctamente a los datos anidados.

Este ejercicio permite aplicar de forma práctica los conceptos fundamentales de listas y diccionarios en Python, así como el acceso a estructuras de datos anidadas mediante índices y claves. 

A través del ejemplo de recetas de latte, se refuerza la importancia de organizar información compleja de manera estructurada y clara. 

Estos conocimientos son esenciales para el desarrollo de aplicaciones reales en las que se necesita gestionar grandes volúmenes de datos, como menús digitales, sistemas de pedidos o bases de datos de recetas en el mundo del arte latte y en cualquier otro ámbito donde sea necesario organizar información de forma eficiente.
