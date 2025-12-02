import mysql.connector														# Importo el conector a base de datos

conexion = mysql.connector.connect(	
    host="localhost",      
    user="usuario1",    
    password="Portafolio123$",  
    database="portafolio"      
)																									# Me conecto a la base de datos

cursor = conexion.cursor() 												# Creo un cursor

cursor.execute('''
	SELECT * FROM pieza_categoria;
	'''
)																									# Pido el contenido de la lista

filas = cursor.fetchall()													# Lo guardo en una lista

for fila in filas:																# Para cada elemento de la lista
	print(fila)																			# Lo pinto en pantalla
