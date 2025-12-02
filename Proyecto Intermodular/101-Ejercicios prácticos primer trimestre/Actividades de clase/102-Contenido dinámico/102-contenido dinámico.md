```
''' 
Blog personal
2025 Fabiana Victoria Sotillo
Programa que crea un blog personal web con JSON y  HTML mediante Flask.
'''
```

---
Este ejercicio tiene como finalidad practicar la creación de un servidor web dinámico utilizando Flask. Flask permite generar contenido web desde Python, combinando la lógica del servidor con la generación de páginas HTML personalizadas. En este caso, el proyecto consiste en un blog que muestra artículos almacenados en un archivo JSON, el cual es leído y procesado por el servidor para generar la estructura HTML de manera dinámica. 

A través de esta práctica, se busca afianzar los conocimientos sobre la manipulación de archivos JSON, la generación de contenido web desde Python y el uso de Flask como herramienta para construir aplicaciones ligeras y funcionales. Además, el ejercicio permite aplicar conceptos de diseño web mediante el uso de CSS embebido en la plantilla HTML.

---
El proyecto está compuesto principalmente por dos archivos:

1. En blog.json, los artículos se organizan como una lista de objetos, cada uno con las claves: titulo, fecha, autor y contenido. Esta estructura permite que los datos se lean fácilmente con la librería json y que puedan procesarse en un bucle dentro del programa para generar dinámicamente las secciones del blog.
```
[
	{
		"titulo":"Primer artículo",
		"fecha":"2025-10-16",
		"autor":"Fabiana Sotillo",
		"contenido":"Este es el contenido del primer artículo"
	},
	{
		"titulo":"Segundo artículo",
		"fecha":"2025-10-16",
		"autor":"Fabiana Sotillo",
		"contenido":"Este es el contenido del segundo artículo"
	},
	{
		"titulo":"Tercero artículo",
		"fecha":"2025-10-16",
		"autor":"Fabiana Sotillo",
		"contenido":"Este es el contenido del tercer artículo"
	},
	{
		"titulo":"Cuarto artículo",
		"fecha":"2025-10-16",
		"autor":"Fabiana Sotillo",
		"contenido":"Este es el contenido del cuarto artículo"
	}
]
```

2. En el archivo servidor.py, 

- Se importa el módulo Flask y la librería json. 
```
from flask import Flask
import json
```

- Se crea una instancia del servidor con ```aplicacion = Flask(__name__)``` y se define una ruta principal con el decorador @aplicacion.route("/"), que ejecuta la función raiz(). Dentro de esta función, se construye una cadena HTML que servirá como la página web del blog.
```
aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
##################################### Este es un bloque
    cadena = '''
    <!doctype html>
		# ... el código continúa
```

- Primero, se define el encabezado y el estilo básico utilizando CSS interno para configurar el color de fondo, el tipo de letra y la disposición de los elementos. Luego, se abre el archivo blog.json y se cargan sus datos con json.load(archivo). 
```
 cadena = '''
    <!doctype html>
<html lang="es">
  <head>
    <title>FABIANAblog</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
      header,footer{text-align:center;}
      main{color:black;}
    </style>
  </head>
  <body>
    <header><h1>FABIANAblog</h1></header>
    <main>
    '''
    #################################### Otro bloque que se repite
    archivo = open("blog.json", 'r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
```

- Por cada artículo dentro de la lista, el código genera un bloque ```<article>``` con el título, fecha, autor y contenido. 
```
 <article>
            <h3>'''+linea['titulo']+'''</h3>
            <time>'''+linea['fecha']+'''</time>
            <p>'''+linea['autor']+'''</p>
            <p>'''+linea['contenido']+'''</p>
          </article>
```

- Finalmente, se completa el HTML con un pie de página y se devuelve la cadena completa mediante la instrucción return.
```
  <footer>(c)2025 Fabiana Victoria Sotillo</footer>
  </body>
</html>
    '''
    ###########
    return cadena
```

---
A continuación se muestra el código funcional completo:
```
''' 
Blog personal
2025 Fabiana Victoria Sotillo
Programa que crea un blog personal web con JSON y  HTML mediante Flask.
'''

# Abre una terminal e instala flask:
# pip install flask
# Flask es un microservidor web que nos permite generar HTML desde Python

from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
##################################### Este es un bloque
    cadena = '''
    <!doctype html>
<html lang="es">
  <head>
    <title>FABIANAblog</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
      header,footer{text-align:center;}
      main{color:black;}
    </style>
  </head>
  <body>
    <header><h1>FABIANAblog</h1></header>
    <main>
    '''
    #################################### Otro bloque que se repite
    archivo = open("blog.json", 'r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
          <article>
            <h3>'''+linea['titulo']+'''</h3>
            <time>'''+linea['fecha']+'''</time>
            <p>'''+linea['autor']+'''</p>
            <p>'''+linea['contenido']+'''</p>
          </article>
          '''
     ######################################### Otro bloque más
    cadena += '''
    </main>
    <footer>(c)2025 Fabiana Victoria Sotillo</footer>
  </body>
</html>
    '''
    #####################################
    return cadena

# Ahora arranco el servidor
if __name__== "__main__":
    aplicacion.run(debug="True")
```

El servidor se ejecuta con aplicacion.run(debug=True), lo que permite acceder al blog localmente a través del navegador y ver los artículos generados dinámicamente.

---
El ejercicio permitió consolidar el uso de Flask para generar páginas web dinámicas a partir de datos almacenados en JSON, integrando lógica de programación y diseño web en un mismo entorno. Se aplicaron conceptos esenciales como la lectura de archivos, el manejo de estructuras de datos en Python y la construcción de HTML dentro de Python. Asimismo, se reforzó la comprensión del flujo cliente-servidor en aplicaciones web y la capacidad de crear interfaces funcionales y personalizables. Este tipo de práctica representa un paso fundamental en la formación de habilidades para el desarrollo web, ya que combina programación, diseño y estructura de información en un proyecto práctico.