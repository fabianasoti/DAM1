# Para conectarnos, creamos usuario
'''
-- crea usuario nuevo con contraseña
CREATE USER 
'usuario1'@'localhost' 
IDENTIFIED  BY 'Portafolio123$';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'usuario1'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'usuario1'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `portafolio`.* 
TO 'usuario1'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
'''

import mysql.connector

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
  print("La opción que has escogido es: ",opcion)
  if opcion == 1:
    titulo = input("Introduce el titulo de la nueva pieza: ")
    descripcion = input("Introduce la descripcion de la nueva pieza: ")
    imagen = input("Introduce el nombre de la imagen de la nueva pieza: ")
    url = input("Introduce la url de la nueva pieza: ")
    cursor.execute("INSERT INTO Pieza VALUES (NULL,'"+titulo+"','"+descripcion+"','"+imagen+"','"+url+"', 1);")
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
