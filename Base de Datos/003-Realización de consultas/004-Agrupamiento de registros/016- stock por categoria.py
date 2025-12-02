import mysql.connector
import matplotlib.pyplot as pt

conexion = mysql.connector.connect(
    host="localhost",
    user="cliente",
    password="Clientes123$",
    database="clientes"
)

cursor = conexion.cursor()

cursor.execute('''
    SELECT nombre, categoria, stock
    FROM productos;
''')

filas = cursor.fetchall()

etiquetas = []
stocks = []

for fila in filas:
    nombre = fila[0]
    categoria = fila[1]
    stock = fila[2]

    etiquetas.append(f"{categoria} - {nombre} ({stock})")
    stocks.append(stock)

print(etiquetas)
print(stocks)

pt.pie(stocks, labels=etiquetas, autopct="%1.1f%%")
pt.title("Stock por producto")
pt.show()

