# Creación de una base de datos y sistema web para noticias tecnológicas


El presente ejercicio tiene como objetivo consolidar los conocimientos previamente adquiridos sobre bases de datos, lenguaje SQL y desarrollo web con PHP mediante la creación de un sistema completo de gestión de noticias tecnológicas. A través del diseño de una base de datos, la creación de tablas relacionadas, la implementación de un sistema de acceso y la visualización de contenidos en una página web, se busca comprender el funcionamiento de una arquitectura cliente-servidor y reforzar la integración entre bases de datos y aplicaciones web dinámicas.

---
En esta práctica se trabaja con un sistema de información denominado "El jocarsa - Noticias tecnológicas", el cual permite almacenar, consultar y gestionar noticias, autores y usuarios mediante una base de datos relacional. Para ello, se aplican conceptos fundamentales como la creación de bases de datos, definición de tablas, uso de claves primarias y foráneas, consultas SQL y desarrollo de interfaces web con PHP.

El ejercicio también introduce la implementación de un sistema de filtrado que permite mostrar noticias por fecha de publicación o por autor, facilitando el acceso estructurado a la información.

---
Aplicación práctica
1. Creación de la base de datos

En primer lugar, se crea una base de datos llamada "El jocarsa - Noticias tecnológicas" utilizando lenguaje SQL. Esta base de datos servirá como contenedor principal de toda la información del sistema.
```
CREATE DATABASE el_jocarsa_noticias;
USE el_jocarsa_noticias;
```

2. Creación de las tablas principales
Se crean las tablas necesarias para almacenar la información sobre noticias, autores y usuarios.
```
CREATE TABLE autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150)
);

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    password VARCHAR(100)
);

CREATE TABLE noticias (
    id_noticia INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATE,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);
```
Estas tablas permiten estructurar la información de forma organizada, relacionando cada noticia con su autor correspondiente.

3. Sistema de acceso a la base de datos con PHP
Se desarrolla un sistema de conexión mediante PHP que permite realizar operaciones de inserción, actualización, eliminación y consulta de datos. Este sistema actúa como intermediario entre la página web y la base de datos.
```
<?php
$conexion = new mysqli("localhost", "usuario", "password", "el_jocarsa_noticias");

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}
?>
```
Gracias a esta conexión, se pueden ejecutar consultas SQL desde la aplicación web.

4. Página web de visualización de noticias
Se implementa una página web en PHP que muestra las noticias almacenadas en la base de datos. Esta página incluye un menú que permite:

- Listar todas las noticias disponibles.

- Filtrar noticias por fecha de publicación.

- Filtrar noticias por autor.
```
<?php
$resultado = $conexion->query("SELECT noticias.titulo, noticias.contenido, autores.nombre 
FROM noticias 
JOIN autores ON noticias.id_autor = autores.id_autor");

while ($fila = $resultado->fetch_assoc()) {
    echo "<h2>".$fila['titulo']."</h2>";
    echo "<p>".$fila['contenido']."</p>";
    echo "<small>Autor: ".$fila['nombre']."</small><hr>";
}
?>
```
Este sistema permite al usuario navegar de forma sencilla por las noticias publicadas.

---
Como resultado de esta práctica, se obtiene un sistema funcional de gestión de noticias tecnológicas que permite almacenar, consultar y administrar información mediante una base de datos relacional y una aplicación web desarrollada en PHP. El sistema permite mostrar las noticias de forma estructurada y aplicar filtros por autor o fecha, facilitando la navegación por los contenidos.

En este ejercicio se han aplicado de forma práctica los conceptos fundamentales de bases de datos, lenguaje SQL y desarrollo web con PHP, integrando todos ellos en un sistema real de gestión de noticias. Esta práctica permite comprender el funcionamiento completo de una aplicación web basada en bases de datos, desde el almacenamiento de la información hasta su visualización en una interfaz web. Asimismo, este tipo de ejercicios resulta esencial para el desarrollo de sistemas de información más complejos y para el fortalecimiento del pensamiento lógico y estructurado en el diseño de aplicaciones web modernas.
