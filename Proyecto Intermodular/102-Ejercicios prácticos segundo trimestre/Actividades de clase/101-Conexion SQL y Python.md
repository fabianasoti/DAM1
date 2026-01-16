En este ejercicio se trabaja el acceso a bases de datos MySQL desde Python utilizando la librería mysql.connector, aplicando los conceptos de conexión, ejecución de consultas SQL, proyección de campos, ordenación de resultados y recuperación de datos en forma de diccionario. La proyección permite seleccionar únicamente los campos necesarios de una tabla, asignándoles alias legibles, mientras que la ordenación organiza los resultados según un criterio determinado. Por su parte, el uso de cursores con resultados en formato diccionario facilita el acceso a los datos mediante claves en lugar de índices, mejorando la legibilidad y manipulación de la información. El objetivo del ejercicio es aprender a realizar consultas estructuradas y manejar los resultados de forma eficiente desde Python.

---
El proyecto se compone de tres archivos principales que trabajan de forma progresiva:

1. Conexión a la base de datos

Se establece la conexión con la base de datos clientes utilizando la plantilla proporcionada. Esta conexión permite ejecutar consultas SQL desde Python y obtener los resultados.

Se utilizan los siguientes elementos:

- mysql.connector.connect() para crear la conexión

- cursor() para ejecutar sentencias SQL

- fetchall() para recuperar los datos

2. Proyección y ordenación

En este paso se ejecuta una consulta SQL que:

- Selecciona únicamente los campos nombre, apellidos y edad

- Asigna alias legibles a cada campo

- Ordena los resultados por edad en orden descendente (ORDER BY edad DESC)

Esto permite obtener una vista clara y organizada de los datos.

3. Resultado como diccionario

Finalmente, se modifica el cursor para que devuelva los resultados como diccionarios utilizando el parámetro:
```
cursor = conexion.cursor(dictionary=True)
```

De esta forma, cada fila se representa como un diccionario donde las claves son los alias definidos en la consulta SQL, facilitando su acceso y manipulación.

---
Estos son los archivos que se han utilizado en el desarrollo del ejercicio.

1. 003-plantilla de conexion.py
```
''' 
Conexión a base de datos MySQL
2026 Fabiana Victoria Sotillo
Programa que establece una conexión con la base de datos clientes y muestra todos los registros,
utilizando la librería mysql.connector para ejecutar una consulta básica.
'''
import mysql.connector 

# Establecemos la conexión con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="clientes",
    password="Clientes123$",
    database="clientes"
)

# Creamos el cursor
cursor = conexion.cursor()

# Ejecutamos una consulta SQL
cursor.execute("SELECT * FROM clientes;")

# Recuperamos todas las filas
filas = cursor.fetchall()

# Mostramos los resultados
print(filas)
```

2. 004-proyeccion y ordenacion.py
```
''' 
Proyección y ordenación de datos
2026 Fabiana Victoria Sotillo
Programa que realiza una consulta SQL proyectando campos específicos de la tabla clientes,
asignándoles alias legibles y ordenando los resultados por edad de forma descendente.
'''
import mysql.connector 

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="clientes",
    password="Clientes123$",
    database="clientes"
)

# Creamos el cursor
cursor = conexion.cursor()

# Ejecutamos la consulta con proyección y ordenación
cursor.execute('''
    SELECT
        nombre AS "Nombre del cliente",
        apellidos AS "Apellidos del cliente",
        edad AS "Edad del cliente"
    FROM clientes
    ORDER BY edad DESC;
''')

# Recuperamos los resultados
filas = cursor.fetchall()

# Mostramos los resultados
print(filas)
```

3. 005-resultado como diccionario.py
```
''' 
Resultado como diccionario en MySQL
2025 Fabiana Victoria Sotillo
Programa que ejecuta una consulta SQL con proyección y ordenación, recuperando los resultados
como diccionarios para facilitar su acceso y manipulación desde Python.
'''
import mysql.connector 

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="clientes",
    password="Clientes123$",
    database="clientes"
)

# Creamos el cursor en modo diccionario
cursor = conexion.cursor(dictionary=True)

# Ejecutamos la consulta SQL
cursor.execute('''
    SELECT
        nombre AS "Nombre del cliente",
        apellidos AS "Apellidos del cliente",
        edad AS "Edad del cliente"
    FROM clientes
    ORDER BY edad DESC;
''')

# Recuperamos todas las filas como diccionarios
filas = cursor.fetchall()

# Mostramos los resultados
for fila in filas:
    print(fila)
```

---
Los resultados finales de la ejecución del programa, muestra que este devuelve una lista de diccionarios con la siguiente estructura:
```
{
 'Nombre del cliente': 'Ana',
 'Apellidos del cliente': 'García López',
 'Edad del cliente': 42
}
```
Esto permite acceder a los valores por clave, por ejemplo:
```
fila["Nombre del cliente"]
fila["Edad del cliente"]
```

---
En este ejercicio se ha trabajado la conexión entre Python y MySQL mediante la librería mysql.connector, aplicando consultas SQL con proyección de campos y ordenación de resultados. Se ha aprendido a seleccionar únicamente la información relevante de una tabla, asignar alias legibles a los campos y organizar los datos según un criterio específico. Además, se ha utilizado un cursor configurado en modo diccionario para representar cada fila como un conjunto clave-valor, lo que facilita el acceso y la manipulación de la información. Este ejercicio refuerza los fundamentos del acceso a bases de datos desde Python y sienta las bases para el desarrollo de aplicaciones más complejas que requieren interacción con sistemas gestores de bases de datos.
