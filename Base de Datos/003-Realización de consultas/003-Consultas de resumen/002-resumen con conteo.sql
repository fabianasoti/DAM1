-- sudo mysql -u root -p

USE clientes;

SELECT
COUNT(nombre)
FROM clientes;
+---------------+
| COUNT(nombre) |
+---------------+
|            32 |
+---------------+

