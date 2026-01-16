En este ejercicio se trabaja la creación de una aplicación web sencilla utilizando Flask para generar contenido HTML dinámico desde Python. Se implementa un calendario de doce meses utilizando un sistema de rejilla (grid layout), donde cada mes se representa como un bloque y cada día como una celda individual. Mediante bucles y concatenación de cadenas, se construye la estructura HTML desde el servidor y se devuelve al navegador como respuesta. El objetivo del ejercicio es comprender cómo Flask permite generar páginas web dinámicas y cómo se pueden combinar Python y HTML para crear interfaces visuales estructuradas.

---
El ejercicio se divide en cuatro partes principales:

#### 1. Instalación de Flask

Se instala la librería Flask mediante el gestor de paquetes pip, lo que permite crear aplicaciones web con Python de forma sencilla.
```
pip install flask
```

#### 2. Creación de la aplicación Flask

Se crea una nueva aplicación Flask utilizando la clase Flask. Esta aplicación será la encargada de gestionar las peticiones del navegador y devolver el contenido HTML.

#### 3. Definición de la ruta principal

Se define una ruta inicial (/) que genera dinámicamente el código HTML del calendario. En esta ruta se utiliza una cadena que contiene la estructura HTML y estilos CSS, junto con bucles for para generar los meses y los días.

Cada mes se representa como un bloque con un grid de 7 columnas (una por cada día de la semana) y cada día se muestra como una celda.

#### 4. Ejecución del servidor

Finalmente, se ejecuta el servidor Flask en modo desarrollo para poder visualizar el calendario desde el navegador.

---
A continuación se muestra el código de la app.py:
```
''' 
Calendario web con Flask
2026 Fabiana Victoria Sotillo
Programa que crea una aplicación Flask para generar un calendario de 12 meses
utilizando HTML dinámico y un sistema de rejilla (grid layout).
'''
from flask import Flask

# Creo una nueva aplicación
aplicacion = Flask(__name__)

# Defino la ruta principal
@aplicacion.route("/")
def raiz():

    cadena = '''
    <!doctype html>
    <html>
      <head>
        <title>Calendario en Python</title>
        <meta charset="utf-8">
        <style>
          .mes{
            width:700px;
            display:grid;
            grid-template-columns:auto auto auto auto auto auto auto;
            margin-bottom:30px;
          }
          .dia{
            width:100px;
            height:100px;
            border:1px solid grey;
            display:flex;
            justify-content:center;
            align-items:center;
            font-family:Arial;
          }
        </style>
      </head>
      <body>
        <h1>Calendario anual</h1>
    '''

    # Generar los 12 meses
    for mes in range(1, 13):
        cadena += '<h2>Mes ' + str(mes) + '</h2>'
        cadena += '<div class="mes">'

        # Generar los días del mes
        for dia in range(1, 31):
            cadena += '<div class="dia">' + str(dia) + '</div>'

        cadena += '</div>'

    # Cerrar HTML
    cadena += '''
      </body>
    </html>
    '''

    return cadena

# Arrancar servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)
```

---
Como resultados final se tiene que al acceder a la aplicación, se muestra una página web con:
- Un calendario de 12 meses
- Cada mes organizado en un grid de 7 columnas
- Cada día representado por una celda numerada

Para finalizar, se puede decir que en este ejercicio se ha desarrollado una aplicación web con Flask que genera dinámicamente un calendario anual utilizando código Python para construir la estructura HTML. Se han aplicado los conceptos de creación de rutas, generación de contenido dinámico y uso de estilos CSS para organizar los elementos en un sistema de rejilla. Esta práctica permite comprender cómo Python puede utilizarse para generar interfaces web y cómo Flask actúa como intermediario entre el servidor y el navegador. El ejercicio refuerza los fundamentos del desarrollo web con Python y sienta las bases para aplicaciones más complejas que integren lógica y presentación de forma dinámica.
