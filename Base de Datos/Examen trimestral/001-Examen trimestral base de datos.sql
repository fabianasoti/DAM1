-- sudo mysql -u root -p

-- Se crea la base de datos portafolioexamen
CREATE DATABASE portafolioexamen;

-- Se comprueba su correcta creación
SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| biblioteca25       |
| ejemploclaves      |
| empresadam         |
| funbiana           |
| information_schema |
| mysql              |
| performance_schema |
| portafolio         |
| portafolioexamen   |
| sys                |
+--------------------+

-- Se selecciona la base de datos
USE portafolioexamen;

-- Se crean dos tablas, 
-- piezasportafolio (Identificador,titulo,descripcion,fecha,id_categoria)
CREATE TABLE piezasportafolio(
	Identificador INT AUTO_INCREMENT,
	titulo VARCHAR(100),
	descripcion VARCHAR(100),
	fecha VARCHAR(100),
	id_categoria INT(100),							
	PRIMARY KEY (Identificador)
);

-- Se comprueba que se  ha creado correctamente con su clave primaria
DESCRIBE piezasportafolio;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripcion   | varchar(100) | YES  |     | NULL    |                |
| fecha         | varchar(100) | YES  |     | NULL    |                |
| id_categoria  | int          | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+


-- y categoriasportafolio(Identificador, nombre) 
CREATE TABLE categoriasportafolio(
	Identificador INT AUTO_INCREMENT,
	nombre VARCHAR(100),						
	PRIMARY KEY (Identificador)
);

-- Se comprueba que se  ha creado correctamente con su clave primaria
DESCRIBE categoriasportafolio;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

-- Se demuestra la capacidad de hacer un CRUD; inserción, lectura, actualización y eliminación de registros 

-- Insertaren: categoriasportafolio(Identificador, nombre)
INSERT INTO categoriasportafolio VALUES(
	NULL,
	'Exámenes Trimestrales'
);
-- Se comprueba que se ha creado el registro correctamente
SELECT * FROM categoriasportafolio;
+---------------+------------------------+
| Identificador | nombre                 |
+---------------+------------------------+
|             1 | Exámenes Trimestrales  |
+---------------+------------------------+

-- Insertar en: piezasportafolio (Identificador,titulo,descripcion,fecha,id_categoria)
INSERT INTO piezasportafolio VALUES(
	NULL,
	'Examen Trimestral 01',
	'En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre',
	'10-11-25',
	1
);

-- Se comprueba que se ha creado el registro correctamente. Aplicando lectura
SELECT * FROM piezasportafolio;
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
| Identificador | titulo               | descripcion                                                                                | fecha    | id_categoria |
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
|             1 | Examen Trimestral 01 | En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre | 10-11-25 |            1 |
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+

-- Actualizar piezasportafolio
UPDATE piezasportafolio
	SET titulo = 'Examen 1er Trimestre'
	WHERE Identificador = 1;

-- Se comprueba que se ha actualizado el registro correctamente. Aplicando lectura
SELECT * FROM piezasportafolio;
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
| Identificador | titulo               | descripcion                                                                                | fecha    | id_categoria |
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
|             1 | Examen 1er Trimestre | En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre | 10-11-25 |            1 |
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+

-- Actualizar piezasportafolio
UPDATE categoriasportafolio
	SET nombre = 'Examen'
	WHERE Identificador = 1;

-- Se comprueba que se ha actualizado el registro correctamente. Aplicando lectura
SELECT * FROM categoriasportafolio;
+---------------+--------+
| Identificador | nombre |
+---------------+--------+
|             1 | Examen |
+---------------+--------+

-- Eliminar elementos en categoriasportafolio
DELETE FROM categoriasportafolio
	WHERE Identificador = 1;

-- Se comprueba que se ha eliminado correctamente
SELECT * FROM categoriasportafolio;
Empty set

-- Eliminar elementos en piezasportafolio
DELETE FROM piezasportafolio
	WHERE Identificador = 1;
	
-- Se comprueba que se ha eliminado correctamente
SELECT * FROM categoriasportafolio;
Empty set

-- Se actualiza para poder crear la clave ajena
UPDATE piezasportafolio
	SET id_categoria = 2
	WHERE Identificador = 1;

-- Se crea una seleccion cruzada con LEFT JOIN y una vista de esa misma peticion 
ALTER TABLE piezasportafolio
	ADD CONSTRAINT pieza_a_categoria
	FOREIGN KEY (id_categoria) 
	REFERENCES categoriasportafolio(Identificador)
	ON DELETE CASCADE
	ON UPDATE CASCADE;

-- Se comprueba que se ha creado la clave ajena
DESCRIBE piezasportafolio;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripcion   | varchar(100) | YES  |     | NULL    |                |
| fecha         | varchar(100) | YES  |     | NULL    |                |
| id_categoria  | int          | YES  | MUL | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

-- Se realiza petición cruzada

CREATE VIEW pieza_categoria AS

SELECT 
piezasportafolio.titulo,
piezasportafolio.descripcion,
categoriasportafolio.nombre
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON categoriasportafolio.Identificador = piezasportafolio.id_categoria;

-- Se comprueba que se ha creado la vista
SELECT * FROM pieza_categoria;
+----------------------+--------------------------------------------------------------------------------------------+------------------------+
| titulo               | descripcion                                                                                | nombre                 |
+----------------------+--------------------------------------------------------------------------------------------+------------------------+
| Examen 1er Trimestre | En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre | Exámenes Trimestrales  |
+----------------------+--------------------------------------------------------------------------------------------+------------------------+

-- Crea un usuario con permisos para acceder a esa base de datos
-- Se crea usuario nuevo con contraseña segura
-- Con el nombre de usuario que queramos
CREATE USER
'benito'@'localhost'
IDENTIFIED BY 'F0nt4n3r0*';

-- Se permite acceso a ese usuario
GRANT USAGE ON *.* TO 'benito'@'localhost';

-- Se eliminan todos los límites de uso del usuario
ALTER USER 'benito'@'localhost'
REQUIRE NONE
WITH MAX_QUERIES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 0
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- Se le asignan todos los privilegios sobre la base de datos empresadam
GRANT ALL PRIVILEGES ON portafolioexamen.* TO 'benito'@'localhost';
GRANT ALL PRIVILEGES ON portafolioexamen.*
TO 'benito'@'localhost';

-- Se recarga la tabla de privilegios
FLUSH PRIVILEGES;

-- Se comprueba que se ha creado el usuario correctamente
SELECT User, Host FROM mysql.user;
+---------------------+-----------+
| User                | Host      |
+---------------------+-----------+
| [tunombredeusuario] | localhost |
| benito              | localhost |
| debian-sys-maint    | localhost |
| empresadam          | localhost |
| mysql.infoschema    | localhost |
| mysql.session       | localhost |
| mysql.sys           | localhost |
| portafolio          | localhost |
| root                | localhost |
| susana              | localhost |
| usuario1            | localhost |
+---------------------+-----------+












