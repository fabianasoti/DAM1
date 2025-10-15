INSERT INTO clientes VALUES(
	NULL,
	'12345678Z',
	'Fabiana Victoria',
	'Sotillo',
	'info@fa.com'
);

Query OK, 1 row affected (0,02 sec)

SELECT * FROM clientes;
+---------------+-----------+------------------+-----------+-------------+
| identificador | dni       | nombre           | apellidos | email       |
+---------------+-----------+------------------+-----------+-------------+
|             5 | 12345678Z | Fabiana Victoria | Sotillo   | info@fa.com |
+---------------+-----------+------------------+-----------+-------------+
1 row in set (0,00 sec)


