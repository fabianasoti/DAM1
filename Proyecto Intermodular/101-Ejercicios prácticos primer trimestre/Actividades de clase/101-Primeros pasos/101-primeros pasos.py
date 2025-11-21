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