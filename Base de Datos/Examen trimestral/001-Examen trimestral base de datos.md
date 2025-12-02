```
''' 
Base de datos portafolioexamen
2025 Fabiana Victoria Sotillo
Creación de una base de datos relacional con PK, FK, Vista y usuarios
'''
```

---
En este ejercicio se construye la base de datos portafolioexamen, orientada a gestionar piezas y categorías de proyectos. Se aplicaron los principios del modelo relacional mediante el uso de claves primarias, foráneas y vistas. La clave primaria (PK) identifica registros únicos, la foránea (FK) establece vínculos entre tablas, y la vista (VIEW) permite consultar datos combinados. El objetivo fue crear las tablas Pieza y Categoria, relacionarlas mediante una FK y generar una vista pieza_categoria que muestre su unión con un JOIN. Además de demostrar cómo se realiza el insertar, leer, actualizar y eliminar registros. Asimismo, se ha creado un usuario y se muestra cómo configurar sus permisos para trabajar en la base de datos portafolioexamen.

---
Se ilustrará el paso a paso del ejercicio con sus respectivas comprobaciones en mysql:

### 1. Se crea la base de datos portafolioexamen
```
CREATE DATABASE portafolioexamen;
```

- Se comprueba su correcta creación
```
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
```

- Se selecciona la base de datos
```
USE portafolioexamen;
```

### 2. Se crean dos tablas con claves primarias:
- piezasportafolio (Identificador,titulo,descripcion,fecha,id_categoria)
```
CREATE TABLE piezasportafolio(
	Identificador INT AUTO_INCREMENT,
	titulo VARCHAR(100),
	descripcion VARCHAR(100),
	fecha VARCHAR(100),
	id_categoria INT(100),							
	PRIMARY KEY (Identificador)
);
```

- Se comprueba que se  ha creado correctamente con su clave primaria
```
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
```

- y categoriasportafolio(Identificador, nombre) 
```
CREATE TABLE categoriasportafolio(
	Identificador INT AUTO_INCREMENT,
	nombre VARCHAR(100),						
	PRIMARY KEY (Identificador)
);
```

- Se comprueba que se  ha creado correctamente con su clave primaria
```
DESCRIBE categoriasportafolio;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```

### 3.  Se crea clave foránea para enlazar autores con piezas Inserta registros en ambas tablas  

- Se crea la llave foránea para poder ser utilizada en la selección cruzada.
```
ALTER TABLE piezasportafolio
	ADD CONSTRAINT pieza_a_categoria
	FOREIGN KEY (id_categoria) 
	REFERENCES categoriasportafolio(Identificador)
	ON DELETE CASCADE
	ON UPDATE CASCADE;
```

- Se comprueba que se ha creado la clave ajena
```
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
```

### 4. Se demuestra cómo insertar, leer, actualizar y eliminar registros 

- Insertar en: categoriasportafolio(Identificador, nombre)
```
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
```

- Insertar en: piezasportafolio (Identificador,titulo,descripcion,fecha,id_categoria)
```
INSERT INTO piezasportafolio VALUES(
	NULL,
	'Examen Trimestral 01',
	'En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre',
	'10-11-25',
	1
);
```

- Se comprueba que se ha creado el registro correctamente. Aplicando lectura.
```
SELECT * FROM piezasportafolio;
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
| Identificador | titulo               | descripcion                                                                                | fecha    | id_categoria |
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
|             1 | Examen Trimestral 01 | En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre | 10-11-25 |            1 |
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
```

- Actualizar piezasportafolio
```
UPDATE piezasportafolio
	SET titulo = 'Examen 1er Trimestre'
	WHERE Identificador = 1;
```

- Se comprueba que se ha actualizado el registro correctamente. Aplicando lectura.
```
SELECT * FROM piezasportafolio;
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
| Identificador | titulo               | descripcion                                                                                | fecha    | id_categoria |
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
|             1 | Examen 1er Trimestre | En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre | 10-11-25 |            1 |
+---------------+----------------------+--------------------------------------------------------------------------------------------+----------+--------------+
```

- Actualizar piezasportafolio
```
UPDATE categoriasportafolio
	SET nombre = 'Examen'
	WHERE Identificador = 1;
```

- Se comprueba que se ha actualizado el registro correctamente. Aplicando lectura.
```
SELECT * FROM categoriasportafolio;
+---------------+--------+
| Identificador | nombre |
+---------------+--------+
|             1 | Examen |
+---------------+--------+
```

- Se eliminan elementos en categoriasportafolio.
```
DELETE FROM categoriasportafolio
	WHERE Identificador = 1;
```

- Se comprueba que se ha eliminado correctamente
```
SELECT * FROM categoriasportafolio;
Empty set
```

- Se eliminan elementos en piezasportafolio
```
DELETE FROM piezasportafolio
	WHERE Identificador = 1;
```

- Se comprueba que se ha eliminado correctamente
```
SELECT * FROM categoriasportafolio;
Empty set
```

- Se actualiza para poder crear la clave ajena
```
UPDATE piezasportafolio
	SET id_categoria = 2
	WHERE Identificador = 1;
```

### 5. Se crea una seleccion cruzada con LEFT JOIN y una vista de esa misma petición 

- Se realiza petición cruzada
```
CREATE VIEW pieza_categoria AS

SELECT 
piezasportafolio.titulo,
piezasportafolio.descripcion,
categoriasportafolio.nombre
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON categoriasportafolio.Identificador = piezasportafolio.id_categoria;
```

- Se comprueba que se ha creado la vista.
```
SELECT * FROM pieza_categoria;
+----------------------+--------------------------------------------------------------------------------------------+------------------------+
| titulo               | descripcion                                                                                | nombre                 |
+----------------------+--------------------------------------------------------------------------------------------+------------------------+
| Examen 1er Trimestre | En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre | Exámenes Trimestrales  |
+----------------------+--------------------------------------------------------------------------------------------+------------------------+
```

### 6. Se crea un usuario con permisos para acceder a la base de datos
```
- Se crea usuario nuevo con contraseña segura con el nombre de usuario que queramos.
CREATE USER
'benito'@'localhost'
IDENTIFIED BY 'F0nt4n3r0*';
```

- Se permite acceso a ese usuario.
```
GRANT USAGE ON *.* TO 'benito'@'localhost';
```

- Se eliminan todos los límites de uso del usuario.
```
ALTER USER 'benito'@'localhost'
REQUIRE NONE
WITH MAX_QUERIES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 0
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
```

- Se le asignan todos los privilegios sobre la base de datos empresadam.
```
GRANT ALL PRIVILEGES ON portafolioexamen.* TO 'benito'@'localhost';
GRANT ALL PRIVILEGES ON portafolioexamen.*
TO 'benito'@'localhost';
```

- Se recarga la tabla de privilegios.
```
FLUSH PRIVILEGES;
```

- Se comprueba que se ha creado el usuario correctamente
```
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
```

---
La realización de este ejercicio permite aplicar de forma práctica los principios del modelo relacional en bases de datos. Ayuda a comprender de manera práctica el uso de claves primarias y foráneas para mantener la integridad de los datos, así como la utilidad de las vistas (VIEW) para combinar información procedente de distintas tablas en una única consulta estructurada.

Este tipo de estructura es esencial para proyectos como un portafolio, ya que separa los datos en entidades lógicas (piezas y categorías) y facilita su gestión, manteniendo a la vez una presentación. Se ha ilustrado cómo modificar los datos de una base de datos, crearlos, mostrarlos, actualizarlos y eliminarlos, conceptos que son fundamentales para la gestión de una base de datos.

Además, se ha reforzado la importancia del orden lógico al insertar y relacionar los registros, consolidando habilidades fundamentales para el diseño y desarrollo de sistemas de bases de datos más complejos.

Asimismo, esta práctica permitió comprender la importancia de gestionar usuarios y privilegios en MySQL para mantener la seguridad y el control de acceso a la base de datos. La creación de un usuario con privilegios específicos asegura que cada cuenta pueda realizar únicamente las operaciones autorizadas, evitando accesos no deseados o modificaciones indebidas en los datos.  La actividad reforzó el uso de comandos clave como CREATE USER, GRANT, ALTER USER y FLUSH PRIVILEGES, mostrando cómo se puede configurar un usuario de manera segura y eficiente, garantizando la administración correcta y segura de los recursos de la base de datos.
