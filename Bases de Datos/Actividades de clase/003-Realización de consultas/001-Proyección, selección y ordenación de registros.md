```
'''
Proyección, selección y ordenación de registros en SQL
2026 Fabiana Sotillo
Se realizan consultas de selección, proyección y ordenación de registros en SQL
'''
```

---
El presente ejercicio se centra en el uso del lenguaje SQL como herramienta fundamental para la gestión y consulta de bases de datos, específicamente en la aplicación de conceptos como la selección de columnas, la ordenación de registros y la personalización de los nombres de los campos mostrados en los resultados.

En este contexto, se ha creado una base de datos llamada clientes, y se trabaja con una tabla llamada clientes, se hacen una serie de inserciones ficticias dentro de esta tabla con la siguiente estructura:
```
CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	edad INT
);
```

Y luego se aplican cláusulas como SELECT, FROM, ORDER BY y AS, cuyo propósito es filtrar los datos necesarios, ordenarlos en función de un criterio específico y mostrar los resultados con nombres de columnas personalizados.

---
En esta actividad se utilizan diferentes consultas SQL para practicar tres conceptos fundamentales: la ordenación descendente de datos, la selección de columnas específicas y el uso de alias para nombrar columnas en los resultados.

En primer lugar, se trabaja la ordenación descendente mediante la cláusula ORDER BY acompañada de la palabra clave DESC, la cual permite ordenar los registros de una tabla desde el valor más alto al más bajo según el campo indicado. En este caso, se utiliza el campo edad para mostrar a los clientes desde el mayor hasta el menor.

En segundo lugar, se aborda la selección de columnas específicas utilizando la instrucción SELECT, que permite indicar únicamente los campos que se desean mostrar en la consulta, evitando así mostrar información innecesaria.

Por último, se emplea la cláusula AS para asignar alias a las columnas, lo que permite personalizar los nombres que aparecen en el resultado de la consulta, facilitando su lectura e interpretación.

---
A continuación, se presentan las consultas SQL utilizadas en el ejercicio, junto con su explicación.

1. Ordenación descendente por edad
```
SELECT 
    nombre AS 'Nombre del cliente',
    apellidos AS 'Apellidos del cliente',
    edad AS 'Edad del cliente'
FROM 
    clientes
ORDER BY
    edad DESC;
```

Esta consulta selecciona los campos nombre, apellidos y edad de la tabla clientes. Mediante la cláusula AS, se renombran las columnas para que aparezcan con un formato más descriptivo en el resultado. Posteriormente, se utiliza ORDER BY edad DESC para ordenar los registros desde el cliente de mayor edad hasta el de menor edad. Dando como resultado la siguiente imagen de la tabla.

```
+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Alberto            | Domínguez             |               53 |
| Tomás              | Flores                |               52 |
| Luis               | Fernández             |               51 |
| Óscar              | Rubio                 |               50 |
| Raúl               | Muñoz                 |               48 |
| Andrés             | Cortés                |               47 |
| Javier             | Martinez              |               46 |
| Gonzalo            | León                  |               45 |
| Juan               | Lopez                 |               45 |
| Beatriz            | Gil                   |               44 |
| Elena              | Jiménez               |               42 |
| Víctor             | Delgado               |               41 |
| Patricia           | Torres                |               40 |
| Jorge              | Castro                |               39 |
| Carmen             | Ruiz                  |               38 |
| Rocío              | Cabrera               |               37 |
| Isabel             | Romero                |               36 |
| Héctor             | Santos                |               35 |
| Ana                | Sánchez               |               34 |
| Sergio             | Álvarez               |               33 |
| Noelia             | Cano                  |               33 |
| Silvia             | Molina                |               32 |
| David              | Navarro               |               31 |
| Cristina           | Vázquez               |               30 |
| María              | Gómez                 |               29 |
| Marta              | Peña                  |               28 |
| Rubén              | Ramos                 |               28 |
| Pablo              | Hernández             |               27 |
| Irene              | Serrano               |               27 |
| Natalia            | Ortiz                 |               26 |
| Laura              | Moreno                |               25 |
| Lucía              | Iglesias              |               24 |
+--------------------+-----------------------+------------------+
```

---
2. Selección de solo algunas columnas
```
SELECT 
    nombre,
    apellidos
FROM 
    clientes;
```

En esta consulta se seleccionan únicamente las columnas nombre y apellidos de la tabla clientes. Esto permite mostrar solo la información relevante, reduciendo la cantidad de datos presentados y optimizando la lectura de los resultados.

```
+----------+------------+
| nombre   | apellidos  |
+----------+------------+
| Juan     | Lopez      |
| Javier   | Martinez   |
| Ana      | Sánchez    |
| María    | Gómez      |
| Luis     | Fernández  |
| Carmen   | Ruiz       |
| Pablo    | Hernández  |
| Elena    | Jiménez    |
| Sergio   | Álvarez    |
| Laura    | Moreno     |
| Raúl     | Muñoz      |
| Isabel   | Romero     |
| David    | Navarro    |
| Patricia | Torres     |
| Alberto  | Domínguez  |
| Cristina | Vázquez    |
| Rubén    | Ramos      |
| Beatriz  | Gil        |
| Jorge    | Castro     |
| Natalia  | Ortiz      |
| Óscar    | Rubio      |
| Silvia   | Molina     |
| Víctor   | Delgado    |
| Rocío    | Cabrera    |
| Héctor   | Santos     |
| Lucía    | Iglesias   |
| Andrés   | Cortés     |
| Marta    | Peña       |
| Tomás    | Flores     |
| Noelia   | Cano       |
| Gonzalo  | León       |
| Irene    | Serrano    |
+----------+------------+
```

---
3. Nombrar columnas al seleccionar
```
SELECT 
    nombre AS 'Nombre del cliente',
    apellidos AS 'Apellidos del cliente',
    edad AS 'Edad del cliente'
FROM 
    clientes;
```

Esta consulta muestra los mismos campos que la anterior (y añade la muestra de la edad pero con su alias), pero añade alias mediante la cláusula AS, lo que permite personalizar los nombres de las columnas en el resultado, haciendo la información más clara y comprensible para el usuario final.

Como resultado de estas consultas, se obtiene una tabla organizada y clara que muestra los datos de los clientes según los criterios establecidos que sean requeridos, ya sea filtrando columnas, ordenando por edad o renombrando los campos para mejorar la presentación.

```
+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Juan               | Lopez                 |               45 |
| Javier             | Martinez              |               46 |
| Ana                | Sánchez               |               34 |
| María              | Gómez                 |               29 |
| Luis               | Fernández             |               51 |
| Carmen             | Ruiz                  |               38 |
| Pablo              | Hernández             |               27 |
| Elena              | Jiménez               |               42 |
| Sergio             | Álvarez               |               33 |
| Laura              | Moreno                |               25 |
| Raúl               | Muñoz                 |               48 |
| Isabel             | Romero                |               36 |
| David              | Navarro               |               31 |
| Patricia           | Torres                |               40 |
| Alberto            | Domínguez             |               53 |
| Cristina           | Vázquez               |               30 |
| Rubén              | Ramos                 |               28 |
| Beatriz            | Gil                   |               44 |
| Jorge              | Castro                |               39 |
| Natalia            | Ortiz                 |               26 |
| Óscar              | Rubio                 |               50 |
| Silvia             | Molina                |               32 |
| Víctor             | Delgado               |               41 |
| Rocío              | Cabrera               |               37 |
| Héctor             | Santos                |               35 |
| Lucía              | Iglesias              |               24 |
| Andrés             | Cortés                |               47 |
| Marta              | Peña                  |               28 |
| Tomás              | Flores                |               52 |
| Noelia             | Cano                  |               33 |
| Gonzalo            | León                  |               45 |
| Irene              | Serrano               |               27 |
+--------------------+-----------------------+------------------+
```

---
Este ejercicio permite aplicar de forma práctica los conceptos básicos de consulta en bases de datos mediante SQL, como la selección de columnas específicas, la ordenación de registros en orden descendente y la personalización de los nombres de los campos utilizando alias. Estas operaciones resultan fundamentales para la organización y presentación eficiente de la información, facilitando su análisis y comprensión. Además, este tipo de ejercicios contribuye al desarrollo del pensamiento lógico y estructurado necesario para trabajar con bases de datos más complejas, sentando las bases para el uso de consultas avanzadas y optimización de sistemas de información.
