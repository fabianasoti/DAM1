En este ejercicio se aplican los fundamentos del microframework Flask para crear un servidor web básico en Python. Flask permite desarrollar aplicaciones web ligeras y escalables utilizando estructuras sencillas basadas en rutas. El propósito de esta práctica es comprender cómo iniciar un servidor local, devolver contenido HTML desde Python y generar una página dinámica mediante la estructura de control for. Además, se refuerza el uso de estilos CSS integrados en código HTML y la concatenación de cadenas para construir contenido dinámico.

El proceso se dividió en tres etapas principales:

1. Instalación y configuración del entorno Flask:
Se instaló la librería Flask mediante el comando pip install flask y se verificó su correcto funcionamiento ejecutando un script básico que devuelve texto plano desde el servidor local.

2. Creación de una página HTML con Flask:
Se utilizó la función @aplicacion.route("/") para definir la ruta raíz del servidor y la función raiz() para devolver código HTML con etiquetas y estilos CSS, demostrando la posibilidad de integrar diseño dentro de Flask.

3. Generación de contenido HTML dinámico:
Se implementó un bucle for en Python para generar una secuencia de números del 1 al 30 dentro del HTML, demostrando cómo Flask puede crear contenido dinámico a partir de estructuras de control y concatenación de cadenas.

Durante la práctica se observó cómo Flask procesa las solicitudes HTTP, construye la respuesta HTML y la envía al navegador. También se realizaron pruebas locales para comprobar el funcionamiento del servidor en la dirección http://127.0.0.1:5000/.

---
```
''' 
Desarrollo web con Flask
2025 Fabiana Victoria Sotillo
Programa que crea un servidor Flask para mostrar contenido HTML estático y dinámico,
utilizando estructuras de control en Python y estilos CSS integrados.
'''

from flask import Flask

# Se crea la aplicación principal
aplicacion = Flask(__name__)

# Ruta principal de la aplicación
@aplicacion.route("/")
def raiz():
    # Inicia una cadena HTML con estructura y estilo básico
    cadena = '''
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <title>HTML dinámico con Flask</title>
        <style>
          body {font-family: Arial; background-color: Lavender;}
          h1 {color: red; text-align: center;}
          div {
            display: inline-block;
            margin: 5px;
            padding: 10px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 1px 1px 3px gray;
          }
        </style>
      </head>
      <body>
        <h1>Esto es HTML a tope de power</h1>
    '''

    # Bucle para generar números del 1 al 30
    for dia in range(1, 31):
        cadena += f'<div>{dia}</div>'

    # Cierre del cuerpo y del documento HTML
    cadena += '''
      </body>
    </html>
    '''
    
    # Devuelve el HTML generado al navegador
    return cadena

# Punto de entrada de la aplicación
if __name__ == "__main__":
    aplicacion.run(debug=True)
```

---
Al ejecutar python app.py y abrir http://127.0.0.1:5000/ en el navegador, se muestra una página con un encabezado rojo y treinta cuadros numerados del 1 al 30, dispuestos de forma ordenada y con estilo.

La práctica permitió comprender los principios básicos del desarrollo web con Flask, incluyendo la creación de rutas, el retorno de contenido HTML y la generación dinámica mediante bucles. Además, se integraron conceptos de estilo CSS para mejorar la presentación del contenido. 

Este ejercicio resulta esencial para conectar la programación en Python con la creación de aplicaciones web. Su aplicación práctica evidencia la relación directa entre la estructura de Python y la representación visual en la web.