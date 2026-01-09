import matplotlib.pyplot as pt

# Datos de ejemplo (reemplaza con tus datos reales)
edades = [45, 46, 34, 29]
nombres = ['Juan', 'Javier', 'Ana', 'María']

# Crear gráfico de pastel
pt.pie(edades, labels=nombres, autopct='%1.1f%%')
pt.axis('equal')  # Para que el gráfico sea circular

# Mostrar gráfico
pt.show()
