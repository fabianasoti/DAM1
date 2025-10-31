# Importamos libreria 
# Permite trabajar con bases de datos SQLite desde Python.
import sqlite3

# Nos conectamos a la base de datos
# Crea (si no existe) o abre una conexión al archivo de base de datos llamado empresa.db.
# Esta conexión es el vínculo entre el script de Python y la base de datos.
conexion = sqlite3.connect("empresa.db")

# Creamos un cursor,
# que es un objeto que permite ejecutar sentencias SQL 
# (como SELECT, INSERT, UPDATE, DELETE, etc.) y obtener resultados.
cursor = conexion.cursor()

# Ejecuta una consulta SQL que selecciona todas las filas y columnas de la tabla clientes.
# Es decir, está pidiendo todos los registros almacenados en esa tabla.
cursor.execute('''
    SELECT * FROM clientes;
''')

# Recupera todas las filas resultantes de la consulta y las guarda en una lista llamada filas.
# Cada elemento de la lista representa una fila (registro), normalmente como una tupla.
filas = cursor.fetchall()

# Recorre la lista de resultados y muestra cada registro por pantalla.
for fila in filas:
    print(fila)

# Lanzamos la petición
# Se usa para guardar cambios en la base de datos (INSERT, UPDATE, DELETE).
conexion.commit()
