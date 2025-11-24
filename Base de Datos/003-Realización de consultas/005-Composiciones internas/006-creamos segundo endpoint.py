import mysql.connector
from flask import Flask
import json

conexion = mysql.connector.connect(
	host="localhost",
	user="tiendaclase",
	password="F0nt4n3r0*",
	database="tiendaclase"
)                                      
  
app = Flask(__name__)

@app.route("/clientes")
def clientes():
	cursor = conexion.cursor() 
	cursor.execute("SELECT * FROM clientes;")  

	filas = cursor.fetchall()
	return json.dumps(filas)
	
# http://127.0.0.1:5000/clientes

@app.route("/tablas")
def tablas():
	cursor = conexion.cursor() 
	cursor.execute("SHOW TABLES;")  

	filas = cursor.fetchall()
	tablas = []
	for fila in filas:
		tablas.append(fila[0])
	return json.dumps(tablas)

if __name__ == "__main__":
	app.run(debug=True)
	
# http://127.0.0.1:5000/tablas
	

