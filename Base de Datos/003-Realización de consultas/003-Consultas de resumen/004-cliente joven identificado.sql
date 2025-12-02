-- sudo mysql -u root -p

USE clientes;

SELECT
nombre,
apellidos,
edad
FROM clientes
ORDER BY edad ASC
LIMIT 1;

+--------+-----------+------+
| nombre | apellidos | edad |
+--------+-----------+------+
| Lucía  | Iglesias  |   24 |
+--------+-----------+------+

