import mysql.connector 

conexion = mysql.connector.connect(
	host="localhost",
	user="tiendaclase",
	password="F0nt4n3r0*",
	database="tiendaclase"
)                                      
  
cursor = conexion.cursor() 
cursor.execute("SELECT * FROM clientes;")  

filas = cursor.fetchall()

print(filas)
