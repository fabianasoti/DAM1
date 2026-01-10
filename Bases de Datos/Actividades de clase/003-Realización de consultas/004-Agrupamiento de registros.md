```
'''
Agrupación de productos por categoría y visualización de datos
2026 Fabiana Victoria Sotillo
Programa que se conecta a una base de datos MySQL  y representa los resultados mediante
un gráfico de barras utilizando la librería matplotlib desde Python
'''
```

---
El presente ejercicio tiene como objetivo aplicar el concepto de agrupamiento de registros en una base de datos MySQL mediante la cláusula GROUP BY, así como reforzar la visualización de datos utilizando Python y la librería matplotlib. A través de la conexión a una base de datos llamada clientes, se realiza una consulta que permite contar cuántos productos existen por cada categoría, procesar los resultados en Python y representarlos gráficamente mediante un gráfico de barras. De este modo, se busca comprender cómo agrupar información, analizar resultados y presentarlos de forma visual para facilitar su interpretación y toma de decisiones.

---
En esta actividad se establece una conexión entre Python y una base de datos MySQL utilizando la librería mysql.connector. Una vez conectados, se ejecuta una consulta SQL que agrupa los productos por su categoría y cuenta el número de registros en cada grupo mediante la función COUNT(*) junto con la cláusula GROUP BY.

Posteriormente, los resultados obtenidos se recorren mediante un bucle para mostrar por pantalla el número de productos por categoría. A continuación, se emplea la librería matplotlib para representar estos datos mediante un gráfico de barras, permitiendo visualizar de forma clara la distribución de productos según su categoría. Finalmente, se cierra la conexión a la base de datos para garantizar un uso correcto de los recursos del sistema.

---
A continuación, se presenta el procedimiento utilizado en el ejercicio junto con su explicación.

```
'''
Agrupación de productos por categoría y visualización de datos
2026 Fabiana Victoria Sotillo
Programa que se conecta a una base de datos MySQL  y representa los resultados mediante
un gráfico de barras utilizando la librería matplotlib desde Python
'''

import mysql.connector 
import matplotlib.pyplot as plt

# Conexión a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
cursor = conexion.cursor()

# Consulta agrupada por categoría
cursor.execute('''
  SELECT 
    COUNT(*) AS numero,
    categoria
  FROM 
    productos
  GROUP BY 
    categoria;
''')

# Obtener los resultados
filas = cursor.fetchall()

# Mostrar resultados por consola
for fila in filas:
  print("Categoría: ", fila[1], "Número de productos: ", fila[0])
  
# Datos para el gráfico
cantidades = []
etiquetas = []

for fila in filas:
  cantidades.append(fila[0])
  etiquetas.append(fila[1])

# Crear un gráfico de barras
plt.bar(etiquetas, cantidades)
plt.xlabel('Categoría')
plt.ylabel('Número de productos')
plt.title('Distribución de productos por categoría')
plt.show()

# Cierre de la conexión
cursor.close()
conexion.close()
```

---
1. Conexión a la base de datos
import mysql.connector
```
# Conexión a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
cursor = conexion.cursor()
```
Este bloque de código permite establecer la conexión entre Python y la base de datos MySQL llamada clientes, utilizando las credenciales correspondientes y creando un cursor para ejecutar consultas.


2. Consulta agrupada por categoría
```
# Consulta agrupada por categoría
cursor.execute('''
  SELECT 
    COUNT(*) AS numero,
    categoria
  FROM 
    productos
  GROUP BY 
    categoria;
''')
```
Esta consulta utiliza la función COUNT(*) para contar el número de productos y la cláusula GROUP BY para agruparlos según su categoría.


3. Procesamiento y visualización de resultados por consola
```
# Procesando y mostrando los resultados
filas = cursor.fetchall()

for fila in filas:
  print("Categoría: ", fila[1], "Número de productos: ", fila[0])
```
Este bucle recorre los resultados obtenidos de la consulta y muestra por pantalla el nombre de la categoría junto con el número de productos correspondiente.


4. Visualización de datos con gráfico de barras
import matplotlib.pyplot as plt
```
# Datos para el gráfico
cantidades = []
etiquetas = []

for fila in cursor.fetchall():
  cantidades.append(fila[0])
  etiquetas.append(fila[1])

# Crear un gráfico de barras
plt.bar(etiquetas, cantidades)
plt.xlabel('Categoría')
plt.ylabel('Número de productos')
plt.title('Distribución de productos por categoría')
plt.show()
```
Este bloque permite almacenar los datos obtenidos en listas y generar un gráfico de barras que representa visualmente la distribución de productos por categoría.

5. Cierre de la conexión
```
cursor.close()
conexion.close()
```
Estas instrucciones cierran correctamente la conexión con la base de datos y liberan los recursos utilizados.

---
Como resultado del ejercicio, se obtiene un listado con el número de productos por cada categoría y una representación gráfica en forma de gráfico de barrasque permite observar de forma visual cómo se distribuyen los productos dentro de la base de datos.

En este ejercicio se han aplicado los conceptos de conexión a bases de datos, ejecución de consultas SQL con la cláusula GROUP BY, procesamiento de resultados mediante estructuras de control en Python y visualización de datos con la librería matplotlib. Esta práctica permite comprender cómo agrupar información almacenada en una base de datos, analizarla de forma estructurada y representarla visualmente para facilitar su interpretación. Asimismo, refuerza la lógica de programación y el uso de herramientas fundamentales para el análisis de datos, constituyendo una base sólida para el desarrollo de aplicaciones y sistemas más complejos.
