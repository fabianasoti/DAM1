```
'''
Base de datos biblioteca25
v0.1 Fabiana Sotillo
Base de datos con tablas relacionadas, aplicando claves primarias, 
foráneas, restricciones CHECK y UNIQUE, y valores por defecto
'''
```
---
Las bases de datos relacionales se basan en el modelo, donde la información se organiza en tablas relacionadas entre sí mediante campos comunes llamados claves.

SQL (Structured Query Language) es un lenguaje diseñado para crear, administrar y manipular bases de datos relacionales. Permite definir estructuras (tablas), insertar y consultar datos,

El objetivo de este ejercicio es crear una base de datos relacional en MySQL para gestionar una biblioteca, aplicando correctamente conceptos de modelado de datos, restricciones de integridad y relaciones entre tablas mediante claves primarias y foráneas. 

En este ejercicio se aplican los siguientes conocimientos técnicos, los cuales se ponen en práctica en la creación de la base de datos biblioteca25 y sus tablas correspondientes: autores, libros, socios y prestamos, todas integradas mediante claves foráneas:

- Se crear BD y usarla:
```
mysql> CREATE DATABASE biblioteca25;
Query OK, 1 row affected (0,00 sec)
```

- Se elige la base de datos para trabajar con ella
```
mysql> USE biblioteca25;
Database changed
```

- Se crea la primera tabla con las claves primarias (PRIMARY KEY): identifican de forma única cada fila. Y se usa DESCRIBE para mostrar la tabla y confirmar que está bien construida.
```
mysql> CREATE TABLE autores (
    ->   id INT AUTO_INCREMENT PRIMARY KEY,
    ->   nombre VARCHAR(100) NOT NULL,
    ->   pais VARCHAR(80) NULL
    -> );
		
	DESCRIBE autores;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | NO   |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
		
mysql> CREATE TABLE libros(
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    ->   titulo VARCHAR(20) NOT NULL,
    ->   isbn VARCHAR(255) NOT NULL UNIQUE,
    ->   precio DECIMAL(8,2) NOT NULL,
    ->   autor_id INT NOT NULL
    -> );
	
DESCRIBE libros;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(20)  | NO   |     | NULL    |                |
| isbn     | varchar(255) | NO   | UNI | NULL    |                |
| recio    | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```

- Se crean las claves foráneas (FOREIGN KEY): vinculan datos entre tablas relacionadas.
 ```
 mysql> ALTER TABLE libros
    -> ADD CONSTRAINT fk_libros_autores
    -> FOREIGN KEY (autor_id) 
    -> REFERENCES autores(id)
    -> ON DELETE CASCADE
    -> ON UPDATE CASCADE;
```

- Se aplican restricciones (CHECK, UNIQUE, NOT NULL): garantizan la integridad de los datos. También se aplican valores por defecto (DEFAULT) y auto_increment, que automatizan la inserción de datos.
```
mysql> CREATE TABLE socios(
    ->    id INT AUTO_INCREMENT PRIMARY KEY,
    ->    nombre VARCHAR(100) NOT NULL,
    ->    email VARCHAR(120) NOT NULL UNIQUE,
    ->    fecha_alta DATE NOT NULL DEFAULT (CURRENT_DATE)
    -> );
		
mysql> ALTER TABLE socios
    -> ADD CONSTRAINT comprobar_email
    -> CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'); 
Query OK, 0 rows affected (0,07 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

- Se realizan inserciones dentro de las tablas para poder trabajar con la información en forma de datos, y poder conectar las tablas, por ejemplo:
```
INSERT INTO libros VALUES(
	NULL,
	'Cien años de soledad', 
	'9780307474728', 
	11.99, 
	2
);
Query OK, 1 row affected (0,01 sec)
```

- Y luego si se usa SELECT * FROM libros; se puede mostrar lo que se ha ingresado en la tabla que se seleccione, por ejemplo:
```
SELECT * FROM libros;
+----+-----------------------+----------------+--------+----------+
| id | titulo                | isbn           | precio | autor_id |
+----+-----------------------+----------------+--------+----------+
|  1 | Violeta               | 978-9500720001 |  20.99 |        1 |
|  2 | Cien años de soledad  | 9780307474728  |  11.99 |        2 |
|  3 | Kafka en la orilla    | 9788499082478  |  18.99 |        3 |
+----+-----------------------+----------------+--------+----------+
```

- Se realizan consultas y validaciones: permiten verificar la consistencia del diseño. En este caso se ejemplifica con la verificación de que email sea válido dentro de esta inserción
```
-- Verificación insertar email inválido para que dé error:
INSERT INTO socios VALUES(
	NULL,
	'Susana Santana',
	'algo',
	'31/10/25'
);
ERROR 3819 (HY000): Check constraint 'comprobar_email' is violated.
```

---

A continuación, se muestra todo el bloque de sql trabajado en consola:
```
Base de datos biblioteca25
v0.1 Fabiana Sotillo
Base de datos con tablas relacionadas, aplicando claves primarias, 
foráneas, restricciones CHECK y UNIQUE, y valores por defecto

sudo mysql -u root -p

-- Paso 1: Crear BD y usarla
mysql> CREATE DATABASE biblioteca25;
Query OK, 1 row affected (0,00 sec)

mysql> USE biblioteca25;
Database changed

mysql> SELECT DATABASE();
+--------------+
| DATABASE()   |
+--------------+
| biblioteca25 |
+--------------+
1 row in set (0,00 sec)

-- Paso 2: Crear tabla autores
mysql> CREATE TABLE autores (
    ->   id INT AUTO_INCREMENT PRIMARY KEY,
    ->   nombre VARCHAR(100) NOT NULL,
    ->   pais VARCHAR(80) NULL
    -> );
Query OK, 0 rows affected (0,05 sec)

mysql> DESCRIBE autores;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | NO   |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0,01 sec)


--Paso 3: Crear tabla libros con UNIQUE, CHECK y FK
mysql> CREATE TABLE libros(
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    ->   titulo VARCHAR(20) NOT NULL,
    ->   isbn VARCHAR(255) NOT NULL UNIQUE,
    ->   precio DECIMAL(8,2) NOT NULL,
    ->   autor_id INT NOT NULL
    -> );
Query OK, 0 rows affected (0,07 sec)


mysql> ALTER TABLE libros
    -> ADD CONSTRAINT fk_libros_autores
    -> FOREIGN KEY (autor_id) 
    -> REFERENCES autores(id)
    -> ON DELETE CASCADE
    -> ON UPDATE CASCADE;
Query OK, 0 rows affected (0,11 sec)
Records: 0  Duplicates: 0  Warnings: 0


-- Verificación:
--SHOW INDEX FROM libros; para ver UNIQUE en isbn e índice de titulo.
mysql> SHOW INDEX FROM libros;
+--------+------------+-------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table  | Non_unique | Key_name          | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+--------+------------+-------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| libros |          0 | PRIMARY           |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          0 | isbn              |            1 | isbn        | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| libros |          1 | fk_libros_autores |            1 | autor_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+--------+------------+-------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
3 rows in set (0,03 sec)

-- Como evidencia - DESCRIBE libros;
mysql> DESCRIBE libros;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(20)  | NO   |     | NULL    |                |
| isbn     | varchar(255) | NO   | UNI | NULL    |                |
| recio    | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)


-- Paso 4: Crear tabla socios con UNIQUE y CHECK de email
mysql> CREATE TABLE socios(
    ->    id INT AUTO_INCREMENT PRIMARY KEY,
    ->    nombre VARCHAR(100) NOT NULL,
    ->    email VARCHAR(120) NOT NULL UNIQUE,
    ->    fecha_alta DATE NOT NULL DEFAULT (CURRENT_DATE)
    -> );
Query OK, 0 rows affected (0,05 sec)

-- Se añade el CHECK del email
ALTER TABLE socios
	ADD CONSTRAINT comprobar_email
	CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');
	Query OK, 0 rows affected (0,07 sec)
Records: 0  Duplicates: 0  Warnings: 0

-- Verificación insertar email inválido para que dé error:
INSERT INTO socios VALUES(
	NULL,
	'Susana Santana',
	'algo',
	'31/10/25'
);
ERROR 3819 (HY000): Check constraint 'comprobar_email' is violated.

INSERT INTO socios VALUES(
	NULL,
	'Susana Santana',
	'info@susana.com',
	'31/10/25'
);
Query OK, 1 row affected, 1 warning (0,03 sec)

INSERT INTO socios VALUES(
	NULL,
	'Benito Bonito',
	'info@benito.com',
	'01/06/23'
);
Query OK, 1 row affected, 1 warning (0,02 sec)

-- Se comprueba que se añadieron correctamente
mysql> SELECT * FROM socios;
+----+----------------+-----------------+------------+
| id | nombre         | email           | fecha_alta |
+----+----------------+-----------------+------------+
|  1 | Susana Santana | info@susana.com | 2031-10-25 |
|  2 | Benito Bonito  | info@benito.com | 2001-06-23 |
+----+----------------+-----------------+------------+
2 rows in set (0,01 sec)


-- Paso 5: Crear tabla prestamos con FKs y CHECK de fechas
CREATE TABLE prestamos(
	id INT AUTO_INCREMENT PRIMARY KEY,
	socio_id INT NOT NULL,
	libro_id INT NOT NULL,
	fecha_prestamo DATE NOT NULL DEFAULT (CURRENT_DATE),
	fecha_devolucion DATE NULL,
	CHECK (fecha_devolucion IS NULL OR fecha_devolucion >= fecha_prestamo)
);
Query OK, 0 rows affected (0,05 sec)

-- Se realiza la FK con socio_id y libro_id
ALTER TABLE prestamos
	ADD CONSTRAINT fk_prestamos_socios
	FOREIGN KEY (socio_id) 
	REFERENCES socios(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE;
Query OK, 0 rows affected (0,09 sec)
Records: 0  Duplicates: 0  Warnings: 0

ALTER TABLE prestamos
	ADD CONSTRAINT fk_prestamos_libros
	FOREIGN KEY (libro_id) 
	REFERENCES libros(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE;
Query OK, 0 rows affected (0,13 sec)
Records: 0  Duplicates: 0  Warnings: 0

-- Inserciones a todas las tablas
-- Inserción a autores:
INSERT INTO autores VALUES(
	NULL,
	'Isabel Allende',
	'Chile'
);

INSERT INTO autores VALUES(
	NULL,
	'Gabriel García Márquez',
	'Colombia'
);

INSERT INTO autores VALUES(
	NULL,
	'Haruki Murakami',
	'Japón'
);

mysql> SELECT * FROM autores;
+----+--------------------------+----------+
| id | nombre                   | pais     |
+----+--------------------------+----------+
|  1 | Isabel Allende           | Chile    |
|  2 | Gabriel García Márquez   | Colombia |
|  3 | Haruki Murakami          | Japón    |
+----+--------------------------+----------+
3 rows in set (0,00 sec)

-- Inserción a libros:
INSERT INTO libros VALUES(
	NULL,
	'Violeta', 
	'978-9500720001', 
	20.99, 
	1
);
Query OK, 1 row affected (0,03 sec)

INSERT INTO libros VALUES(
	NULL,
	'Cien años de soledad', 
	'9780307474728', 
	11.99, 
	2
);
Query OK, 1 row affected (0,01 sec)

INSERT INTO libros VALUES(
	NULL,
	'Kafka en la orilla', 
	'9788499082478', 
	18.99, 
	3
);
Query OK, 1 row affected (0,04 sec)

mysql> SELECT * FROM libros;
+----+-----------------------+----------------+--------+----------+
| id | titulo                | isbn           | precio | autor_id |
+----+-----------------------+----------------+--------+----------+
|  1 | Violeta               | 978-9500720001 |  20.99 |        1 |
|  2 | Cien años de soledad  | 9780307474728  |  11.99 |        2 |
|  3 | Kafka en la orilla    | 9788499082478  |  18.99 |        3 |
+----+-----------------------+----------------+--------+----------+
3 rows in set (0,01 sec)

-- Prueba 2 inserciones a prestamos:
-- un préstamo activo (sin fecha_devolucion)
INSERT INTO prestamos VALUES(
	NULL,
	1, 
	1,
	'2025-10-20', 
	NULL
);
Query OK, 1 row affected (0,03 sec)

-- un préstamo devuelto (fecha_devolucion ≥ fecha_prestamo).
INSERT INTO prestamos VALUES(
	NULL,
	2, 
	1,
	'2025-10-20', 
	'2025-10-25'
);
Query OK, 1 row affected (0,01 sec)

-- Intenta un préstamo con fecha_devolucion anterior: debe fallar.
INSERT INTO prestamos VALUES(
	NULL,
	3, 
	1,
	'2025-10-20', 
	'2025-10-19'
);
ERROR 3819 (HY000): Check constraint 'prestamos_chk_1' is violated.

-- Verificación:
mysql> DESCRIBE prestamos;
+------------------+------+------+-----+-----------+-------------------+
| Field            | Type | Null | Key | Default   | Extra             |
+------------------+------+------+-----+-----------+-------------------+
| id               | int  | NO   | PRI | NULL      | auto_increment    |
| socio_id         | int  | NO   | MUL | NULL      |                   |
| libro_id         | int  | NO   | MUL | NULL      |                   |
| fecha_prestamo   | date | NO   |     | curdate() | DEFAULT_GENERATED |
| fecha_devolucion | date | YES  |     | NULL      |                   |
+------------------+------+------+-----+-----------+-------------------+
5 rows in set (0,00 sec)

mysql> SHOW INDEX FROM prestamos;
+-----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table     | Non_unique | Key_name            | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+-----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| prestamos |          0 | PRIMARY             |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | fk_prestamos_socios |            1 | socio_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| prestamos |          1 | fk_prestamos_libros |            1 | libro_id    | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
+-----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
3 rows in set (0,00 sec)

-- Resumen de comprobaciones finales
mysql> SHOW TABLES;
+------------------------+
| Tables_in_biblioteca25 |
+------------------------+
| autores                |
| libros                 |
| prestamos              |
| socios                 |
+------------------------+
4 rows in set (0,00 sec)

mysql> DESCRIBE autores;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | NO   |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0,00 sec)

mysql> DESCRIBE libros;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(20)  | NO   |     | NULL    |                |
| isbn     | varchar(255) | NO   | UNI | NULL    |                |
| precio   | decimal(8,2) | NO   |     | NULL    |                |
| autor_id | int          | NO   | MUL | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)

mysql> DESCRIBE socios;
+------------+--------------+------+-----+-----------+-------------------+
| Field      | Type         | Null | Key | Default   | Extra             |
+------------+--------------+------+-----+-----------+-------------------+
| id         | int          | NO   | PRI | NULL      | auto_increment    |
| nombre     | varchar(100) | NO   |     | NULL      |                   |
| email      | varchar(120) | NO   | UNI | NULL      |                   |
| fecha_alta | date         | NO   |     | curdate() | DEFAULT_GENERATED |
+------------+--------------+------+-----+-----------+-------------------+
4 rows in set (0,00 sec)
```

---
En este ejercicio se aplicaron los principios fundamentales del diseño de bases de datos relacionales y del uso de SQL como lenguaje estructurado para gestionar datos.

Se implementaron cuatro tablas relacionadas, aplicando claves primarias, foráneas, restricciones CHECK y UNIQUE, y valores por defecto, asegurando la integridad de la información en cada operación.

El modelo final de la base de datos biblioteca25 demuestra cómo SQL permite estructurar información de manera coherente y bien organizada, evitando la redundancia de datos y manteniendo el orden de la información de manera cosistente.
