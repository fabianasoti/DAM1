-- sudo mysql -u root -p

USE clientes;

SELECT
	ROUND(AVG(edad))
FROM clientes;
+------------------+
| ROUND(AVG(edad)) |
+------------------+
|               37 |
+------------------+

SELECT
	FLOOR(AVG(edad))
FROM clientes;
+------------------+
| FLOOR(AVG(edad)) |
+------------------+
|               37 |
+------------------+


SELECT
	CEIL(AVG(edad))
FROM clientes;
+-----------------+
| CEIL(AVG(edad)) |
+-----------------+
|              38 |
+-----------------+

