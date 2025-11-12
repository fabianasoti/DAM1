En este ejercicio se desarrolló una aplicación web dinámica utilizando Python con Flask, MySQL y HTML/CSS. El objetivo fue conectar una base de datos llamada portafolio con una página web que muestra, de forma estructurada, la información contenida en la vista pieza_categoria.

Flask es un microframework que permite crear aplicaciones web ligeras en Python, mientras que MySQL se emplea como sistema gestor de bases de datos para almacenar la información de forma estructurada. Por otro lado, HTML y CSS se utilizan para dar formato y estilo visual a la página resultante.

El ejercicio combina conceptos de conexión a bases de datos, consultas SQL, estructuras de control en Python y plantillas HTML, permitiendo mostrar datos almacenados en una tabla o vista de manera automática y visualmente organizada.

---
Así pues, se ejemplificará el paso a paso del desarrollo del código:

- El código comienza importando las librerías necesarias: mysql.connector para gestionar la conexión con la base de datos MySQL y Flask para crear el servidor web.
```
import mysql.connector
from flask import Flask
```
- Luego, se establece la conexión con la base de datos portafolio utilizando las credenciales correspondientes, y se crea un cursor, que permite ejecutar consultas SQL dentro de Python.
```
conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123$",  
    database="portafolio"      
)																					# Me conecto a la base de datos
                            
cursor = conexion.cursor()                # Creo un cursor
```

- Luego, se define la aplicación Flask y una ruta principal (/) que se encarga de generar la página web. En esta ruta, se ejecuta la consulta "SELECT * FROM pieza_categoria;". Esta instrucción recupera todas las filas de la vista pieza_categoria, que combina datos de las tablas piezasportafolio y categoriasportafolio mediante una unión (JOIN).
```
app = Flask(__name__)                     # Creo una aplicación Flask (web)

@app.route("/")                           # Atrapo la ruta raiz (/)
def holamundo():                          # Defino una funcion
  cursor.execute('''
  SELECT * FROM pieza_categoria;
''')  # Pido el contenido de la vista
```

- Los resultados se almacenan en una lista de Python (filas) que contiene toda la información que se mostrará dinámicamente en la página.
```
	filas = cursor.fetchall() 
```
- Antes de seguir con el código en Python, se ejemplifica cómo está estructurado el código HTML que va dentro del programa:
	- En el ```<head>``` se definen las etiquetas meta (para SEO y redes sociales), los estilos CSS y la fuente personalizada mediante @font-face.
	- En el ```<body>```, se organizan los contenidos en tres secciones principales: ```<header>, <main> y <footer>.```
	- El bloque CSS incluye propiedades como display: flex, grid-template-columns, margin, padding y background, que permiten distribuir los elementos visualmente, ajustar su alineación y mejorar la estética.
	- El uso de Flexbox facilita la disposición lateral de imágenes y texto (.bloque), mientras que Grid se emplea para organizar el portafolio en varias columnas.

-  Luego se va estructurando el código HTML dentro del código de Python, separándolo en secciones para que la aplicación pueda ser ejecutada correctamente. Por lo tanto, a continuación, se construye una cadena donde irá el contenido HTML (cadena) que representa la estructura visual del sitio web. Desde el inicio hasta el main, es decir, hasta antes de la parte del código que se repetirá.
```
	cadena = '''
<!-- Aquí va el contenido html -->
'''
```

- Dentro del bucle for fila in filas:, se genera dinámicamente un bloque ```<article>``` para cada registro de la vista, incorporando los valores de las columnas (como título, descripción, imagen y enlace). Cada iteración del bucle añade un nuevo artículo al HTML, logrando así que el contenido se actualice automáticamente al modificar la base de datos. 
```
	for fila in filas:                        # Para cada elemento de la lista
		cadena += '''
			<article>
				<p>"'''+fila[4]+'''"</p>
				<h4>"'''+fila[0]+'''"</h4>
				<p>"'''+fila[1]+'''"</p>
				<a href= "'''+fila[3]+'''"></a>
				<img src="'''+fila[2]+'''">          
			</article>
```

- Finalmente, se cierra la estructura HTML y se devuelve la cadena completa como respuesta del servidor.
```
cadena += '''</main>
    <footer>
          <p>&copy; 2025 Fabiana Sotillo</p>
    </footer>
  </body>
</html>
	'''
	return cadena                             # Devuelvo la cadena como HTML en la web

if __name__ == "__main__":                # Si este es el archivo principal
    app.run(debug=True)                   # Ejecuta la web	
```
	
---
A continuación se ilustra el código funcional completo:
```
''' 
Integración Flask y MySQL con plantilla HTML
2025 Fabiana Victoria Sotillo
Programa que conecta una base de datos MySQL con Flask y muestra 
de forma dinámica los registros de una vista llamada pieza_categoria 
dentro de una página web con estructura y estilos en HTML y CSS.
'''

import mysql.connector                    # Importo el conector a base de datos
from flask import Flask                   # Importo la libreria Flask

conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123$",  
    database="portafolio"      
)																					# Me conecto a la base de datos
                            
cursor = conexion.cursor()                # Creo un cursor
app = Flask(__name__)                     # Creo una aplicación Flask (web)

@app.route("/")                           # Atrapo la ruta raiz (/)
def holamundo():                          # Defino una funcion
	cursor.execute('''
  SELECT * FROM pieza_categoria;
''')  # Pido el contenido de la vista

	filas = cursor.fetchall()                 # Lo guardo en una lista
	######### AQUI PONGO EL INICIO HASTA EL MAIN
	cadena = '''
	<!doctype html>
<html lang="es">
  <head>
    <title>Fabiana Victoria Sotillo</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    <meta name="description" content="Web de Fabiana Victoria Sotillo Cuevas, estudiante de DAM, crochetera en su tiempo libre">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="keywords" content="programación,desarrollo,clave3,...">
      <meta name="author" content="Fabiana Victoria Sotillo">
      <link rel="icon" href="kermit cute.jpeg" type="image/jpeg">
      <meta property="og:title" content="Fabiana Victoria Sotillo">
      <meta property="og:description" content="Web de Fabiana Victoria Sotillo Cuevas, estudiante de DAM, crochetera en su tiempo libre">
      <meta property="og:image" content="kermit cute.jpeg">
      <meta property="og:url" content="https://fabianasotillo.com">
      <meta property="og:type" content="website">
      <style>
        @font-face{
            font-family: "ubuntu";
            src:url("BebasNeue-Regular.otf");
        }
        h1{
          color:MediumSlateBlue;
          font-family: "ubuntu";
        }
        h2,h3{
          color:MediumSlateBlue;
          font-family:monospace;
        }
        body{
          background:Lavender;
        }
        header,main,footer{
          width:750px;
          background:white;
          margin:auto;
          padding:20px;
        }
        #inicio img{
          width:100px;
        }
        .bloque{
          display:flex;
          gap:20px;
        }
        .bloque img{
          flex:1;
          width:50%;
          height:50%;
        }
        .bloque p{
          flex:1;
          font-size:10px;
          text-align:justify;
        }
        #diseño .bloque{
          flex-direction: row-reverse;
        }
        #contenedor_portafolio{
          display:grid;
          grid-template-columns:auto auto auto;
          gap:20px;
        }
        #contenedor_portafolio{
          width:100%;
        }
        form{
          display:flex;
          flex-direction:column;
          flex:1;
          gap:10px;
        }
      </style>
  </head>
  <body>
    <header>
      <h1>Fabiana Victoria Sotillo</h1>
      <h2>fabiana.victoria.sotillo@alu.ceacfp.es</h2>
    </header>
    <main>
	'''                               # Creo una cadena vacia
	######### AQUI PONGO LO QUE SE REPITE
	for fila in filas:                        # Para cada elemento de la lista
		cadena += '''
			<article>
				<p>"'''+fila[4]+'''"</p>
				<h4>"'''+fila[0]+'''"</h4>
				<p>"'''+fila[1]+'''"</p>
				<a href= "'''+fila[3]+'''"></a>
				<img src="'''+fila[2]+'''">          
			</article>
   	'''                     										# Añado el registro a la cadena
	######### AQUI PONGO EL FINAL
	cadena += '''</main>
    <footer>
          <p>&copy; 2025 Fabiana Sotillo</p>
    </footer>
  </body>
</html>
	'''
	return cadena                             # Devuelvo la cadena como HTML en la web

if __name__ == "__main__":                # Si este es el archivo principal
    app.run(debug=True)                   # Ejecuta la web	
```

---
Este código genera automáticamente una página web con todos los registros de la vista pieza_categoria, mostrando títulos, descripciones, imágenes y enlaces de manera dinámica.

El ejercicio permitió integrar distintos conocimientos de las materias pilares del ciclo; programación, bases de datos y lenguajes de marcas para el diseño de interfaces. Se aplicaron conceptos fundamentales como el uso de vistas SQL, la conexión entre Flask y MySQL, el manejo de consultas y la generación dinámica de contenido HTML desde Python.
Además, se reforzó el uso de estructuras como bucles for, cadenas multilínea y la inclusión de estilos CSS para mejorar la presentación visual. 

Este tipo de práctica es esencial para comprender cómo se construyen sitios web dinámicos y cómo se relacionan el backend y el frontend, sentando las bases para el desarrollo de aplicaciones web más complejas y completas.