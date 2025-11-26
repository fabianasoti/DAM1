import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="composiciones4",
  password="ComposicionS14T325342523$",
  database="composiciones"
)                                      

  
cursor = conexion.cursor(dictionary=True) 
cursor.execute("SELECT * FROM matriculas_join;")  

filas = cursor.fetchall()

print(filas)
