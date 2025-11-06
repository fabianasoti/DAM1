import mysql.connector

conexion = mysql.connector.connect(	
    host="localhost",      
    user="usuario1",    
    password="Portafolio123$",  
    database="portafolio"      
)

cursor = conexion.cursor()

cursor.execute('''
	SELECT * FROM pieza_categoria;
	'''
)

filas = cursor.fetchall()

for fila in filas:
	print(fila)
