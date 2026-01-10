import mysql.connector 
import matplotlib.pyplot as plt

conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
cursor = conexion.cursor()

cursor.execute('''
  SELECT 
    COUNT(*) AS numero,
    categoria
  FROM 
    productos
  GROUP BY 
    categoria;
''')

filas = cursor.fetchall()

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

cursor.close()
conexion.close()
