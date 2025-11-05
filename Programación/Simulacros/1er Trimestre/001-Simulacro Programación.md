```
''' 
Gestión de portafolio con MySQL y Python
2025 Fabiana Victoria Sotillo
Programa que permite insertar, listar, actualizar y eliminar piezas del portafolio 
utilizando una base de datos MySQL conectada mediante la librería mysql.connector.
'''
```

---
Este ejercicio consiste en desarrollar un sistema básico de gestión de un portafolio utilizando una base de datos MySQL y un programa en Python que permite realizar operaciones CRUD (crear, leer, actualizar y eliminar). Se aplican conceptos fundamentales de bases de datos relacionales como claves primarias, foráneas, vistas y permisos de usuario, junto con el manejo de conexión y ejecución de sentencias SQL desde Python mediante la librería mysql.connector. El objetivo práctico es simular la administración de las piezas de un portafolio digital mediante un menú interactivo que gestiona registros en la tabla Pieza.

---

- Primero, se configura el entorno de la base de datos portafolio y se crean las tablas Categoria y Pieza, con su relación mediante una clave foránea (id_categoria). Luego, se define un usuario de MySQL con permisos específicos sobre dicha base de datos.
```
# Creación del usuario y asignación de permisos en MySQL

CREATE USER 'usuario1'@'localhost' IDENTIFIED BY 'Portafolio123$';
GRANT USAGE ON *.* TO 'usuario1'@'localhost';
ALTER USER 'usuario1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `portafolio`.* TO 'usuario1'@'localhost';
FLUSH PRIVILEGES;
```

- Desde Python, el programa se conecta a MySQL utilizando las credenciales del nuevo usuario y ejecuta sentencias SQL dinámicas mediante un cursor. 
```
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="usuario1",
    password="Portafolio123$",
    database="portafolio"
)
cursor = conexion.cursor()
```
 
- El sistema presenta un menú que ofrece las cuatro operaciones CRUD:
```
print("Gestion de portafolio v0.1")

while True:
    print("Escoge una opcion")
    print("1.-Insertar")
    print("2.-Listar")
    print("3.-Actualizar")
    print("4.-Eliminar")
    opcion = int(input("Escoge una opcion: "))
    print("La opción que has escogido es: ", opcion)
```

- Se definen las opciones dentro de un bucle while True, atrapando sus funciones con condicionales (if, elif)
	- Insertar: agrega una nueva pieza con sus atributos (título, descripción, imagen, URL y categoría).
		```
		    if opcion == 1:
        titulo = input("Introduce el titulo de la nueva pieza: ")
        descripcion = input("Introduce la descripcion de la nueva pieza: ")
        imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
        url = input("Introduce la url de la nueva pieza: ")
        cursor.execute("INSERT INTO Pieza VALUES (
					NULL,'"+titulo+"','"+descripcion+"','"+imagen+"','"+url+"',1);")
        conexion.commit()
		```
		
	- Listar: muestra todas las piezas registradas.
		```
		elif opcion == 2:
        cursor.execute("SELECT * FROM Pieza;")
        lineas = cursor.fetchall()
        for linea in lineas:
         print(linea)
		```
		
	- Actualizar: permite modificar los datos de una pieza existente.
		```
		    elif opcion == 3:
        identificador = input("Introduce el Identificador a actualizar: ")
        titulo = input("Introduce el titulo de la nueva pieza: ")
        descripcion = input("Introduce la descripcion de la nueva pieza: ")
        imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
        url = input("Introduce la url de la nueva pieza: ")
        cursor.execute('''
            UPDATE Pieza 
            SET
            titulo = "'''+titulo+'''",
            descripción = "'''+descripcion+'''",
            imagen = "'''+imagen+'''",
            url = "'''+url+'''"
            WHERE Identificador = '''+identificador+''';
        ''')
        conexion.commit()
		```
		
	- Eliminar: borra un registro mediante su identificador.
		```
		  elif opcion == 4:
        identificador = input("Introduce el Identificador a eliminar: ")
        cursor.execute("DELETE FROM Pieza WHERE Identificador = "+identificador+";")
        conexion.commit()
		```
Cada operación ejecuta un commit para guardar los cambios en la base de datos. Se manejan las consultas SQL con concatenación de variables y estructura condicional if/elif para definir el flujo de ejecución según la opción seleccionada.

---
A continuación se muestra el código funcional completo:

```
''' 
Gestión de portafolio con MySQL y Python
2025 Fabiana Victoria Sotillo
Programa que permite insertar, listar, actualizar y eliminar piezas del portafolio 
utilizando una base de datos MySQL conectada mediante la librería mysql.connector.
'''

# Creación del usuario y asignación de permisos en MySQL
'''
CREATE USER 'usuario1'@'localhost' IDENTIFIED BY 'Portafolio123$';
GRANT USAGE ON *.* TO 'usuario1'@'localhost';
ALTER USER 'usuario1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `portafolio`.* TO 'usuario1'@'localhost';
FLUSH PRIVILEGES;
'''

import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="usuario1",
    password="Portafolio123$",
    database="portafolio"
)
cursor = conexion.cursor()

print("Gestion de portafolio v0.1")

while True:
    print("Escoge una opcion")
    print("1.-Insertar")
    print("2.-Listar")
    print("3.-Actualizar")
    print("4.-Eliminar")
    opcion = int(input("Escoge una opcion: "))
    print("La opción que has escogido es: ", opcion)

    if opcion == 1:
        titulo = input("Introduce el titulo de la nueva pieza: ")
        descripcion = input("Introduce la descripcion de la nueva pieza: ")
        imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
        url = input("Introduce la url de la nueva pieza: ")
        cursor.execute("INSERT INTO Pieza VALUES (NULL,'"+titulo+"','"+descripcion+"','"+imagen+"','"+url+"',1);")
        conexion.commit()

    elif opcion == 2:
        cursor.execute("SELECT * FROM Pieza;")
        lineas = cursor.fetchall()
        for linea in lineas:
            print(linea)

    elif opcion == 3:
        identificador = input("Introduce el Identificador a actualizar: ")
        titulo = input("Introduce el titulo de la nueva pieza: ")
        descripcion = input("Introduce la descripcion de la nueva pieza: ")
        imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
        url = input("Introduce la url de la nueva pieza: ")
        cursor.execute('''
            UPDATE Pieza 
            SET
            titulo = "'''+titulo+'''",
            descripción = "'''+descripcion+'''",
            imagen = "'''+imagen+'''",
            url = "'''+url+'''"
            WHERE Identificador = '''+identificador+''';
        ''')
        conexion.commit()

    elif opcion == 4:
        identificador = input("Introduce el Identificador a eliminar: ")
        cursor.execute("DELETE FROM Pieza WHERE Identificador = "+identificador+";")
        conexion.commit()
```

---
El ejercicio permite integrar los fundamentos de bases de datos relacionales con la programación en Python, fortaleciendo la comprensión del manejo de datos a través de sentencias SQL ejecutadas desde código. La práctica del modelo CRUD favorece el desarrollo del pensamiento algorítmico orientado a la gestión de información y prepara el terreno para implementar sistemas más complejos con validaciones, manejo de errores y seguridad reforzada en futuras aplicaciones web o de escritorio.
