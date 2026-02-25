SET @nombre = 'Fabiana Victoria';
SET @apellidos = 'Sotillo';
SET @email = 'info@fabiana.com';
SET @direccion = 'La calle de Fabiana';

INSERT INTO clientes(
    nombre,
    apellidos,
    email,
    direccion
)
VALUES(
    @nombre,
    @apellidos,
    @email,
    @direccion
);
