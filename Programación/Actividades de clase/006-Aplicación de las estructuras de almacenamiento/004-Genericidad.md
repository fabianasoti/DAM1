```
'''
Uso de listas y manejo de excepciones con ingredientes de café
2025 Fabiana Victoria Sotillo
Programa que recorre una lista de ingredientes y calcula el doble de
su cantidad utilizando estructuras try-except para gestionar errores.
'''
```

---
En este ejercicio se desarrolla un programa en Python que permite trabajar con listas y manejar errores mediante estructuras de control de excepciones utilizando try y except. 

A través de una lista de ingredientes necesarios para preparar un café americano, se simula una situación real en la que no todos los valores pueden convertirse correctamente a números. 

El objetivo principal es comprender cómo detectar errores durante la ejecución del programa y gestionarlos correctamente, evitando que el programa se detenga de forma inesperada.

---
El programa comienza declarando una lista llamada ```ingredientes_cafe = ['agua', 'café', 'leche', 'sazón', 'vainilla']```, que contiene distintos ingredientes necesarios para preparar un café. 

Posteriormente se define una función llamada calcular_doble_ingredientes, encargada de recorrer la lista y calcular el doble de cada ingrediente cuando sea posible.
```
def calcular_doble_ingredientes(lista):
```

Dentro de la función se utiliza un bucle for para recorrer todos los elementos de la lista. 
```
 for ingrediente in lista:
```

Para cada elemento, se emplea un bloque try-except que intenta convertir el ingrediente a un número entero. 
```
        try:
            ingrediente = int(ingrediente)
            print(ingrediente * 2)
```

En caso de que no sea posible realizar la conversión, el programa entra en el bloque except y muestra un mensaje indicando que el valor no es válido.
```
        except:
            centinela = False
            for i in range(0, len(ingredientes_etiquetas)):
                if ingrediente == ingredientes_etiquetas[i]:
                    print("Ingrediente:", ingrediente, "- Doble cantidad simulada:", (i + 1) * 2)
                    centinela = True
            if centinela == False:
                print("No válido")

calcular_doble_ingredientes(ingredientes_cafe)
```

Este mecanismo permite que el programa continúe su ejecución aunque se produzcan errores en algunos elementos de la lista, lo que resulta fundamental en programas reales donde los datos pueden no ser siempre correctos.

---
A continuación se muestra el código funcional completo:
```
'''
Uso de listas y manejo de excepciones con ingredientes de café
2025 Fabiana Victoria Sotillo
Programa que recorre una lista de ingredientes y calcula el doble de su cantidad
utilizando estructuras try-except para gestionar errores.
'''

ingredientes_cafe = ['agua', 'café', 'leche', 'caramelo', 'vainilla']
ingredientes_etiquetas = ['agua', 'café', 'leche', 'caramelo', 'vainilla']

def calcular_doble_ingredientes(lista):
    for ingrediente in lista:
        try:
            ingrediente = int(ingrediente)
            print(ingrediente * 2)
        except:
            centinela = False
            for i in range(0, len(ingredientes_etiquetas)):
                if ingrediente == ingredientes_etiquetas[i]:
                    print("Ingrediente:", ingrediente, "- Doble cantidad simulada:", (i + 1) * 2)
                    centinela = True
            if centinela == False:
                print("No válido")

calcular_doble_ingredientes(ingredientes_cafe)

```

---
El programa recorre la lista de ingredientes y trata de convertir cada elemento a un número entero. Cuando no es posible realizar la conversión, se gestiona el error mediante el bloque except, mostrando un mensaje adecuado y permitiendo que el programa continúe con el resto de elementos.

Este ejercicio permite aplicar de forma práctica el uso de listas y el manejo de excepciones en Python mediante las estructuras try y except. A través de un ejemplo basado en ingredientes de café, se refuerza la importancia de controlar los errores durante la ejecución de un programa y de garantizar que este continúe funcionando correctamente incluso cuando se encuentran datos no válidos. 

Este tipo de control es fundamental para el desarrollo de aplicaciones más complejas, donde la validación de datos y la gestión de errores resultan imprescindibles para un correcto funcionamiento.
