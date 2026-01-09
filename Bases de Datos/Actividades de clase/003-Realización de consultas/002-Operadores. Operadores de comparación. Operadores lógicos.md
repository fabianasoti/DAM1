```
'''
Operadores lógicos, aritméticos y de comparación en SQL
2026 Fabiana Sotillo
Se realizan consultas con operadores para generar nuevos valores a partir de los datos originales sin modificar la información almacenada en la base de datos
'''
```

---
En esta actividad se utilizan operadores aritméticos para realizar cálculos sobre los valores de una columna en una base de datos en SQL, operaciones como sumas, restas y multiplicaciones, lo que permite generar nuevos valores a partir de los datos originales sin modificar la información almacenada en la base de datos. Asimismo, se emplean operadores lógicos junto con la estructura condicional CASE para clasificar a los clientes según su edad en diferentes grupos.

Además, se refuerza el uso de alias mediante la cláusula AS, lo que permite asignar nombres personalizados a las columnas generadas en las consultas, facilitando la interpretación de los resultados. De esta manera, se integran cálculos, condiciones y presentación de datos en una misma consulta, mejorando la capacidad de análisis de la información.

---
A continuación, se presentan las consultas SQL utilizadas en el ejercicio junto con su explicación.

1. Uso de operadores aritméticos para aumentar la edad.
```
SELECT 
    nombre,
    apellidos,
    edad + 500 AS 'Edad aumentada'
FROM clientes;
```

Esta consulta selecciona las columnas nombre, apellidos y calcula una nueva columna llamada Edad aumentada, que resulta de sumar 500 al valor original de la columna edad. Esta operación se realiza únicamente en el resultado de la consulta y no modifica los datos almacenados.
```
+----------+------------+----------------+
| nombre   | apellidos  | Edad aumentada |
+----------+------------+----------------+
| Juan     | Lopez      |            545 |
| Javier   | Martinez   |            546 |
| Ana      | Sánchez    |            534 |
| María    | Gómez      |            529 |
| Luis     | Fernández  |            551 |
| Carmen   | Ruiz       |            538 |
| Pablo    | Hernández  |            527 |
| Elena    | Jiménez    |            542 |
| Sergio   | Álvarez    |            533 |
| Laura    | Moreno     |            525 |
| Raúl     | Muñoz      |            548 |
| Isabel   | Romero     |            536 |
| David    | Navarro    |            531 |
| Patricia | Torres     |            540 |
| Alberto  | Domínguez  |            553 |
| Cristina | Vázquez    |            530 |
| Rubén    | Ramos      |            528 |
| Beatriz  | Gil        |            544 |
| Jorge    | Castro     |            539 |
| Natalia  | Ortiz      |            526 |
| Óscar    | Rubio      |            550 |
| Silvia   | Molina     |            532 |
| Víctor   | Delgado    |            541 |
| Rocío    | Cabrera    |            537 |
| Héctor   | Santos     |            535 |
| Lucía    | Iglesias   |            524 |
| Andrés   | Cortés     |            547 |
| Marta    | Peña       |            528 |
| Tomás    | Flores     |            552 |
| Noelia   | Cano       |            533 |
| Gonzalo  | León       |            545 |
| Irene    | Serrano    |            527 |
+----------+------------+----------------+
```

---
2. Uso de operadores aritméticos para disminuir la edad
```
SELECT 
    nombre,
    apellidos,
    edad - 100 AS 'Edad reducida'
FROM clientes;
```

En esta consulta se resta 100 al valor de la columna edad, generando una nueva columna llamada Edad reducida, lo que permite practicar operaciones matemáticas básicas sobre los datos.
```
+----------+------------+---------------+
| nombre   | apellidos  | Edad reducida |
+----------+------------+---------------+
| Juan     | Lopez      |           -55 |
| Javier   | Martinez   |           -54 |
| Ana      | Sánchez    |           -66 |
| María    | Gómez      |           -71 |
| Luis     | Fernández  |           -49 |
| Carmen   | Ruiz       |           -62 |
| Pablo    | Hernández  |           -73 |
| Elena    | Jiménez    |           -58 |
| Sergio   | Álvarez    |           -67 |
| Laura    | Moreno     |           -75 |
| Raúl     | Muñoz      |           -52 |
| Isabel   | Romero     |           -64 |
| David    | Navarro    |           -69 |
| Patricia | Torres     |           -60 |
| Alberto  | Domínguez  |           -47 |
| Cristina | Vázquez    |           -70 |
| Rubén    | Ramos      |           -72 |
| Beatriz  | Gil        |           -56 |
| Jorge    | Castro     |           -61 |
| Natalia  | Ortiz      |           -74 |
| Óscar    | Rubio      |           -50 |
| Silvia   | Molina     |           -68 |
| Víctor   | Delgado    |           -59 |
| Rocío    | Cabrera    |           -63 |
| Héctor   | Santos     |           -65 |
| Lucía    | Iglesias   |           -76 |
| Andrés   | Cortés     |           -53 |
| Marta    | Peña       |           -72 |
| Tomás    | Flores     |           -48 |
| Noelia   | Cano       |           -67 |
| Gonzalo  | León       |           -55 |
| Irene    | Serrano    |           -73 |
+----------+------------+---------------+
```

---
3. Uso de operadores lógicos para clasificar por edad
```
SELECT 
    nombre,
    apellidos,
    edad,
    CASE 
        WHEN edad < 30 THEN 'Menor de 30 años'
        WHEN edad >= 30 AND edad < 40 THEN 'Entre 30 y 40 años'
        ELSE 'Mayor o igual a 40 años'
    END AS 'Edad grupo'
FROM clientes;
```

Esta consulta utiliza la estructura condicional CASE junto con operadores lógicos (<, >=, AND) para clasificar a los clientes en diferentes grupos de edad. El resultado muestra una nueva columna llamada Edad grupo, que indica a qué rango etario pertenece cada cliente.

```
+----------+------------+------+--------------------------+
| nombre   | apellidos  | edad | Edad grupo               |
+----------+------------+------+--------------------------+
| Juan     | Lopez      |   45 | Mayor o igual a 40 años  |
| Javier   | Martinez   |   46 | Mayor o igual a 40 años  |
| Ana      | Sánchez    |   34 | Entre 30 y 40 años       |
| María    | Gómez      |   29 | Menor de 30 años         |
| Luis     | Fernández  |   51 | Mayor o igual a 40 años  |
| Carmen   | Ruiz       |   38 | Entre 30 y 40 años       |
| Pablo    | Hernández  |   27 | Menor de 30 años         |
| Elena    | Jiménez    |   42 | Mayor o igual a 40 años  |
| Sergio   | Álvarez    |   33 | Entre 30 y 40 años       |
| Laura    | Moreno     |   25 | Menor de 30 años         |
| Raúl     | Muñoz      |   48 | Mayor o igual a 40 años  |
| Isabel   | Romero     |   36 | Entre 30 y 40 años       |
| David    | Navarro    |   31 | Entre 30 y 40 años       |
| Patricia | Torres     |   40 | Mayor o igual a 40 años  |
| Alberto  | Domínguez  |   53 | Mayor o igual a 40 años  |
| Cristina | Vázquez    |   30 | Entre 30 y 40 años       |
| Rubén    | Ramos      |   28 | Menor de 30 años         |
| Beatriz  | Gil        |   44 | Mayor o igual a 40 años  |
| Jorge    | Castro     |   39 | Entre 30 y 40 años       |
| Natalia  | Ortiz      |   26 | Menor de 30 años         |
| Óscar    | Rubio      |   50 | Mayor o igual a 40 años  |
| Silvia   | Molina     |   32 | Entre 30 y 40 años       |
| Víctor   | Delgado    |   41 | Mayor o igual a 40 años  |
| Rocío    | Cabrera    |   37 | Entre 30 y 40 años       |
| Héctor   | Santos     |   35 | Entre 30 y 40 años       |
| Lucía    | Iglesias   |   24 | Menor de 30 años         |
| Andrés   | Cortés     |   47 | Mayor o igual a 40 años  |
| Marta    | Peña       |   28 | Menor de 30 años         |
| Tomás    | Flores     |   52 | Mayor o igual a 40 años  |
| Noelia   | Cano       |   33 | Entre 30 y 40 años       |
| Gonzalo  | León       |   45 | Mayor o igual a 40 años  |
| Irene    | Serrano    |   27 | Menor de 30 años         |
+----------+------------+------+--------------------------+
```

---
4. Uso combinado de operadores aritméticos y lógicos con alias
```
SELECT 
    nombre,
    apellidos,
    edad * 2 AS 'Doble edad',
    CASE 
        WHEN edad < 30 THEN 'Menor de 30 años'
        ELSE 'Mayor o igual a 30 años'
    END AS 'Grupo etario'
FROM clientes;
```

En esta consulta se multiplica la edad por dos para crear la columna Doble edad y, al mismo tiempo, se clasifica a los clientes en dos grupos mediante una condición lógica, asignando alias a ambas columnas generadas.

Como resultado de estas consultas, se obtiene una tabla que muestra los datos de los clientes junto con columnas calculadas y clasificaciones por rangos de edad, lo que permite analizar la información desde diferentes perspectivas.
```
+----------+------------+------------+--------------------------+
| nombre   | apellidos  | Doble edad | Grupo etario             |
+----------+------------+------------+--------------------------+
| Juan     | Lopez      |         90 | Mayor o igual a 30 años  |
| Javier   | Martinez   |         92 | Mayor o igual a 30 años  |
| Ana      | Sánchez    |         68 | Mayor o igual a 30 años  |
| María    | Gómez      |         58 | Menor de 30 años         |
| Luis     | Fernández  |        102 | Mayor o igual a 30 años  |
| Carmen   | Ruiz       |         76 | Mayor o igual a 30 años  |
| Pablo    | Hernández  |         54 | Menor de 30 años         |
| Elena    | Jiménez    |         84 | Mayor o igual a 30 años  |
| Sergio   | Álvarez    |         66 | Mayor o igual a 30 años  |
| Laura    | Moreno     |         50 | Menor de 30 años         |
| Raúl     | Muñoz      |         96 | Mayor o igual a 30 años  |
| Isabel   | Romero     |         72 | Mayor o igual a 30 años  |
| David    | Navarro    |         62 | Mayor o igual a 30 años  |
| Patricia | Torres     |         80 | Mayor o igual a 30 años  |
| Alberto  | Domínguez  |        106 | Mayor o igual a 30 años  |
| Cristina | Vázquez    |         60 | Mayor o igual a 30 años  |
| Rubén    | Ramos      |         56 | Menor de 30 años         |
| Beatriz  | Gil        |         88 | Mayor o igual a 30 años  |
| Jorge    | Castro     |         78 | Mayor o igual a 30 años  |
| Natalia  | Ortiz      |         52 | Menor de 30 años         |
| Óscar    | Rubio      |        100 | Mayor o igual a 30 años  |
| Silvia   | Molina     |         64 | Mayor o igual a 30 años  |
| Víctor   | Delgado    |         82 | Mayor o igual a 30 años  |
| Rocío    | Cabrera    |         74 | Mayor o igual a 30 años  |
| Héctor   | Santos     |         70 | Mayor o igual a 30 años  |
| Lucía    | Iglesias   |         48 | Menor de 30 años         |
| Andrés   | Cortés     |         94 | Mayor o igual a 30 años  |
| Marta    | Peña       |         56 | Menor de 30 años         |
| Tomás    | Flores     |        104 | Mayor o igual a 30 años  |
| Noelia   | Cano       |         66 | Mayor o igual a 30 años  |
| Gonzalo  | León       |         90 | Mayor o igual a 30 años  |
| Irene    | Serrano    |         54 | Menor de 30 años         |
+----------+------------+------------+--------------------------+
```

---
Este ejercicio permite aplicar de forma práctica los operadores aritméticos y lógicos en SQL para realizar cálculos sobre los datos y establecer condiciones que facilitan su clasificación. Estas operaciones son fundamentales para el análisis de información en bases de datos, ya que permiten transformar y organizar los datos de manera dinámica sin alterar su contenido original. Asimismo, el uso de alias mejora la presentación de los resultados, contribuyendo al desarrollo de consultas más claras y estructuradas.
