Iniciando sesión en MySQL
sudo mysql -u root -p

Creo la base de datos 
CREATE DATABASE blog2;

Nos aseguramos de que se ha creado:
SHOW DATABASES;

Nos tenemos que meter en la base de datos 
USE blog2;

Creamos una tabla
CREATE TABLE autores(
	Identificador INT(10),
	nombre VARCHAR(100),
	apellidos VARCHAR(100),
	email VARCHAR(100)
);

O bien con PRIMARY KEY desde el principio
opción 1:
CREATE TABLE autores(
	Identificador INT AUTO_INCREMENT PRIMARY KEY(255),
	nombre VARCHAR(100),
	apellidos VARCHAR(100),
	email VARCHAR(100)
);

opción 2:
CREATE TABLE autores(
	Identificador INT AUTO_INCREMENT(255),
	nombre VARCHAR(100),
	apellidos VARCHAR(100),
	email VARCHAR(100),
	PRIMARY KEY (Identificador),
);

O bien sin identificador para crearla en el futuro:
CREATE TABLE autores(
	nombre VARCHAR(100),
	apellidos VARCHAR(100),
	email VARCHAR(100)
);


Miramos que hemos creado bien
SHOW TABLES;

Quiero tirar la columna Identificador para crearla bien
ALTER TABLE autores DROP Identificador;

Ahora creo columna
ALTER TABLE autores ADD COLUMN Identificador INT auto_increment PRIMARY KEY FIRST;

Vamos a ver qué es lo que se ha hecho
DESCRIBE autores;

Ahora quiero insertar un autr de prueba:
INSERT INTO autores VALUES(
	NULL,
	'Fabiana',
	'Sotillo',
	'info@fabiana.com'
);

Me aseguro:
SELECT * FROM autores;

Creamos una tabla entradas:
CREATE TABLE entradas(
	Identificador INT AUTO_INCREMENT,
	titulo VARCHAR(100),
	fecha VARCHAR(100),
	imagen VARCHAR(100)
	id_autor VARCHAR(100)							-- Esto dará error, habrá que convertir a INT más adelante
	contenido TEXT,
	PRIMARY KEY (Identificador)
);

Comprobamos la existencia de la tabla:
SHOW TABLES;

Describimos:
DESCRIBE entradas;

Creamos una foreign key:
ALTER TABLE entradas
	ADD CONSTRAINT autores_a_entradas
	FOREIGN KEY (id_autor) 
	REFERENCES autores(Identificador)
	ON DELETE CASCADE
	ON UPDATE CASCADE;

Cambiamos tipo de datos
ALTER TABLE entradas
MODIFY COLUMN id_autor INT;

Insertamos una entrada
INSERT INTO entradas VALUES(
	NULL,
	'Título de la primera entrada',
	'2025-11-03',
	'imagen.jpg',
	1,
	'Este es el contenido de la primera entrada'
);

Verificamos:
SELECT * FROM entradas;

Petición cruzada:
SELECT 
entradas.titulo,entradas.fecha,entradas.imagen,entradas.contenido,autores.nombre,autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;

Por último creamos una vista:
CREATE VIEW vista_entrada AS
SELECT 
entradas.titulo,entradas.fecha,entradas.imagen,entradas.contenido,autores.nombre,autores.apellidos
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;

SELECT * FROM vista_entradas;			--Se comporta como una tabla solo para leerla, mostrarla (no funciona con el UPDATE-DELETE)



























