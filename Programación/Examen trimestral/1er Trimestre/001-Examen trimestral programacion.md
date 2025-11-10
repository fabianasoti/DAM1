```
''' 
Gestión de la base de datos portafolioexamen con MySQL y Python
2025 Fabiana Victoria Sotillo
Programa que permite insertar, listar, actualizar y eliminar piezas del portafolio 
utilizando una base de datos MySQL conectada mediante la librería mysql.connector.
'''
```

---
En las bases de datos relacionales, es necesario realizar acciones básicas que permitan almacenar, organizar y administrar información de manera estructurada mediante tablas compuestas por filas y columnas. Esto funciona bajo un modelo cliente-servidor y utiliza SQL (Structured Query Language) para interactuar con los datos.

El objetivo de este ejercicio es practicar la aplicación de las operaciones fundamentales de manipulación de datos, conocidas como CRUD (Create, Read, Update, Delete). Mediante la inserción, lectura, actualización y eliminación de registros, se busca comprender cómo se gestionan los datos de manera eficiente y cómo se aplican los conceptos de tipos de datos y restricciones en un entorno relacional. 

Este ejercicio consiste en desarrollar un sistema básico de gestión de la base de datos portafolioexamen, conectándose ala  base de datos MySQL desde un programa en Python, que permite realizar operaciones CRUD (crear, leer, actualizar y eliminar). Se aplican conceptos fundamentales de bases de datos relacionales como claves primarias, foráneas, vistas y permisos de usuario, junto con el manejo de conexión y ejecución de sentencias SQL desde Python mediante la librería mysql.connector. El objetivo práctico es simular la administración de las piezas de un portafolio digital mediante un menú interactivo que gestiona registros en la tabla piezasportafolio.

---
A continuación, se ilustra el paso a paso del ejercicio:

- Se configura el entorno de la base de datos portafolioexamen y se crean las tablas categoriasportafolio y piezasportafolio, con su relación mediante una clave foránea (id_categoria). Luego, se define un usuario de MySQL con permisos específicos sobre dicha base de datos.
```
# Creación del usuario y asignación de permisos en MySQL

CREATE USER 'benito'@'localhost' IDENTIFIED BY 'F0nt4n3r0*';
GRANT USAGE ON *.* TO 'benito'@'localhost';
ALTER USER 'benito'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `portafolioexamen`.* TO 'benito'@'localhost';
FLUSH PRIVILEGES;
```

- Desde Python, el programa se conecta a MySQL utilizando las credenciales del nuevo usuario y ejecuta sentencias SQL dinámicas mediante un cursor. 
```
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",      
    user="benito",    
    password="F0nt4n3r0*",  
    database="portafolioexamen"      
)
cursor = conexion.cursor() 
```
 
- El sistema presenta un menú que ofrece las cuatro operaciones CRUD:
```
print("Gestion de portafolioexamen v0.1")
while True:
  print("Escoge una opcion")
  print("1.-Insertar")
  print("2.-Listar")
  print("3.-Actualizar")
  print("4.-Eliminar")
  opcion = int(input("Escoge una opcion: "))
  print("La opción que has escogido es: ",opcion)
```

- Se definen las opciones dentro de un bucle while True, atrapando sus funciones con condicionales (if, elif)
	- Insertar: agrega una nueva pieza con sus atributos (título, descripción, imagen, URL y categoría).
		```
		   if opcion == 1:
				titulo = input("Introduce el titulo de la nueva pieza del portafolio: ")
				descripcion = input("Introduce la descripcion de la nueva pieza: ")
				fecha = input("Introduce la fecha de la nueva pieza del portafolio: ")
				id_categoria = input("Introduce el id de la categoria a la que pertenece la nueva pieza del portafolio: ")
				cursor.execute("INSERT INTO piezasportafolio VALUES (NULL,'"+titulo+"','"+descripcion+"','"+fecha+"','"+id_categoria+"');")
				conexion.commit()
		```
		
	- Listar: muestra todas las piezas registradas.
		```
		elif opcion == 2:
			cursor.execute("SELECT * FROM piezasportafolio;")
			lineas = cursor.fetchall()
			for linea in lineas:
				print(linea)
		```
		
	- Actualizar: permite modificar los datos de una pieza existente.
		```
		 elif opcion == 3:
				identificador = input("Introduce el Identificador a actualizar: ")
				titulo = input("Introduce el nuevo titulo de la pieza del portafolio: ")
				descripcion = input("Introduce la nueva descripción de la pieza del portafolio: ")
				fecha = input("Introduce la nueva fecha de la pieza del portafolio: ")
				id_categoria = input("Introduce el id de la categoria a la que pertenece la pieza del portafolio a actualizar: ")
				cursor.execute('''
					UPDATE piezasportafolio 
					SET
					titulo = "'''+titulo+'''",
					descripcion = "'''+descripcion+'''",
					fecha = "'''+fecha+'''",
					id_categoria = "'''+id_categoria+'''"
					WHERE Identificador = '''+identificador+''';
				''')
				conexion.commit()
		```
		
	- Eliminar: borra un registro mediante su identificador.
		```
		 elif opcion == 4:
			identificador = input("Introduce el Identificador a eliminar: ")
			cursor.execute("DELETE FROM piezasportafolio portafolio WHERE Identificador = "+identificador+";")
			conexion.commit()
		```
Cada operación ejecuta un commit para guardar los cambios en la base de datos. Se manejan las consultas SQL con concatenación de variables y estructura condicional if/elif para definir el flujo de ejecución según la opción seleccionada.

---
A continuación se muestra el código funcional completo:

```
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",      
    user="benito",    
    password="F0nt4n3r0*",  
    database="portafolioexamen"      
)
cursor = conexion.cursor() 

print("Gestion de portafolioexamen v0.1")
while True:
  print("Escoge una opcion")
  print("1.-Insertar")
  print("2.-Listar")
  print("3.-Actualizar")
  print("4.-Eliminar")
  opcion = int(input("Escoge una opcion: "))
  print("La opción que has escogido es: ",opcion)
  if opcion == 1:
    titulo = input("Introduce el titulo de la nueva pieza del portafolio: ")
    descripcion = input("Introduce la descripcion de la nueva pieza: ")
    fecha = input("Introduce la fecha de la nueva pieza del portafolio: ")
    id_categoria = input("Introduce el id de la categoria a la que pertenece la nueva pieza del portafolio: ")
    cursor.execute("INSERT INTO piezasportafolio VALUES (NULL,'"+titulo+"','"+descripcion+"','"+fecha+"','"+id_categoria+"');")
    conexion.commit()
  elif opcion == 2:
    cursor.execute("SELECT * FROM piezasportafolio;")
    lineas = cursor.fetchall()
    for linea in lineas:
      print(linea)
  elif opcion == 3:
    identificador = input("Introduce el Identificador a actualizar: ")
    titulo = input("Introduce el nuevo titulo de la pieza del portafolio: ")
    descripcion = input("Introduce la nueva descripción de la pieza del portafolio: ")
    fecha = input("Introduce la nueva fecha de la pieza del portafolio: ")
    id_categoria = input("Introduce el id de la categoria a la que pertenece la pieza del portafolio a actualizar: ")
    cursor.execute('''
      UPDATE piezasportafolio 
      SET
      titulo = "'''+titulo+'''",
      descripcion = "'''+descripcion+'''",
      fecha = "'''+fecha+'''",
      id_categoria = "'''+id_categoria+'''"
      WHERE Identificador = '''+identificador+''';
    ''')
    conexion.commit()
  elif opcion == 4:
    identificador = input("Introduce el Identificador a eliminar: ")
    cursor.execute("DELETE FROM piezasportafolio portafolio WHERE Identificador = "+identificador+";")
    conexion.commit()
```

---
El ejercicio permite integrar los fundamentos de bases de datos relacionales con la programación en Python, fortaleciendo la comprensión del manejo de datos a través de sentencias SQL ejecutadas desde código. La práctica del modelo CRUD favorece el desarrollo del pensamiento lógico orientado a la gestión de información, además de permitir una gestión consistente e integral de una base de datos desde un programa en Python, y prepara el terreno para implementar sistemas más complejos con validaciones, manejo de errores y seguridad reforzada en futuras aplicaciones web o de escritorio.
