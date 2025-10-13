ALTER TABLE clientes
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
Query OK, 0 rows affected (0,06 sec)
Records: 0  Duplicates: 0  Warnings: 0


ALTER = Altera
TABLE = Tabla
clientes = La tabla que quiero alterar
ADD = la operación que quiero realizar
COLUMN = Quiero añadir una columna
identificador = es el nombre de la columna que quiero añadir
INT = el tipo de dato de la columna (entero)
AUTO_INCREMENT = el numero va a crecer automáticamente
PRIMARY KEY = Clave primaria
FIRST = si hay varias, esta tiene la preferencia

DESCRIBE clientes;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| identificador | int          | NO   | PRI | NULL    | auto_increment |
| dni           | varchar(9)   | YES  |     | NULL    |                |
| nombre        | varchar(50)  | YES  |     | NULL    |                |
| apellidos     | varchar(255) | YES  |     | NULL    |                |
| email         | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
5 rows in set (0,01 sec)

INSERT INTO clientes
VALUES(
	NULL,
	'12345678M',
	'Fabiana Victoria',
	'Sotillo',
	'fabiana@sotillo.com'
);
Query OK, 1 row affected (0,02 sec)

SELECT * FROM clientes;
+---------------+-----------+------------------+-----------+---------------------+
| identificador | dni       | nombre           | apellidos | email               |
+---------------+-----------+------------------+-----------+---------------------+
|             1 | 12345678M | Fabiana Victoria | Sotillo   | fabiana@sotillo.com |
+---------------+-----------+------------------+-----------+---------------------+
1 row in set (0,00 sec)

INSERT INTO clientes
VALUES(
	NULL,
	'14567895A',
	'Susana Banana',
	'Perez',
	'susana@perez.com'
);
Query OK, 1 row affected (0,02 sec)

SELECT * FROM clientes;
+---------------+-----------+------------------+-----------+---------------------+
| identificador | dni       | nombre           | apellidos | email               |
+---------------+-----------+------------------+-----------+---------------------+
|             1 | 12345678M | Fabiana Victoria | Sotillo   | fabiana@sotillo.com |
|             2 | 14567895A | Susana Banana    | Perez     | susana@perez.com    |
+---------------+-----------+------------------+-----------+---------------------+
2 rows in set (0,00 sec)


Ejemplo: casos en los que nos interesa intervenir el orden incrementado; facturas.
Igual no se recomienda. Hay que dejar que la base de datos controle los id. Esa es la idea de tener una base de datos.
20260001


Próxima clase: Validaciones para que la base de datos pueda decir que el correo es incorrecto, por ejemplo.
INSERT INTO clientes
VALUES(
	NULL,
	'14567895A',
	'Susana Banana',
	'Perez',
	'correoincorrecto'
);

mysql> SELECT * FROM clientes;
+---------------+-----------+------------------+-----------+---------------------+
| identificador | dni       | nombre           | apellidos | email               |
+---------------+-----------+------------------+-----------+---------------------+
|             1 | 12345678M | Fabiana Victoria | Sotillo   | fabiana@sotillo.com |
|             2 | 14567895A | Susana Banana    | Perez     | susana@perez.com    |
|             3 | 14567895A | Susana Banana    | Perez     | correoincorrecto    |
+---------------+-----------+------------------+-----------+---------------------+

mysql> EXIT;
Bye

