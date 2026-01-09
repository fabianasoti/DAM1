```
'''
Consultas de resumen
2026 Fabiana Sotillo
Uso de funciones agregadas y matemáticas como AVG, ROUND, FLOOR y CEIL en SQL.
'''
```

---
El presente ejercicio tiene como finalidad aplicar funciones de redondeo y consultas avanzadas en una base de datos MySQL, así como reforzar la obtención de información estadística a partir de los datos almacenados. Mediante el uso de funciones agregadas y matemáticas como AVG, ROUND, FLOOR y CEIL, se calcula el promedio de edad de los clientes con distintos criterios de redondeo. Asimismo, se emplean consultas de ordenación para identificar al cliente de mayor edad y se introduce la visualización de datos mediante gráficos utilizando la librería matplotlib en Python, con el objetivo de mejorar la interpretación de la información obtenida.

En esta actividad se trabaja con una base de datos llamada clientes, a la cual se accede mediante la terminal utilizando el gestor MySQL. Una vez establecida la conexión, se realizan consultas para calcular el promedio de edad de los clientes utilizando funciones de redondeo que permiten obtener valores enteros aproximados según distintos criterios: redondeo al entero más cercano, redondeo hacia abajo y redondeo hacia arriba.

Posteriormente, se utiliza la cláusula ORDER BY junto con DESC y LIMIT para ordenar los registros por edad de forma descendente y seleccionar únicamente el cliente de mayor edad. Finalmente, se introduce el uso de la librería matplotlib en Python para representar los datos en forma de gráfico de pastel, facilitando así la visualización y el análisis de la información obtenida a partir de la base de datos.

---
A continuación, se presentan las consultas y el procedimiento utilizados en el ejercicio.

1. Conexión a la base de datos
```
sudo mysql -u root -p
```
Este comando permite acceder a MySQL desde la terminal y conectarse a la base de datos correspondiente.

2. Cálculo del promedio de edad con redondeo al entero más cercano
```
SELECT ROUND(AVG(edad)) FROM clientes;
```
Esta consulta calcula el promedio de la columna edad y utiliza la función ROUND para redondear el resultado al número entero más cercano.
```
+------------------+
| ROUND(AVG(edad)) |
+------------------+
|               37 |
+------------------+
```

3. Cálculo del promedio de edad con redondeo hacia abajo
```
SELECT FLOOR(AVG(edad)) FROM clientes;
```
En esta consulta se emplea la función FLOOR, que redondea el promedio de edad hacia el entero inferior más cercano.
```
+------------------+
| FLOOR(AVG(edad)) |
+------------------+
|               37 |
+------------------+
```

4. Cálculo del promedio de edad con redondeo hacia arriba
```
SELECT CEIL(AVG(edad)) FROM clientes;
```
Esta consulta utiliza la función CEIL para redondear el promedio de edad hacia el entero superior más cercano.
```
+-----------------+
| CEIL(AVG(edad)) |
+-----------------+
|              38 |
+-----------------+
```

5. Identificación del cliente de mayor edad
```
SELECT nombre, apellidos, edad 
FROM clientes 
ORDER BY edad DESC 
LIMIT 1;
```
Esta consulta ordena los clientes por edad de forma descendente y muestra únicamente el primer registro, que corresponde al cliente de mayor edad.
```
+---------+------------+------+
| nombre  | apellidos  | edad |
+---------+------------+------+
| Alberto | Domínguez  |   53 |
+---------+------------+------+
```

6. Visualización de datos con gráfico de pastel en Python

Para representar los datos gráficamente, se utiliza la librería matplotlib, que permite crear gráficos en forma de tarta.

Para ello, primero es necesaria la instalación de la librería:
```
pip3 install matplotlib --break-system-packages
```

Se utiliza el siguiente código en python para generar un gráfico de pastel:
```
import matplotlib.pyplot as pt

# Datos de ejemplo (sacados de la base de datos clientes)
edades = [45, 46, 34, 29]
nombres = ['Juan', 'Javier', 'Ana', 'María']

# Crear gráfico de pastel
pt.pie(edades, labels=nombres, autopct='%1.1f%%')
pt.axis('equal')  # Para que el gráfico sea circular

# Mostrar gráfico
pt.show()
```

Este pequeño bloque de código permite representar visualmente las edades de los clientes mediante un gráfico de pastel, facilitando la interpretación de los datos. Este se presneta en una pequeña pestaña y gracias a la librería matplotlib, permite que la imagen sea guardada en formato PNG.

---
Como añadido extra, a continuación se muestra el gráfico pastel, convertido a formato SVG para su correcta visualización en un visor de MarkDown:

<svg width="400" height="320" viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="400" fill="white" />
  <g transform="translate(250, 200)">
    <path d="M 0 0 L -40.6 -144.4 A 150 150 0 0 0 -126.1 81.4 Z" fill="#ff7f0e" />
    <text x="-80" y="-30" font-family="Arial" font-size="14" text-anchor="middle">29.9%</text>
    <text x="-160" y="-50" font-family="Arial" font-size="16" text-anchor="end">Javier</text>
    <path d="M 0 0 L -126.1 81.4 A 150 150 0 0 0 56.9 138.8 Z" fill="#2ca02c" />
    <text x="-30" y="80" font-family="Arial" font-size="14" text-anchor="middle">22.1%</text>
    <text x="-80" y="140" font-family="Arial" font-size="16" text-anchor="end">Ana</text>
    <path d="M 0 0 L 56.9 138.8 A 150 150 0 0 0 150 0 Z" fill="#d62728" />
    <text x="75" y="65" font-family="Arial" font-size="14" text-anchor="middle">18.8%</text>
    <text x="160" y="100" font-family="Arial" font-size="16" text-anchor="start">María</text>
    <path d="M 0 0 L 150 0 A 150 150 0 0 0 -40.6 -144.4 Z" fill="#1f77b4" />
    <text x="65" y="-55" font-family="Arial" font-size="14" text-anchor="middle">29.2%</text>
    <text x="160" y="-100" font-family="Arial" font-size="16" text-anchor="start">Juan</text>
  </g>
</svg>

---
Como resultado de las consultas SQL, se obtiene el promedio de edad de los clientes utilizando distintos métodos de redondeo, así como la identificación del cliente de mayor edad de la base de datos. Además, mediante el uso de Python y matplotlib, se logra una representación gráfica de los datos que permite analizarlos de forma visual.

Este ejercicio permite aplicar funciones de redondeo y consultas de ordenación en MySQL para obtener información estadística a partir de una base de datos. Asimismo, se refuerza el uso de funciones agregadas como AVG y se introduce la visualización de datos mediante gráficos, lo que facilita su análisis e interpretación. Estas herramientas resultan fundamentales para el manejo y análisis de información en bases de datos, y constituyen una base sólida para el desarrollo de consultas más avanzadas y sistemas de análisis de datos más complejos.
