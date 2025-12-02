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