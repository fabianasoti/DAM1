```
'''
Uso de plantillas en Flask para mostrar datos de una base de datos MySQL
2026 Fabiana Sotillo
Bases de datos relacionales y desarrollo web utilizando Flask
'''
```

---
El presente ejercicio tiene como objetivo aplicar los conocimientos adquiridos sobre bases de datos relacionales y desarrollo web utilizando Flask, integrando ambos entornos mediante el uso de plantillas HTML. A través de la creación de una base de datos con varias tablas relacionadas, la inserción de datos de ejemplo, la creación de una vista en SQL y la conexión desde una aplicación Flask, se busca comprender cómo recuperar información almacenada en MySQL y mostrarla dinámicamente en una página web. De este modo, se refuerza el uso de consultas SQL, la gestión de vistas y la presentación de datos mediante templates.

---
En esta actividad se comienza con la creación de una base de datos llamada composiciones, en la que se definen varias tablas relacionadas entre sí: alumnos, profesores, asignaturas y matrículas. Estas tablas permiten representar una estructura académica básica con relaciones entre estudiantes, asignaturas y docentes.

Posteriormente, se insertan datos de ejemplo para poder trabajar con información real dentro de la base de datos. A continuación, se crea una vista en SQL que combina información de varias tablas mediante instrucciones INNER JOIN, lo que permite obtener un conjunto de datos unificado y listo para su visualización.

Seguidamente, se desarrolla una aplicación Flask que se conecta a la base de datos, ejecuta una consulta sobre la vista creada y envía los resultados a una plantilla HTML. Esta plantilla se encarga de mostrar los datos en forma de tabla, utilizando la sintaxis propia de los templates de Flask. Finalmente, se ejecuta la aplicación y se visualizan los datos desde el navegador.

---
A continuación, se describe el procedimiento seguido para llevar a cabo la actividad.

1. Creación de la base de datos y las tablas

Se ejecuta el siguiente script en MySQL para crear la base de datos "composiciones" y sus tablas correspondientes:
```
CREATE DATABASE composiciones;

USE composiciones;

CREATE TABLE alumnos(
    Identificador INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100)
);

CREATE TABLE profesores(
    Identificador INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100)
);

CREATE TABLE asignaturas(
    Identificador INT PRIMARY KEY,
    nombre VARCHAR(100),
    id_profesor INT
);

CREATE TABLE matriculas(
    Identificador INT PRIMARY KEY,
    id_asignatura INT,
    id_alumno INT
);
```

Posteriormente, se insertan datos de ejemplo en las tablas para poder realizar pruebas.

2. Inserción de datos de muestra
```
INSERT INTO alumnos (Identificador, nombre, apellidos) VALUES
(1,'Ana','García López'),
(2,'Luis','Martínez Pérez'),
(3,'María','Sánchez Ruiz'),
(4,'Javier','Fernández Gómez'),
(5,'Laura','Díaz');

INSERT INTO profesores (Identificador, nombre, apellidos) VALUES
(101,'Juan','Pérez'),
(102,'Ana','López');

INSERT INTO asignaturas (Identificador, nombre, id_profesor) VALUES
(1001,'Matemáticas',101),
(1002,'Física',102);

INSERT INTO matriculas (Identificador, id_asignatura, id_alumno) VALUES
(1,1001,1),
(2,1001,2),
(3,1002,3);
```

3. Creación de la vista en SQL
4. ```
CREATE VIEW matriculas_join AS 
SELECT 
    asignaturas.nombre AS 'Asignatura',
    alumnos.nombre AS 'Alumno',
    alumnos.apellidos AS 'Apellidos'
FROM matriculas
INNER JOIN asignaturas ON matriculas.id_asignatura = asignaturas.Identificador
INNER JOIN alumnos ON matriculas.id_alumno = alumnos.Identificador;
```

Esta vista permite combinar la información de varias tablas para facilitar su consulta desde la aplicación Flask.

4. Aplicación Flask para mostrar los datos
```
import mysql.connector 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    conexion = mysql.connector.connect(
        host="localhost",
        user="composiciones",
        password="composiciones",
        database="composiciones"
    )                                      

    cursor = conexion.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM matriculas_join;")
    filas = cursor.fetchall()
    return render_template("index.html", datos=filas)

if __name__ == "__main__":
    app.run(debug=True)
```

Este script establece la conexión con la base de datos, ejecuta la consulta sobre la vista y envía los datos a la plantilla HTML.

5. Creación del template HTML
```
<!doctype html>
<html lang="es">
<head>
    <title>Backoffice</title>
    <meta charset="utf-8">
    <style>
        body{font-family:sans-serif;background:aliceblue;}
        table{width:100%;border-collapse:collapse;margin-bottom:20px;}
        th, td{padding:10px;text-align:left;border-bottom:1px solid #ddd;}
        th{background-color:#f2f2f2;}
    </style>
</head>
<body>
    <h1>Backoffice</h1>
    <table>
        <tr>
            <th>Asignatura</th>
            <th>Alumno</th>
            <th>Apellidos</th>
        </tr>
        {% for fila in datos %}
        <tr>
            <td>{{ fila['Asignatura'] }}</td>
            <td>{{ fila['Alumno'] }}</td>
            <td>{{ fila['Apellidos'] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

Esta plantilla permite mostrar los datos en una tabla HTML utilizando la sintaxis de templates de Flask.

---
Como resultado de la ejecución de la aplicación Flask, se visualiza en el navegador una tabla que muestra las asignaturas, los nombres de los alumnos y sus apellidos, obtenidos directamente desde la base de datos mediante una vista SQL.

Este ejercicio permite integrar bases de datos relacionales con aplicaciones web utilizando Flask y plantillas HTML. La creación de vistas en SQL facilita la obtención de información combinada de varias tablas, mientras que el uso de templates permite presentar los datos de forma clara y estructurada. Esta práctica resulta fundamental para el desarrollo de aplicaciones web dinámicas y para la gestión eficiente de información almacenada en bases de datos relacionales.
