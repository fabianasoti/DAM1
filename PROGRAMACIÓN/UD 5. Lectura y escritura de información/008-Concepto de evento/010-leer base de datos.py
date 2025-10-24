# pip3 install mysql-connector-python --break system-packages
# sudo apt install libmysqlclient-dev python3-mysql.connector
# solo si da error de ssl en socket:
# pip3 install --user --upgrade mysql-connector-python --break-system-packages

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)

cursor = conexion.cursor()
cursor.execute('''
 SELECT * FROM clientes; 
  );
''')

filas = cursor.fetchall()
for fila in filas:
 	print(fila)


cursor.close()
conexion.close()
