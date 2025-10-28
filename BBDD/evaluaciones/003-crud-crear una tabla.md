sudo mysql -u root -p
[sudo] contraseña para fabiana: 
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.43-0ubuntu0.24.04.2 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

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

