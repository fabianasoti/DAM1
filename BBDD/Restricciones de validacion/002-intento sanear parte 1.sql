ALTER TABLE clientes
	ADD CONSTRAINT comprobar_email
	CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');
ERROR 3819 (HY000): Check constraint 'comprobar_email' is violated.

-- Eliminamos registros que no cumplen

DELETE FROM clientes WHERE identificador = 3;
DELETE FROM clientes WHERE identificador = 4;
Query OK, 1 row affected (0,01 sec)

-- Ahora sí aplicamos

SELECT * FROM clientes;

ALTER TABLE clientes
	ADD CONSTRAINT comprobar_email
	CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');

Query OK, 2 rows affected (0,09 sec)
Records: 2  Duplicates: 0  Warnings: 0
