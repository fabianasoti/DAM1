-- Create --
INSERT INTO clientes VALUES(
	'12345678A',
	'Fabiana Victoria',
	'Sotillo Cuevas',
	'info@sotillo.com'
);
Query OK, 1 row affected (0,03 sec)

-- Read

SELECT * FROM clientes;
+-----------+------------------+----------------+------------------+
| dni       | nombre           | apellidos      | email            |
+-----------+------------------+----------------+------------------+
| 12345678A | Fabiana Victoria | Sotillo Cuevas | info@sotillo.com |
+-----------+------------------+----------------+------------------+
1 row in set (0,00 sec)


-- Update

UPDATE clientes
SET dni = '99999999C'
WHERE nombre = 'Fabiana Victoria';

Query OK, 1 row affected (0,03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

-- Delete

DELETE FROM clientes
WHERE dni = '99999999C';

Query OK, 1 row affected (0,01 sec)

-- Ahora si chequeo mis clientes:

SELECT * FROM clientes;
Empty set (0,00 sec)

