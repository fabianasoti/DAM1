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
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

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

