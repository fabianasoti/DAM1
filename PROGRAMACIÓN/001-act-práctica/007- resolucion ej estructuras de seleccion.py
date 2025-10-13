En este mundo tan diverso y apasionante, donde cada persona tiene su propio ritmo y pasión, en el caso de un entrenador de futbol, sería muy útil poder tener un programa que clasifique a sus jugadores por categorías según su edad, para así poder crear equipos equitativos e inscribirlos a un torneo. También podría ser util para clasificar el tamaño de un café según la cantidad de líquido que quepa en cada taza, por ejemplo, de manera conceptual: si en la taza caben hasta 200ml, el tamaño sería pequeño; si la taza es de máximo 350ml, el tamaño sería mediano; si la taza es de hasta 500ml, el tamaño sería grande. Se podría aplicar el ejemplo a mis hobbies de esta manera:
```
# Establezco variables
taza_ml = input("Dime cuantos mililitros caben en tu taza: ")
taza_ml = int(taza_ml)
# Se realiza la clasificación del tamaño de tazas usando if, elif y else
if taza_ml <= 200: # Y se muestra en pantalla el tamaño del café en cada caso
    print("Tu café es pequeño")
elif taza_ml <= 350:
    print("Tu café es mediano")
elif taza_ml <= 500:
    print("Tu café es grande")
```

Así que, mientras canto una melodía relajante y me tomo un café con arte latte, realizo este programa sencillo que ayudaría al entrenador de futbol a categorizar a sus jugadores.

Para ello:
- Se define la variable de la edad del jugador de esta forma:
```
edad_jugador = input("Dime tu edad: ")
edad_jugador = int(edad_jugador)
```
- Se realiza la clasificación de categoría por edad usando if, elif, else, de esta manera: 

Se utiliza el if para el primer condicional:
```
# Si la edad es menor a 10 años, imprime "Eres un niño".
if edad_jugador < 10 :
    print("Eres un niño")
```

Se utiliza el elif para los siguientes condicionales:
```
# Si la edad está entre 10 y 20 años (inclusive), imprime "Eres un adolescente".
elif edad_jugador >= 10 and edad_jugador <= 20:
    print("Eres un adolescente")
# Si la edad está entre 20 y 30 años (inclusive), imprime "Eres un joven".
elif edad_jugador >= 20 and edad_jugador <= 30:
    print("Eres un joven")
```

Y para cualquier otro supuesto que no se incluya en los condicionales anteriores, se utiliza el else:
```
# Para cualquier otra edad, imprime "Ya no eres un joven".
else:
    print("Ya no eres un joven")
```

Posteriormente, para ilustrar el programa, se muestra el siguiente bloque de código:

```
'''
Programa que clasifica a los jugadores
v.1 Fabiana Sotillo
Este programa categoriza a los jugadores según su edad
'''
# Se define la variable de la edad del jugador
edad_jugador = input("Dime tu edad: ")
edad_jugador = int(edad_jugador) # Se convierte la edad a entero

#Se realiza la clasificación de categoría por edad usando if, elif, else
# Si la edad es menor a 10 años, imprime "Eres un niño".
if edad_jugador < 10 :
    print("Eres un niño")
# Si la edad está entre 10 y 20 años (inclusive), imprime "Eres un adolescente".
elif edad_jugador >= 10 and edad_jugador <= 20:
    print("Eres un adolescente")
# Si la edad está entre 20 y 30 años (inclusive), imprime "Eres un joven".
elif edad_jugador >= 20 and edad_jugador <= 30:
    print("Eres un joven")
# Para cualquier otra edad, imprime "Ya no eres un joven".
else:
    print("Ya no eres un joven")
```

De esta manera, se puede concluir que los condicionales son necesarios y útiles para clasificar por categorías ciertos elementos, y que son tan sencillos de usar que se pueden construir mientras se juega una partida de League of Legends o se toma un café con arte latte. Además, se podría usar para clasificar los cafés por tamaño de taza, o si un personaje en el LOL se va quedando sin puntos de vida y finalmente muere, o la cantidad de hilo que se gasta para hacer un proyecto a crochet dependiendo del tamaño de este.

El uso del if, elif y else es sumamente práctico para realizar categorías y clasificaciones, deben ser debidamente utilizados con sus identaciones y evitar anidaciones innecesarias.
