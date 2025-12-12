CREATE DATABASE portafolio;

-- Nos aseguramos de que se ha creado correctamente
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
| sys                |
+--------------------+

-- La seleccionamos para trabajar con ella
USE portafolio;

-- Creamos primera tabla Pieza (Identificador PK, titulo, descripción, imagen, url, id_categoria FK)
CREATE TABLE Pieza(
	Identificador INT(255) AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(100),
	descripción VARCHAR(255),	-- También podría ser TEXT y tener longitud variable
	imagen VARCHAR(100),
	url VARCHAR(255),
	id_categoria INT(100)
);

-- Verificamos que se ha creado correctamente
DESCRIBE Pieza;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripción   | varchar(255) | YES  |     | NULL    |                |
| imagen        | varchar(100) | YES  |     | NULL    |                |
| url           | varchar(255) | YES  |     | NULL    |                |
| id_categoria  | int          | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+


-- Creamos  tabla Categoria (Identificador PK, titulo, descripción)
CREATE TABLE Categoria(
	Identificador INT(255) AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(100),
	descripción VARCHAR(255)
);

-- Verificamos que se ha creado correctamente
DESCRIBE Categoria;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripción   | varchar(255) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

-- Creamos FK id_categoria FK de Pieza a Categoria
ALTER TABLE Pieza
	ADD CONSTRAINT pieza_a_categoria
	FOREIGN KEY (id_categoria) 
	REFERENCES Categoria(Identificador)
	ON DELETE CASCADE
	ON UPDATE CASCADE;
	
-- Añadimos una instancia a la tabla Categoria
INSERT INTO Categoria VALUES (
	NULL,
	'Diseño Web', 
	'Proyectos y desarrollos de sitios y aplicaciones web.'
);

-- Verificamos que se ha añadido
SELECT * FROM Categoria;
+---------------+-------------+-------------------------------------------------------+
| Identificador | titulo      | descripción                                           |
+---------------+-------------+-------------------------------------------------------+
|             1 | Diseño Web  | Proyectos y desarrollos de sitios y aplicaciones web. |
+---------------+-------------+-------------------------------------------------------+

-- Añadimos una instancia a la tabla Pieza
INSERT INTO Pieza (titulo, descripción, imagen, url, id_categoria)
VALUES (
    'Portafolio Personal',
    'Sitio web creado para mostrar proyectos, habilidades y trabajos de diseño.',
    'portafolio.png',
    'https://fabianasotillo.com',
    1
);

-- Verificamos que se ha añadido
SELECT * FROM Pieza;
+---------------+---------------------+-----------------------------------------------------------------------------+----------------+----------------------------+--------------+
| Identificador | titulo              | descripción                                                                 | imagen         | url                        | id_categoria |
+---------------+---------------------+-----------------------------------------------------------------------------+----------------+----------------------------+--------------+
|             2 | Portafolio Personal | Sitio web creado para mostrar proyectos, habilidades y trabajos de diseño.  | portafolio.png | https://fabianasotillo.com |            1 |
+---------------+---------------------+-----------------------------------------------------------------------------+----------------+----------------------------+--------------+

-- Creamos vista (Debe existir una FK entre Pieza y Categoría. Hacer un join entre las dos tablas y una vista (view) de ese JOIN.)
CREATE VIEW pieza_categoria AS

SELECT 
Pieza.titulo AS t1,
Pieza.descripción AS d1,
Categoria.titulo,
Categoria.descripción
FROM Pieza
LEFT JOIN Categoria
ON Categoria.Identificador = Pieza.id_categoria;

-- Verificamos que funcionó
DESCRIBE pieza_categoria;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| t1           | varchar(100) | YES  |     | NULL    |       |
| d1           | varchar(255) | YES  |     | NULL    |       |
| titulo       | varchar(100) | YES  |     | NULL    |       |
| descripción  | varchar(255) | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+

-- Plantilla para solucionar que en las dos tablas hay atributos que se llaman igual
SELECT 
tabla1.campo1 AS ...,
tabla1.campo2 AS ...,
tabla1.campo3,
tabla2.campo1,
tabla2.campo2
FROM
tabla1
LEFT JOIN tabla2
ON ref = a donde ?;

-- La otra solución es evitar los atributos con mismos nombres

-- Verificamos vista
SELECT * FROM pieza_categoria;

+---------------------+-----------------------------------------------------------------------------+-------------+-------------------------------------------------------+
| t1                  | d1                                                                          | titulo      | descripción                                           |
+---------------------+-----------------------------------------------------------------------------+-------------+-------------------------------------------------------+
| Portafolio Personal | Sitio web creado para mostrar proyectos, habilidades y trabajos de diseño.  | Diseño Web  | Proyectos y desarrollos de sitios y aplicaciones web. |
+---------------------+-----------------------------------------------------------------------------+-------------+-------------------------------------------------------+















