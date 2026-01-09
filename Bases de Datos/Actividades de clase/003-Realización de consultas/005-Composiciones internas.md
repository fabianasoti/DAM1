El presente ejercicio tiene como objetivo aplicar los conceptos fundamentales sobre bases de datos y consultas SQL trabajados en clase, integrándolos con el desarrollo de aplicaciones web mediante el framework Flask en Python. A través de la creación de una base de datos, la conexión desde Python, la implementación de endpoints y la consulta de usuarios del sistema, se busca comprender el funcionamiento de una arquitectura cliente-servidor basada en bases de datos, así como reforzar el uso de scripts SQL y la interacción entre MySQL y aplicaciones web.

---
En esta actividad se comienza con la creación de una base de datos llamada tiendaclase utilizando un script SQL proporcionado, el cual define la estructura inicial necesaria para trabajar con las tablas correspondientes. Posteriormente, se establece una conexión a dicha base de datos mediante un archivo Python que permite realizar consultas y operaciones sobre la información almacenada.

A continuación, se desarrolla un segundo endpoint en Flask que permite obtener información sobre las tablas existentes en la base de datos, mostrando tanto los clientes como las tablas disponibles. De forma complementaria, se ejecuta un script SQL para visualizar los usuarios del sistema MySQL y sus permisos, lo que permite comprender la gestión de accesos dentro del gestor de bases de datos. Finalmente, se prueban los endpoints creados para verificar su correcto funcionamiento y comprobar que devuelven la información esperada.

---
A continuación, se describe el procedimiento seguido para realizar la actividad.

1. Creación de la base de datos

Se ejecuta el script SQL proporcionado 001-creo base de datos.sql en el entorno MySQL para crear la base de datos llamada tiendaclase. Este script define la estructura inicial necesaria para trabajar con las tablas de la tienda.

2. Conexión a la base de datos desde Python

Se utiliza el archivo 004-nos conectamos a mysql.py para establecer la conexión entre Python y la base de datos tiendaclase. Esta conexión permite realizar consultas y operaciones desde una aplicación externa.

3. Creación del segundo endpoint en Flask

Se desarrolla un segundo endpoint utilizando el archivo 006-creamos segundo endpoint.py, el cual devuelve información sobre las tablas existentes en la base de datos. Este endpoint permite visualizar tanto los clientes como las tablas disponibles, facilitando el acceso a la información desde una aplicación web.

4. Visualización de usuarios del sistema MySQL

Se ejecuta el script 003-ver los usuarios del sistema.sql para mostrar los usuarios registrados en MySQL junto con sus permisos. Esta consulta permite comprender cómo se gestiona la seguridad y el acceso a la base de datos.

5. Prueba de los endpoints

Finalmente, se ejecuta el archivo endpoint principal.py para poner en marcha la aplicación Flask y probar ambos endpoints. De esta forma, se verifica que las rutas funcionan correctamente y que devuelven la información esperada.

---
Como resultado de esta actividad, se obtiene una base de datos funcional llamada tiendaclase, accesible desde Python mediante una aplicación Flask. Los endpoints permiten consultar la información almacenada y visualizar las tablas existentes, mientras que los scripts SQL permiten gestionar y analizar los usuarios del sistema.

este ejercicio permite integrar los conocimientos adquiridos sobre bases de datos, consultas SQL y desarrollo web con Flask, aplicando una arquitectura completa que conecta una base de datos MySQL con una aplicación Python. La creación de endpoints facilita el acceso a la información de forma estructurada, mientras que la gestión de usuarios permite comprender los mecanismos de seguridad del sistema. Este tipo de prácticas resulta fundamental para el desarrollo de aplicaciones web modernas basadas en bases de datos y para el aprendizaje de sistemas de información más complejos.
