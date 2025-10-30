-- create
INSERT INTO clientes VALUES(
	NULL,
	'Fabiana Victoria',
	'Sotillo',
	'info@fabiana.com'
);

-- read
SELECT * FROM clientes;

-- update
UPDATE clientes
SET email = 'info@sotillo.com'
WHERE Identificador = 1;

-- delete
DELETE FROM clientes
WHERE Identificador = 1;
