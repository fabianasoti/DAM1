DELETE FROM clientes;
Query OK, 1 row affected (0,02 sec)

INSERT INTO clientes VALUES(
	NULL,
	'12345678Z',
	'Fabiana Victoria',
	'Sotillo Cuevas',
	'info@fa.com'
);
Query OK, 1 row affected (0,02 sec)

SELECT * FROM clientes;
+---------------+-----------+------------------+----------------+-------------+
| identificador | dni       | nombre           | apellidos      | email       |
+---------------+-----------+------------------+----------------+-------------+
|             6 | 12345678Z | Fabiana Victoria | Sotillo Cuevas | info@fa.com |
+---------------+-----------+------------------+----------------+-------------+
1 row in set (0,00 sec)

TRUNCATE TABLE clientes; -- resetea la tabla pero no se la carga

INSERT INTO clientes VALUES( --ya volvemos a ingresar al cliente
	NULL,
	'12345678Z',
	'Fabiana Victoria',
	'Sotillo Cuevas',
	'info@fa.com'
);

SELECT * FROM clientes; 

DROP TABLE clientes; -- mucho mucho cuidado porque esto borra la tabla

