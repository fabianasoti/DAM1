import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)

cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    NULL,
    "22222222J",
    "Susana",
    "Banana",
    "info@susana.com"   
  );
''')

conexion.commit()

cursor.close()
conexion.close()
