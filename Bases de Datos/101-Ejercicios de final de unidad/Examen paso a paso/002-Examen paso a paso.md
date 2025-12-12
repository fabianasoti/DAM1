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
	id_autor VARCHAR(100)
	contenido TEXT,
	PRIMARY KEY
);































