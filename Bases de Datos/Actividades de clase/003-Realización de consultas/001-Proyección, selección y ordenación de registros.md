El presente ejercicio se centra en el uso del lenguaje SQL como herramienta fundamental para la gestión y consulta de bases de datos, específicamente en la aplicación de conceptos como la selección de columnas, la ordenación de registros y la personalización de los nombres de los campos mostrados en los resultados. SQL permite interactuar con bases de datos relacionales mediante instrucciones que facilitan la recuperación, organización y presentación de la información almacenada. En este contexto, se trabaja con una tabla llamada clientes y se aplican cláusulas como SELECT, FROM, ORDER BY y AS, cuyo propósito es filtrar los datos necesarios, ordenarlos en función de un criterio específico y mostrar los resultados con nombres de columnas personalizados, con el objetivo de mejorar la comprensión y presentación de la información obtenida.

En esta actividad se utilizan diferentes consultas SQL para practicar tres conceptos fundamentales: la ordenación descendente de datos, la selección de columnas específicas y el uso de alias para nombrar columnas en los resultados.

En primer lugar, se trabaja la ordenación descendente mediante la cláusula ORDER BY acompañada de la palabra clave DESC, la cual permite ordenar los registros de una tabla desde el valor más alto al más bajo según el campo indicado. En este caso, se utiliza el campo edad para mostrar a los clientes desde el mayor hasta el menor.

En segundo lugar, se aborda la selección de columnas específicas utilizando la instrucción SELECT, que permite indicar únicamente los campos que se desean mostrar en la consulta, evitando así mostrar información innecesaria.

Por último, se emplea la cláusula AS para asignar alias a las columnas, lo que permite personalizar los nombres que aparecen en el resultado de la consulta, facilitando su lectura e interpretación.

A continuación, se presentan las consultas SQL utilizadas en el ejercicio, junto con su explicación.

1. Ordenación descendente por edad
SELECT 
    nombre AS 'Nombre del cliente',
    apellidos AS 'Apellidos del cliente',
    edad AS 'Edad del cliente'
FROM 
    clientes
ORDER BY
    edad DESC;


Esta consulta selecciona los campos nombre, apellidos y edad de la tabla clientes. Mediante la cláusula AS, se renombran las columnas para que aparezcan con un formato más descriptivo en el resultado. Posteriormente, se utiliza ORDER BY edad DESC para ordenar los registros desde el cliente de mayor edad hasta el de menor edad.

2. Selección de solo algunas columnas
SELECT 
    nombre,
    apellidos
FROM 
    clientes;

En esta consulta se seleccionan únicamente las columnas nombre y apellidos de la tabla clientes. Esto permite mostrar solo la información relevante, reduciendo la cantidad de datos presentados y optimizando la lectura de los resultados.

3. Nombrar columnas al seleccionar
SELECT 
    nombre AS 'Nombre del cliente',
    apellidos AS 'Apellidos del cliente',
    edad AS 'Edad del cliente'
FROM 
    clientes;

Esta consulta muestra los mismos campos que la anterior, pero añade alias mediante la cláusula AS, lo que permite personalizar los nombres de las columnas en el resultado, haciendo la información más clara y comprensible para el usuario final.

Como resultado de estas consultas, se obtiene una tabla organizada y clara que muestra los datos de los clientes según los criterios establecidos, ya sea filtrando columnas, ordenando por edad o renombrando los campos para mejorar la presentación.

Un error frecuente es olvidar la cláusula DESC, lo que provocaría que los datos se ordenen de forma ascendente por defecto. Otro error habitual es escribir incorrectamente el nombre de la tabla o de las columnas, lo que generaría errores de sintaxis. Para evitar estos problemas, es importante verificar los nombres de los campos y respetar la estructura correcta de la consulta SQL.

En conclusión, este ejercicio permite aplicar de forma práctica los conceptos básicos de consulta en bases de datos mediante SQL, como la selección de columnas específicas, la ordenación de registros en orden descendente y la personalización de los nombres de los campos utilizando alias. Estas operaciones resultan fundamentales para la organización y presentación eficiente de la información, facilitando su análisis y comprensión. Además, este tipo de ejercicios contribuye al desarrollo del pensamiento lógico y estructurado necesario para trabajar con bases de datos más complejas, sentando las bases para el uso de consultas avanzadas y optimización de sistemas de información.
