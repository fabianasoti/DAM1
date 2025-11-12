Se ha desarrollado una aplicación web dinámica utilizando Python con Flask, MySQL y HTML/CSS. El objetivo ha sido conectar una base de datos llamada portafolioexamen con una página web que muestra, de forma estructurada, la información contenida en la vista pieza_categoria.

Flask es un microframework que permite crear aplicaciones web ligeras en Python, mientras que MySQL se emplea como sistema gestor de bases de datos para almacenar la información de forma estructurada. Por otro lado, HTML y CSS se utilizan para dar formato y estilo visual a la página resultante.

Este programa combina conceptos de conexión a bases de datos, consultas SQL, estructuras de control en Python y plantillas HTML, permitiendo mostrar datos almacenados en una tabla o vista de manera automática y visualmente organizada.

---
Así pues, se ejemplificará el paso a paso del desarrollo del programa:

- Inicialmente se prepara el entorno y se diseña la base de datos en mysql con sus respectivas tablas (piezasportafolio y categoriasportafolio), claves primarias, foráneas, y vistas cruzadas:
```
DESCRIBE piezasportafolio;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| descripcion   | varchar(100) | YES  |     | NULL    |                |
| fecha         | varchar(100) | YES  |     | NULL    |                |
| id_categoria  | int          | YES  | MUL | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

DESCRIBE categoriasportafolio;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```

- Se genera la vista cruzada de las tablas, que es la que se mostrará finalmente en la página web.
```
CREATE VIEW pieza_categoria AS

SELECT 
piezasportafolio.titulo,
piezasportafolio.descripcion,
categoriasportafolio.nombre
FROM piezasportafolio
LEFT JOIN categoriasportafolio
ON categoriasportafolio.Identificador = piezasportafolio.id_categoria;

SELECT * FROM pieza_categoria;
+----------------------+--------------------------------------------------------------------------------------------+------------------------+
| titulo               | descripcion                                                                                | nombre                 |
+----------------------+--------------------------------------------------------------------------------------------+------------------------+
| Examen 1er Trimestre | En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre | Exámenes Trimestrales  |
+----------------------+--------------------------------------------------------------------------------------------+------------------------+
```

- Luego se generan distintos registros en las dos tablas principales, para que luego, al llamar la vista pieza_categoriaen el programa por Python estas sean interpretadas y aparezca el contenido en la página web gracias también a la estructura de HTML. Por ejemplo:
```
INSERT INTO categoriasportafolio VALUES(
	NULL,
	'Desarrollo web'
);

INSERT INTO piezasportafolio VALUES(
	NULL,
	'Diseño de logotipo moderno',
	'Creación de un logotipo minimalista para una marca de moda sostenible.',
	'15-11-25',
	3
);
```

- Este sería el contenido de la vista (lo que aparecerá en la web del portafolio).
```
SELECT * FROM pieza_categoria;
+------------------------------+--------------------------------------------------------------------------------------------+------------------------+
| titulo                       | descripcion                                                                                | nombre                 |
+------------------------------+--------------------------------------------------------------------------------------------+------------------------+
| Examen 1er Trimestre         | En este apartado se ilustra el desarrollo del examen de base de datos del primer trimestre | Exámenes Trimestrales  |
| Diseño de logotipo moderno   | Creación de un logotipo minimalista para una marca de moda sostenible.                     | Desarrollo web         |
| Desarrollo de portafolio web | Diseño y programación de un sitio web personal con HTML, CSS y Python.                     | Desarrollo web         |
+------------------------------+--------------------------------------------------------------------------------------------+------------------------+
```

- El código comienza importando las librerías necesarias: mysql.connector para gestionar la conexión con la base de datos MySQL y Flask para crear el servidor web.
```
import mysql.connector
from flask import Flask
```
- Luego, se establece la conexión con la base de datos portafolio utilizando las credenciales correspondientes, y se crea un cursor, que permite ejecutar consultas SQL dentro de Python.
```
conexion = mysql.connector.connect(
    host="localhost",      
    user="benito",    
    password="F0nt4n3r0*",  
    database="portafolioexamen"      
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
```
<!doctype html>
<html lang="es">
  <head>
    <title>Fabiana Victoria Sotillo</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    <meta name="description" content="Web de Fabiana Victoria Sotillo, estudiante de DAM, crochetera en su tiempo libre">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="keywords" content="programación,desarrollo,clave3,...">
      <meta name="author" content="Fabiana Victoria Sotillo">
      <link rel="icon" href="kermit cute.jpeg" type="image/jpeg">
      <meta property="og:title" content="Fabiana Victoria Sotillo">
      <meta property="og:description" content="Web de Fabiana Victoria Sotillo, estudiante de DAM.">
      <meta property="og:image" content="kermit cute.jpeg">
      <meta property="og:url" content="https://fabianasotillo.com">
      <meta property="og:type" content="website">
      <style>
        /*
            @font-face{
            font-family: "ubuntu";
            src:url("https://static.jocarsa.com/fuentes/ubuntu-font-family-0.83/Ubuntu-R.ttf");
        */
        @font-face{
            font-family: "ubuntu";
            src:url("BebasNeue-Regular.otf");
        }
        h1{
          color:#333366;
          font-family: "ubuntu";
          src:url("BebasNeue-Regular.otf");
        }
        h2,h3{
          color:#777;
          font-family:monospace;
        }
        body{
          background:#f9f9ff;
        }
        header,main,footer{
          width:750px; /* Establece el fondo de los elementos */
          background:white; /* Establece el fondo de los elementos */
          margin:auto; /* Centralo en la pantalla */
          padding:20px; /* Pon un poco de margen interior */
        }
        #inicio img{
          width:100px;        /* No quiero que la imagen se salga */
        }
        .bloque{
          display:flex; /* El bloque de texto e imagen quiero que sea flex */
          gap:20px; /* Distancia entre los elementos*/
        }
        .bloque img{
          flex:1; /* Ocupa una unidad flex */
          width:50%; /* Ocupa el 50% de la anchura */
          height:50%; /* Ocupa el 50% de la altura */
        }
        .bloque p{
          flex:1; /* Ocupa una unidad flex */
          font-size:10px; /* Edito el tamaño del texto */
          text-align:justify; /* Edito la alineación del texto*/
        }
        #diseño .bloque{
          flex-direction: row-reverse; /* Invertimos el orden  un elemento*/
        }
        #contenedor_portafolio{
          display:grid;   /* Este elemento es una rejilla*/
          grid-template-columns:auto auto; /* Y tiene tres columnas */
          gap:20px; /* Separación entre los elementos */
        }
        #contenedor_portafolio{
          width:100%; /* Quiero que la imagen no desborde */
        }
        #contenedor_portafolio article {
				display: flex;
				align-items: flex-start;
				gap: 15px;
				margin-bottom: 15px;
				background: white;
				padding: 10px;               /* ← margen interno (espaciado interno del artículo) */
				border-radius: 8px;          /* ← bordes redondeados */
				box-shadow: 0 0 4px rgba(0, 0, 0, 0.1); /* ← sombra ligera */
				}
      </style>
  </head>
  <body>
    <header>
      <h1>Fabiana Victoria Sotillo</h1>
      <h3>fabiana.victoria.sotillo@alu.ceacfp.es</h3>
    </header>
    <main>
		  <section id="portafolio">
		    <h3>Portafolio</h3>
		    <div id="contenedor_portafolio">
					<article>
						<h4>'''+fila[0]+'''</h4>
						<p>'''+fila[1]+'''</p>
						<p>'''+fila[2]+'''</p>       
					</article>
		</main>
		<footer>
			<p>&copy; 2025 Fabiana Sotillo</p>
    </footer>
  </body>
</html>
```

-  Luego se va estructurando el código HTML dentro del código de Python, separándolo en secciones para que la aplicación pueda ser ejecutada correctamente. Por lo tanto, a continuación, se construye una cadena donde irá el contenido HTML (cadena) que representa la estructura visual del sitio web. Desde el inicio hasta el main, es decir, hasta antes de la parte del código que se repetirá.
```
	cadena = '''
<!-- Aquí va el contenido html -->
'''
```

- Dentro del bucle for fila in filas:, se genera dinámicamente un bloque ```<article>``` para cada registro de la vista, incorporando los valores de las columnas (como título, descripción, imagen y enlace). Cada iteración del bucle añade un nuevo artículo al HTML, logrando así que el contenido se actualice automáticamente al modificar la base de datos. 
```
	for fila in filas: 
		cadena += '''
			<article>
				<h4>'''+fila[0]+'''</h4>
				<p>'''+fila[1]+'''</p>
				<p>'''+fila[2]+'''</p>       
			</article>
   	'''        
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
    user="benito",    
    password="F0nt4n3r0*",  
    database="portafolioexamen"      
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
    <meta name="description" content="Web de Fabiana Victoria Sotillo, estudiante de DAM, crochetera en su tiempo libre">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="keywords" content="programación,desarrollo,clave3,...">
      <meta name="author" content="Fabiana Victoria Sotillo">
      <link rel="icon" href="kermit cute.jpeg" type="image/jpeg">
      <meta property="og:title" content="Fabiana Victoria Sotillo">
      <meta property="og:description" content="Web de Fabiana Victoria Sotillo, estudiante de DAM.">
      <meta property="og:image" content="kermit cute.jpeg">
      <meta property="og:url" content="https://fabianasotillo.com">
      <meta property="og:type" content="website">
      <style>
        /*
            @font-face{
            font-family: "ubuntu";
            src:url("https://static.jocarsa.com/fuentes/ubuntu-font-family-0.83/Ubuntu-R.ttf");
        */
        @font-face{
            font-family: "ubuntu";
            src:url("BebasNeue-Regular.otf");
        }
        h1{
          color:#333366;
          font-family: "ubuntu";
          src:url("BebasNeue-Regular.otf");
        }
        h2,h3{
          color:#777;
          font-family:monospace;
        }
        body{
          background:#f9f9ff;
        }
        header,main,footer{
          width:750px; /* Establece el fondo de los elementos */
          background:white; /* Establece el fondo de los elementos */
          margin:auto; /* Centralo en la pantalla */
          padding:20px; /* Pon un poco de margen interior */
        }
        #inicio img{
          width:100px;        /* No quiero que la imagen se salga */
        }
        .bloque{
          display:flex; /* El bloque de texto e imagen quiero que sea flex */
          gap:20px; /* Distancia entre los elementos*/
        }
        .bloque img{
          flex:1; /* Ocupa una unidad flex */
          width:50%; /* Ocupa el 50% de la anchura */
          height:50%; /* Ocupa el 50% de la altura */
        }
        .bloque p{
          flex:1; /* Ocupa una unidad flex */
          font-size:10px; /* Edito el tamaño del texto */
          text-align:justify; /* Edito la alineación del texto*/
        }
        #diseño .bloque{
          flex-direction: row-reverse; /* Invertimos el orden  un elemento*/
        }
        #contenedor_portafolio{
          display:grid;   /* Este elemento es una rejilla*/
          grid-template-columns:auto auto; /* Y tiene tres columnas */
          gap:20px; /* Separación entre los elementos */
        }
        #contenedor_portafolio{
          width:100%; /* Quiero que la imagen no desborde */
        }
        #contenedor_portafolio article {
				display: flex;
				align-items: flex-start;
				gap: 15px;
				margin-bottom: 15px;
				background: white;
				padding: 10px;               /* ← margen interno (espaciado interno del artículo) */
				border-radius: 8px;          /* ← bordes redondeados */
				box-shadow: 0 0 4px rgba(0, 0, 0, 0.1); /* ← sombra ligera */
				}
      </style>
  </head>
  <body>
    <header>
      <h1>Fabiana Victoria Sotillo</h1>
      <h3>fabiana.victoria.sotillo@alu.ceacfp.es</h3>
    </header>
    <main>
		  <section id="portafolio">
		    <h3>Portafolio</h3>
		    <div id="contenedor_portafolio">
	'''                               # Creo una cadena vacia
	######### AQUI PONGO LO QUE SE REPITE
	for fila in filas:                        # Para cada elemento de la lista
		cadena += '''
			<article>
				<h4>'''+fila[0]+'''</h4>
				<p>'''+fila[1]+'''</p>
				<p>'''+fila[2]+'''</p>       
			</article>
   	'''                     										# Añado el registro a la cadena
	######### AQUI PONGO EL FINAL
	cadena += '''
	</main>
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
Este código genera una página web con todos los registros de la vista pieza_categoria, mostrando títulos, descripciones,  la categoría de manera dinámica.

Se aplicaron conceptos fundamentales como el uso de vistas SQL, la conexión entre Flask y MySQL, el manejo de consultas y la generación dinámica de contenido HTML desde Python.
Además, se reforzó el uso de estructuras como bucles for, cadenas multilínea y la inclusión de estilos CSS para mejorar la presentación visual. 

El diseño de este programa permite integrar distintos conocimientos de las materias pilares del ciclo; programación, bases de datos y lenguajes de marcas para el diseño de interfaces, y gracias a esto se demuestra que es sumamente útil y práctico comprender cómo realizar un programa consistente e íntegro.

Este tipo de práctica es esencial para comprender cómo se construyen sitios web dinámicos y cómo se relacionan el backend y el frontend, sentando las bases para el desarrollo de aplicaciones web más complejas y completas.
