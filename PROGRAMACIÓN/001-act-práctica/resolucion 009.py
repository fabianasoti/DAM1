Programa que crea una función y la importa para ejecutarla
v.01 2025 Fabiana Victoria Sotillo
1ºDAM

---
Las funciones en programación sirven para agrupar código que realiza una tarea específica, lo que permite reutilizarlo, organizar el programa en módulos más simples y fáciles de mantener, y reducir la redundancia del código.
En este caso se usa para guardar una función que calcula una suma entre dos números enteros.

---
Para ello:

- Se crea la función
```
def calculaSuma(operando1, operando2):
```

- Se realiza la operación de suma entre dos parámetros
```
resultado = operando1 + operando2
```

- Se devuelve el resultado de la suma
```
return resultado
```

- Se guarda la función creada en un archivo, en este caso le llamamos: "funcionsuma.py"

- Se importa la función desde funcionsuma.py 
```
from funcionsuma import calculaSuma
```

- Se llama a la función con dos números enteros (4, 3), y finalmente, se muestra el resultado.
```
print(calculaSuma(4,3))
```

---

Para ejemplificar el programa, tenemos el siguiente bloque:
```
def calculaSuma(operando1, operando2):  # Se crea la funcion calculaSuma
    resultado = operando1 + operando2   # Se realiza la operación de suma entre dos parámetros
    return resultado   # Se devuelve el resultado de la suma
# Se guarda la función calculaSuma en un archivo llamado "funcionsuma.py"


from funcionsuma import calculaSuma  # Se importa la función desde funcionsuma.py 
print(calculaSuma(4,3))  # Se llama a la función con dos números enteros (4, 3), y se muestra el resultado.
```

---

Con esto se puede concluir lo importante que es la comprensión sobre el uso práctico de las funciones, ya que con estas se pueden crear - valga la redundancia - funciones que puedan reutilizarse en distintos tipos de programas y de esta manera mermar la redundancia de datos, así, podemos tener códigos más organizados.
