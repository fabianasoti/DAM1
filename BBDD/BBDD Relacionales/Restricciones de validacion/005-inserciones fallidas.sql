INSERT INTO clientes VALUES(
	NULL,
	'12345678A',
	'Fabiana Victoria',
	'Sotillo',
	'info@fa.com'
);

ERROR 3819 (HY000): Check constraint 'comprobar_dni_nie_letra' is violated


INSERT INTO clientes VALUES(
	NULL,
	'12345678Z',
	'Fabiana Victoria',
	'Sotillo',
	'correoincorrecto'
);

ERROR 3819 (HY000): Check constraint 'comprobar_email' is violated.

