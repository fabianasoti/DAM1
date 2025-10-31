Programa que cuenta elementos en un rango específico
v0.1 Fabiana Sotillo - 1ºDAM

---
El bucle "for", se usa para contar elementos en un rango específico, anidar múltiples bucles para recorrer varios rangos simultáneamente, e incrementar variables en cada iteración del bucle. Esta práctica es fundamental para resolver problemas más complejos que involucren conteo y procesamiento de información.

En este ejercicio, se necesita contar cuántos patitos se producen cada día en distintos años de producción, para ello se hará uso del bucle for, para recorrer los años y los días del mes, aumentando el conteo correspondiente por cada día, de cada año

---
Para ilustrar el funcionamiento del bucle for, se mostrará el paso a paso a continuación con ejemplos:

- Se establecen las variables.
```
patitos_contados = 0
```

- Se realiza el bucle for estableciendo un rango por día.
```
for dia in range(1, 32): 
```

- Se establece el aumento de la variable dentro del rango día.
```
patitos_contados += 5
```

- Se establece el rango de años que se quieren contar, y los meses de cada año, que va a permitir que se vaya aumentando la cantidad de patitos por día, recorriendo estos rangos.
```
for anio in range(1978, 2024): 
    for mes in range(1, 13):
``` 

- Se muestra en pantalla cuántos patitos se han producido desde el 1978 hasta el 2023 y los que se han producido en el 2023 específicamente.
```
print("Hoy es el día", dia, "del mes", mes, "del año", anio, "y se han producido", patitos_contados, "patitos")
```
y,
```
print("Los patitos producidos en 2023, son", patitos_2023)
```

-----

Para ilustrar el uso del bucle for, he construido un primer bloque de código en el que se cuentan la cantidad de patitos que se producen en un año, específicamente en el 2023, considerando que cada día se realizaban  5 patitos.
Y luego he hecho otro bloque donde se recorre el bucle desde 1978 hasta 2023 y se calcula el total de patitos producidos en total, contando desde 1978 hasta 2023. Posteriormente, se vuelve a mostrar cuanto se ha calculado solo en un año, en el 2023.

```
#1 Patitos producidos en el año 2023
patitos_contados = 0
patitos_2023 = 0

for mes in range(1, 13):  # Recorremos los meses del año (1 al 12)
    for dia in range(1, 32):  # Recorremos los días del mes (1 al 31)
        patitos_contados += 5  # Suponemos que producen 5 patitos por día
print("Los patitos producidos en 2023, son", patitos_2023) # Se muestra lo que se ha producido en 2023


#2 Patitos producidos desde 1978 a 2024
patitos_contados = 0
patitos_2023 = 0
for anio in range(1978, 2024):  # Recorremos los años desde 1978 hasta 2023
    for mes in range(1, 13):  # Recorremos los meses del año (1 al 12)
        for dia in range(1, 32):  # Recorremos los días del mes (1 al 31)
            patitos_contados += 5  # Suponemos que producen 5 patitos por día
            print("Hoy es el día", dia, "del mes", mes, "del año", anio, "y se han producido", patitos_contados, "patitos") # Se muestra todo lo que se ha producido en patitos en total desde 1978 hasta 2023
            if anio == 2023:
                patitos_2023 +=1
print("Los patitos producidos en 2023, son", patitos_2023) # Se muestra lo que se ha producido en 2023
  
```

---
Para finalizar, se ha podido demostrar lo útil y práctico que es el bucle for para contar elementos en un rango específico, anidar múltiples bucles para recorrer varios rangos simultáneamente, e incrementar variables en cada iteración del bucle. Esta práctica es fundamental para resolver problemas más complejos que involucren conteo y procesamiento de información.
En este caso, contando la cantidad de patitos producidos desde 1978 hasta el 2023.
