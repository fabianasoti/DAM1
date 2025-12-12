```
''' 
Base de datos Portafolio
2025 Fabiana Victoria Sotillo
Creación de una base de datos relacional
'''
```

---
En este ejercicio se construye la base de datos portafolio, orientada a gestionar piezas y categorías de proyectos dentro de un sitio web con panel administrativo. Se aplicaron los principios del modelo relacional mediante el uso de claves primarias, foráneas y vistas. La clave primaria (PK) identifica registros únicos, la foránea (FK) establece vínculos entre tablas, y la vista (VIEW) permite consultar datos combinados. El objetivo fue crear las tablas Pieza y Categoria, relacionarlas mediante una FK y generar una vista pieza_categoria que muestre su unión con un JOIN.

---
Se ilustrará el paso a paso del ejercicio con sus respectivas comprobaciones en mysql:

- El desarrollo comenzó con la creación de la base de datos portafolio y su selección como entorno de trabajo.
```
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

USE portafolio;
```

- Posteriormente se definieron las tablas principales: Pieza y Categoria con sus respectivos campos. 
```
-- Tabla Pieza
CREATE TABLE Pieza(
	Identificador INT(255) AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(100),
	descripción VARCHAR(255),
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

-- Tabla Categoria
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
```

- Luego, mediante ALTER TABLE, se estableció una clave foránea que conecta Pieza.id_categoria con Categoria.Identificador, asegurando la integridad referencial.
```
-- Clave foránea: Pieza.id_categoria → Categoria.Identificador
ALTER TABLE Pieza
	ADD CONSTRAINT pieza_a_categoria
	FOREIGN KEY (id_categoria) 
	REFERENCES Categoria(Identificador)
	ON DELETE CASCADE
	ON UPDATE CASCADE;
```

- Se inserta una categoría (Diseño Web) y una pieza asociada (Portafolio Personal). 
```
-- Inserción de una categoría
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

-- Inserción de una pieza relacionada con la categoría anterior
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
```

- Finalmente, se generó la vista pieza_categoria utilizando un LEFT JOIN con alias para evitar ambigüedades, permitiendo
```

-- Creación de la vista con JOIN entre Pieza y Categoria
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

-- Verificamos vista
SELECT * FROM pieza_categoria;

+---------------------+-----------------------------------------------------------------------------+-------------+-------------------------------------------------------+
| t1                  | d1                                                                          | titulo      | descripción                                           |
+---------------------+-----------------------------------------------------------------------------+-------------+-------------------------------------------------------+
| Portafolio Personal | Sitio web creado para mostrar proyectos, habilidades y trabajos de diseño.  | Diseño Web  | Proyectos y desarrollos de sitios y aplicaciones web. |
+---------------------+-----------------------------------------------------------------------------+-------------+-------------------------------------------------------+
```

---
A continuación se muestra el código SQL completo, comentado y funcional:
```
''' 
Base de datos Portafolio
2025 Fabiana Victoria Sotillo
Creación de una base de datos relacional
'''

-- Creación de la base de datos
CREATE DATABASE portafolio;
USE portafolio;

-- Tabla Pieza
CREATE TABLE Pieza(
	Identificador INT(255) AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(100),
	descripción VARCHAR(255),
	imagen VARCHAR(100),
	url VARCHAR(255),
	id_categoria INT(100)
);

-- Tabla Categoria
CREATE TABLE Categoria(
	Identificador INT(255) AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(100),
	descripción VARCHAR(255)
);

-- Clave foránea: Pieza.id_categoria → Categoria.Identificador
ALTER TABLE Pieza
	ADD CONSTRAINT pieza_a_categoria
	FOREIGN KEY (id_categoria) 
	REFERENCES Categoria(Identificador)
	ON DELETE CASCADE
	ON UPDATE CASCADE;

-- Inserción de una categoría
INSERT INTO Categoria VALUES (
	NULL,
	'Diseño Web', 
	'Proyectos y desarrollos de sitios y aplicaciones web.'
);

-- Inserción de una pieza relacionada con la categoría anterior
INSERT INTO Pieza (titulo, descripción, imagen, url, id_categoria)
VALUES (
    'Portafolio Personal',
    'Sitio web creado para mostrar proyectos, habilidades y trabajos de diseño.',
    'portafolio.png',
    'https://fabianasotillo.com',
    1
);

-- Creación de la vista con JOIN entre Pieza y Categoria
CREATE VIEW pieza_categoria AS
SELECT 
	Pieza.titulo AS t1,
	Pieza.descripción AS d1,
	Categoria.titulo,
	Categoria.descripción
FROM Pieza
LEFT JOIN Categoria
	ON Categoria.Identificador = Pieza.id_categoria;

-- Verificación de la vista
SELECT * FROM pieza_categoria;
```

---
La realización de este ejercicio permite aplicar de forma práctica los principios del modelo relacional en bases de datos. Ayuda a comprender de manera práctica el uso de claves primarias y foráneas para mantener la integridad de los datos, así como la utilidad de las vistas (VIEW) para combinar información procedente de distintas tablas en una única consulta estructurada.

Este tipo de estructura es esencial para proyectos como un portafolio web, ya que separa los datos en entidades lógicas (piezas y categorías) y facilita su gestión desde un panel de administración, manteniendo a la vez una presentación ordenada para el usuario final.

Además, el manejo de errores comunes fortaleció la comprensión de las relaciones entre tablas y la importancia del orden lógico al insertar y relacionar los registros, consolidando habilidades fundamentales para el diseño y desarrollo de sistemas de bases de datos más complejos.
