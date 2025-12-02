-- sudo mysql -u root -p

USE clientes;

SELECT
	AVG(edad)
FROM clientes;

+-----------+
| AVG(edad) |
+-----------+
|   37.3750 |
+-----------+

