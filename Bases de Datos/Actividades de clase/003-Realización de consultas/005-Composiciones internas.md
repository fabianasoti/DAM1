El presente ejercicio tiene como objetivo aplicar los conceptos fundamentales sobre bases de datos y consultas SQL trabajados en clase, integrándolos con el desarrollo de aplicaciones web mediante el framework Flask en Python. A través de la creación de una base de datos, la conexión desde Python, la implementación de endpoints y la consulta de usuarios del sistema, se busca comprender el funcionamiento de una arquitectura cliente-servidor basada en bases de datos, así como reforzar el uso de scripts SQL y la interacción entre MySQL y aplicaciones web.

---
En esta actividad se comienza con la creación de una base de datos llamada tiendaclase utilizando un script SQL proporcionado, el cual define la estructura inicial necesaria para trabajar con las tablas correspondientes. Posteriormente, se establece una conexión a dicha base de datos mediante un archivo Python que permite realizar consultas y operaciones sobre la información almacenada.

A continuación, se desarrolla un segundo endpoint en Flask que permite obtener información sobre las tablas existentes en la base de datos, mostrando tanto los clientes como las tablas disponibles. De forma complementaria, se ejecuta un script SQL para visualizar los usuarios del sistema MySQL y sus permisos, lo que permite comprender la gestión de accesos dentro del gestor de bases de datos. Finalmente, se prueban los endpoints creados para verificar su correcto funcionamiento y comprobar que devuelven la información esperada.

---
A continuación, se describe el procedimiento seguido para realizar la actividad.

1. Creación de la base de datos

Se ejecuta el script SQL proporcionado 001-creo base de datos.sql en el entorno MySQL para crear la base de datos llamada tiendaclase. Este script define la estructura inicial necesaria para trabajar con las tablas de la tienda.
```
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;

-- Tabla clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);

-- Tabla productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Datos de prueba: clientes
INSERT INTO clientes (nombre, email, telefono)
VALUES
    ('Susana Santana', 'susana@ejemplo.com', '600123456'),
    ('Benito Bonito', 'benito@ejemplo.com', '611987654'),
    ('Elga Tito', 'elga@ejemplo.com', '622111222');

-- Datos de prueba: productos
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES 
('Ovillo Merino', 'Lana 100% merino suave 100g', 12.50, 45),
('Ganchillo 4mm', 'Aguja ergonómica mango silicona', 5.99, 30),
('Algodón Pima', 'Hilo algodón alta calidad crudo', 8.20, 60),
('Palillos Bambú', 'Agujas de madera 6mm ligeras', 7.50, 20),
('Marcadores', 'Set 50 marcadores tipo candado', 4.50, 100),
('Lana Alpaca', 'Mezcla alpaca y seda gris', 15.90, 15),
('Agujas Circulares', 'Metal 80cm de largo, 5mm grosor', 9.00, 25),
('Tijeras Cigüeña', 'Tijeras bordado diseño vintage', 11.50, 18),
('Cinta Métrica', 'Cinta retráctil de 150cm', 3.00, 75),
('Trapillo Bobina', 'Tela reciclada para cestas 800g', 14.00, 12);
```

2. Conexión a la base de datos desde Python

Se utiliza el archivo 004-nos conectamos a mysql.py para establecer la conexión entre Python y la base de datos tiendaclase. Esta conexión permite realizar consultas y operaciones desde una aplicación externa.
```
import mysql.connector 

conexion = mysql.connector.connect(
	host="localhost",
	user="tiendaclase",
	password="F0nt4n3r0*",
	database="tiendaclase"
)                                      
  
cursor = conexion.cursor() 
cursor.execute("SELECT * FROM clientes;")  

filas = cursor.fetchall()

print(filas)
```
Mostrando este resultado en pantalla:
[(1, 'Susana Santana', 'susana@ejemplo.com', '600123456', None), (2, 'Benito Bonito', 'benito@ejemplo.com', '611987654', None), (3, 'Elga Tito', 'elga@ejemplo.com', '622111222', None)]

3. Creación del segundo endpoint en Flask

Se desarrolla un segundo endpoint utilizando el archivo 006-creamos segundo endpoint.py, el cual devuelve información sobre las tablas existentes en la base de datos. Este endpoint permite visualizar tanto los clientes como las tablas disponibles, facilitando el acceso a la información desde una aplicación web.
```
import mysql.connector
from flask import Flask
import json

conexion = mysql.connector.connect(
	host="localhost",
	user="tiendaclase",
	password="F0nt4n3r0*",
	database="tiendaclase"
)                                      
  
app = Flask(__name__)

@app.route("/clientes")
def clientes():
	cursor = conexion.cursor() 
	cursor.execute("SELECT * FROM clientes;")  

	filas = cursor.fetchall()
	return json.dumps(filas)
	
# http://127.0.0.1:5000/clientes

@app.route("/tablas")
def tablas():
	cursor = conexion.cursor() 
	cursor.execute("SHOW TABLES;")  

	filas = cursor.fetchall()
	tablas = []
	for fila in filas:
		tablas.append(fila[0])
	return json.dumps(tablas)

if __name__ == "__main__":
	app.run(debug=True)
	
# http://127.0.0.1:5000/tablas
```

4. Visualización de usuarios del sistema MySQL

Se ejecuta el script 003-ver los usuarios del sistema.sql para mostrar los usuarios registrados en MySQL junto con sus permisos. Esta consulta permite comprender cómo se gestiona la seguridad y el acceso a la base de datos.
```
SELECT User, Host 
FROM mysql.user;

+--------------------+-----------+
| User               | Host      |
+--------------------+-----------+
| Fabiana            | localhost |
| clientes           | localhost |
| debian-sys-maint   | localhost |
| diarioemocional    | localhost |
| mysql.infoschema   | localhost |
| mysql.session      | localhost |
| mysql.sys          | localhost |
| root               | localhost |
| tiendaclase        | localhost |
| tiendaonlinedamdaw | localhost |
+--------------------+-----------+
```

5. Prueba de los endpoints

Finalmente, se ejecuta el archivo endpoint principal.py para poner en marcha la aplicación Flask y probar ambos endpoints. De esta forma, se verifica que las rutas funcionan correctamente y que devuelven la información esperada.
```
import mysql.connector 
from flask import Flask, render_template, jsonify, g

app = Flask(__name__)

def get_db():
	if 'db' not in g:
		g.db = mysql.connector.connect(
			host="localhost",
			user="tiendaclase",
			password="F0nt4n3r0*",
			database="tiendaclase"
		)
	return g.db

@app.teardown_appcontext
def close_db(exception):
	db = g.pop('db', None)
	if db is not None:
		db.close()

@app.route("/")
def raiz():
	return render_template("index.html")
# http://127.0.0.1:5000/clientes

@app.route("/clientes")
def clientes():
	db = get_db()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM clientes;")
	filas = cursor.fetchall()
	cursor.close()
	return jsonify(filas)
# http://127.0.0.1:5000/tablas

@app.route("/tablas")
def tablas():
	db = get_db()
	cursor = db.cursor()
	cursor.execute("SHOW TABLES;")
	filas = cursor.fetchall()
	cursor.close()

	tablas = [fila[0] for fila in filas]
	return jsonify(tablas)

if __name__ == "__main__":
	app.run(debug=True, use_reloader=False)
```

---
Como resultado de esta actividad, se obtiene una base de datos funcional llamada tiendaclase, accesible desde Python mediante una aplicación Flask. Los endpoints permiten consultar la información almacenada y visualizar las tablas existentes, mientras que los scripts SQL permiten gestionar y analizar los usuarios del sistema.

Este ejercicio permite integrar los conocimientos adquiridos sobre bases de datos, consultas SQL y desarrollo web con Flask, aplicando una arquitectura completa que conecta una base de datos MySQL con una aplicación Python. La creación de endpoints facilita el acceso a la información de forma estructurada, mientras que la gestión de usuarios permite comprender los mecanismos de seguridad del sistema. Este tipo de prácticas resulta fundamental para el desarrollo de aplicaciones web modernas basadas en bases de datos y para el aprendizaje de sistemas de información.
