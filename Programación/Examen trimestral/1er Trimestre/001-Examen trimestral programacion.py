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
