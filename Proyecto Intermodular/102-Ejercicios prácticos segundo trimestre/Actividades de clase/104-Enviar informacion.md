En este ejercicio se trabaja el desarrollo de una aplicación web con Flask que permite capturar información introducida por el usuario a través de un formulario HTML y enviarla al servidor mediante parámetros en la URL. Se utilizan los conceptos de rutas, plantillas HTML y obtención de parámetros con la librería request. El objetivo es comprender cómo funciona la comunicación entre el navegador y el servidor, así como el procesamiento de datos enviados desde un formulario web.

---
El ejercicio se divide en tres partes fundamentales:

#### 1. Creación del formulario en HTML

Se diseña una página web sencilla que contiene un formulario con dos campos de texto: nombre y apellidos. El formulario envía los datos al servidor utilizando el método GET y la ruta /envio.

Se utilizan:
- Etiqueta ```<form>``` para crear el formulario
- Atributo action para indicar la ruta de envío
- Atributo method="get" para enviar los datos por URL
- Campos ```<input>``` para recoger la información del usuario

2. Creación de rutas en Flask

Se configura una aplicación Flask que dispone de dos rutas:
- ```/``` muestra el formulario
- ```/envio``` recibe los datos enviados y los muestra como respuesta

Se emplea la librería request para capturar los parámetros enviados desde el formulario.

3. Ejecución y prueba de la aplicación

La aplicación se ejecuta desde la terminal y se accede a ella mediante el navegador. Tras completar el formulario y pulsar el botón de envío, los datos se muestran en pantalla.

---
A continuación se muestra el código:

#### index.html
```
<!doctype html>
<html>
  <head>
    <title>Micro formulario</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>Micro formulario</h1>

    <form action="/envio" method="get">
      Nombre: <input type="text" name="nombre"><br><br>
      Apellidos: <input type="text" name="apellidos"><br><br>
      <input type="submit" value="Enviar">
    </form>

  </body>
</html>
```

#### 004-lanzamos los datos.py
```
''' 
Formulario con Flask
2026 Fabiana Victoria Sotillo
Programa que crea una aplicación Flask con un formulario web que envía datos al servidor
y los muestra como respuesta utilizando parámetros de la URL.
'''
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal: muestra el formulario
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta que recibe los datos del formulario
@app.route("/envio")
def envio():
    nombre = request.args.get("nombre", "Desconocido")
    apellidos = request.args.get("apellidos", "Desconocidos")
    return f"Nombre: {nombre} - Apellidos: {apellidos}"

# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)
```

#### Estructura del proyecto
```
micro_formulario/
│
├── 004-lanzamos los datos.py
└── templates/
    └── index.html
```

Luego se ejecuta desde la terminal:
```
python3 004-lanzamos\ los\ datos.py
```
Y se abre http://127.0.0.1:5000/ en el navegador.

---
Finalmente, al introducir los datos en el formulario y pulsar Enviar, el navegador muestra:
```
Nombre: Ana - Apellidos: García
```

Los datos se envían mediante la URL y son procesados por Flask correctamente.

En este ejercicio se ha desarrollado una aplicación web sencilla con Flask que permite capturar datos introducidos por el usuario a través de un formulario HTML y procesarlos en el servidor mediante parámetros enviados por la URL. Se han aplicado los conceptos de rutas, plantillas, formularios web y obtención de datos con la librería request. Esta práctica permite comprender el funcionamiento básico de la comunicación entre cliente y servidor, sentando las bases para el desarrollo de aplicaciones web interactivas y dinámicas más avanzadas.
