from flask import Flask, render_template 
import mysql.connector                  # Importamos mysql
########################MYSQL##########################################
conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123$",  
    database="portafolio"      
)																					# Me conecto a la base de datos
                            
cursor = conexion.cursor()  							# Creo un cursos MySQL
#--------------------ESTO ENVÍA LAS TABLAS---------------------------
cursor.execute("SHOW TABLES;")						# Muestra las tablas de la base de datos
tablas = []																# Creo una lista vacía
filas = cursor.fetchall()									# Lo guardo en una lista
for fila in filas:												# Recorro el resultado
	tablas.append(fila[0])									# Lo añado a la lista de tablas
#----------------ESTO ENVÍA LAS CABECERAS DE LAS TABLAS---------------
cursor.execute("SHOW COLUMNS in Pieza;")	# Muestra las tablas de la base de datos
columnas = []																# Creo una lista vacía
filas = cursor.fetchall()									# Lo guardo en una lista
for fila in filas:												# Recorro el resultado
	columnas.append(fila[0])									# Lo añado a la lista de tablas
########################################################################

app = Flask(__name__)

@app.route("/")
def holamundo():
	return render_template("backoffice.html",mis_tablas = tablas)	# Envio las tablas a HTMl
	
if __name__ == "__main__":
	app.run(debug=True)
