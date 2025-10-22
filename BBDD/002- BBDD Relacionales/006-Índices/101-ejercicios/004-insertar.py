# Importamos libreria
import sqlite3

# Nos conectamos a la base de datos
conexion = sqlite3.connect("empresa.db")

# Creamos un cursor
cursor =conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
''')

#Ejecutamos una sentencia
cursor.execute('''
    INSERT INTO clientes VALUES(
        NULL, 'Fabiana', 'Sotillo Cuevas', 'info@fabiana.com'
);
''')

# Lanzamos la petición
conexion.commit()
