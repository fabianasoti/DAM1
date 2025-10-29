En las bases de datos relacionales, es necesario realizar acciones básicas que permitan almacenar, organizar y administrar información de manera estructurada mediante tablas compuestas por filas y columnas. Esto funciona bajo un modelo cliente-servidor y utiliza SQL (Structured Query Language) para interactuar con los datos.

El objetivo de este ejercicio es practicar la aplicación del CRUD; la creación y selección de una base de datos y la práctica de operaciones fundamentales de manipulación de datos, conocidas como CRUD (Create, Read, Update, Delete). Mediante la creación de la tabla clientes, la inserción, lectura, actualización y eliminación de registros, se busca comprender cómo se gestionan los datos de manera eficiente y cómo se aplican los conceptos de tipos de datos y restricciones en un entorno relacional.


- Inicialmente se selecciona la base de datos con la que se quiere trabajar:
```
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| ejemploclaves      |
| empresadam         |
| funbiana           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
7 rows in set (0,01 sec)

mysql> USE funbiana;

Database changed
```

- Una vez dentro, se crea la tabla clientes definiendo el tipo de campo de cada uno, de esta manera, aplicamos la C  (Create) del CRUD, Creando una nueva tabla:
```
mysql> CREATE TABLE clientes (
    ->   dni VARCHAR(9),
    ->   nombre VARCHAR(50),
    ->   apellidos VARCHAR(255),
    ->   email VARCHAR(100)
    -> );
Query OK, 0 rows affected (0,04 sec)
```

- Se inserta un cliente siguiendo la plantilla de la tabla anterior.
```
mysql> INSERT INTO clientes VALUES(
    ->   '12345678Z',
    ->   'Fabiana Victoria',
    ->   'Sotillo',
    ->   'info@fabiana.com'
    -> );
Query OK, 1 row affected (0,04 sec)
```

- Para ilustrar la R (Read) del CRUD, se hace uso del  "SELECT * FROM clientes;", y de esta manera se muestran en pantalla la lista de clientes que se ha ingresado hasta el momento.
```
mysql> SELECT * FROM clientes;
+-----------+------------------+-----------+------------------+
| dni       | nombre           | apellidos | email            |
+-----------+------------------+-----------+------------------+
| 12345678Z | Fabiana Victoria | Sotillo   | info@fabiana.com |
+-----------+------------------+-----------+------------------+
1 row in set (0,00 sec)
```

- Para actualizar un dato de la tabla clientes, y aplicar la U (Update) del CRUD, se utiliza:
```
mysql> UPDATE clientes
    -> SET dni = '11111111A'
    -> WHERE nombre = 'Fabiana Victoria';
Query OK, 1 row affected (0,02 sec)
```
Donde, junto con el comando UPDATE, se indica el nombre de la tabla a modificar,  con SET se añade el dato que se quiere cambiar "dni = '11111111A'", y se identifica la fila que se quiere actualizar con WHERE.

Luego, al mostrar los clientes nuevamente, se puede evidenciar que el dato seleccionado (dni), efectivamente se ha actualizado.
```
Rows matched: 1  Changed: 1  Warnings: 0
mysql> SELECT * FROM clientes;
+-----------+------------------+-----------+------------------+
| dni       | nombre           | apellidos | email            |
+-----------+------------------+-----------+------------------+
| 11111111A | Fabiana Victoria | Sotillo   | info@fabiana.com |
+-----------+------------------+-----------+------------------+
1 row in set (0,00 sec)
```

- Finalmente, para ejemplificar la D (Delete) del CRUD, se utiliza el comando DELETE, seguido de la tabla donde se quiere eliminar el dato, y usando el WHERE para identificar la fila que se quiere eliminar. 
```
mysql> DELETE FROM clientes
    -> WHERE dni = '11111111A';
Query OK, 1 row affected (0,02 sec)
```
En este caso, como solo se ha eliminado la única instancia que se tenía en la tabla, esta queda vacía, es por eso que al intentar leer la tabla, esta se muestra como "empty set"
```
mysql> SELECT * FROM clientes;
Empty set (0,00 sec)
```


A continuación, en el siguiente bloque, se muestra la actividad en consola:
```
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| ejemploclaves      |
| empresadam         |
| funbiana           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
7 rows in set (0,01 sec)

mysql> USE funbiana;

Database changed
mysql> CREATE TABLE clientes (
    ->   dni VARCHAR(9),
    ->   nombre VARCHAR(50),
    ->   apellidos VARCHAR(255),
    ->   email VARCHAR(100)
    -> );
Query OK, 0 rows affected (0,04 sec)

mysql> INSERT INTO clientes VALUES(
    ->   '12345678Z',
    ->   'Fabiana Victoria',
    ->   'Sotillo',
    ->   'info@fabiana.com'
    -> );
Query OK, 1 row affected (0,04 sec)

mysql> SELECT * FROM clientes;
+-----------+------------------+-----------+------------------+
| dni       | nombre           | apellidos | email            |
+-----------+------------------+-----------+------------------+
| 12345678Z | Fabiana Victoria | Sotillo   | info@fabiana.com |
+-----------+------------------+-----------+------------------+
1 row in set (0,00 sec)

mysql> UPDATE clientes
    -> SET dni = '11111111A'
    -> WHERE nombre = 'Fabiana Victoria';
Query OK, 1 row affected (0,02 sec)
Rows matched: 1  Changed: 1  Warnings: 0
mysql> SELECT * FROM clientes;
+-----------+------------------+-----------+------------------+
| dni       | nombre           | apellidos | email            |
+-----------+------------------+-----------+------------------+
| 11111111A | Fabiana Victoria | Sotillo   | info@fabiana.com |
+-----------+------------------+-----------+------------------+
1 row in set (0,00 sec)

mysql> UPDATE clientes
    -> SET apellidos = 'Sotillo Cuevas'
    -> WHERE nombre = 'Fabiana Victoria';
Query OK, 1 row affected (0,02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM clientes;
+-----------+------------------+----------------+------------------+
| dni       | nombre           | apellidos      | email            |
+-----------+------------------+----------------+------------------+
| 11111111A | Fabiana Victoria | Sotillo Cuevas | info@fabiana.com |
+-----------+------------------+----------------+------------------+
1 row in set (0,00 sec)

mysql> DELETE FROM clientes
    -> WHERE dni = '11111111A';
Query OK, 1 row affected (0,02 sec)

mysql> SELECT * FROM clientes;
Empty set (0,00 sec)
```

Este ejercicio permitió practicar y comprender las operaciones fundamentales del CRUD (Create, Read, Update, Delete) en una base de datos relacional utilizando MySQL. A través de la creación de la tabla clientes, se ha practicado la inserción, lectura, actualización y eliminación de datos, además de haberse evidenciado cómo se manipula la información de manera estructurada y segura.

La práctica consolida la comprensión sobre la importancia de definir correctamente los tipos de datos y cómo cada operación CRUD afecta la tabla, evidenciando cada uno de sus cambios, asegurando integridad y consistencia de los datos. Además, proporcionó experiencia práctica en el uso de comandos SQL esenciales, sentando una base sólida para desarrollar aplicaciones que requieran gestión dinámica de información.

