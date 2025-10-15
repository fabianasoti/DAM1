sudo mysql -u root -p


SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| empresadam         |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0,03 sec)

USE empresadam;
mysql> USE empresadam;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A


SHOW TABLES;
mysql> SHOW TABLES;
+----------------------+
| Tables_in_empresadam |
+----------------------+
| clientes             |
+----------------------+
1 row in set (0,00 sec)


DESCRIBE clientes;
mysql> DESCRIBE clientes;
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

SELECT * FROM clientes;
mysql> SELECT * FROM clientes;
+---------------+-----------+------------------+-----------+---------------------+
| identificador | dni       | nombre           | apellidos | email               |
+---------------+-----------+------------------+-----------+---------------------+
|             1 | 12345678M | Fabiana Victoria | Sotillo   | fabiana@sotillo.com |
|             2 | 14567895A | Susana Banana    | Perez     | susana@perez.com    |
|             3 | 14567895A | Susana Banana    | Perez     | correoincorrecto    |
+---------------+-----------+------------------+-----------+---------------------+
3 rows in set (0,01 sec)

INSERT INTO clientes VALUES(
	NULL,
	'12345678M',
	'nombre del cliente',
	'apellidos del cliente',
	'algo'
);
Query OK, 1 row affected (0,04 sec)


SELECT * FROM clientes;
+---------------+-----------+--------------------+-----------------------+---------------------+
| identificador | dni       | nombre             | apellidos             | email               |
+---------------+-----------+--------------------+-----------------------+---------------------+
|             1 | 12345678M | Fabiana Victoria   | Sotillo               | fabiana@sotillo.com |
|             2 | 14567895A | Susana Banana      | Perez                 | susana@perez.com    |
|             3 | 14567895A | Susana Banana      | Perez                 | correoincorrecto    |
|             4 | 12345678M | nombre del cliente | apellidos del cliente | algo                |
+---------------+-----------+--------------------+-----------------------+---------------------+
4 rows in set (0,00 sec)


