En este ejercicio se trabaja la lectura de datos en formato JSON desde un archivo externo utilizando JavaScript con la API Fetch, así como la creación de un microservidor web con Flask para servir contenido HTML de forma local. El formato JSON permite estructurar información de manera ligera y fácilmente intercambiable entre aplicaciones, mientras que Fetch facilita la obtención de estos datos desde el navegador. Por su parte, Flask actúa como un servidor web ligero que permite renderizar plantillas HTML y servir archivos estáticos. El objetivo del ejercicio es comprender cómo se integran estas tecnologías para mostrar datos dinámicos en una página web.

---
El proyecto se compone de tres elementos principales:

1. Lectura de JSON con Fetch en HTML:

Se utiliza JavaScript y la API Fetch para cargar un archivo curriculum.json y mostrar sus datos en una página HTML. Fetch realiza una petición HTTP al archivo JSON, convierte la respuesta en un objeto JavaScript y permite acceder a sus propiedades.

Se utilizan:
- fetch() para solicitar el archivo
- .json() para convertir la respuesta
- Manipulación del DOM para mostrar los datos

2. Creación de un microservidor con Flask:

Flask permite crear un servidor web local que renderiza una plantilla HTML desde la carpeta templates. El servidor escucha en la ruta raíz (/) y devuelve la página index.html.

Se utilizan:
- Flask para crear la aplicación
- @app.route() para definir rutas
- render_template() para cargar HTML

3. Organización del proyecto:

La estructura del proyecto es:
```
proyecto/
│
├── 003-microservidor.py
├── templates/
│   └── index.html
└── static/
    └── curriculum.json
```

Esto permite que Flask encuentre correctamente la plantilla HTML y el archivo JSON.

---
A continuación se muestra el código funcional en el que se ha trabajado:

#### 001-leer json.html:
```
<!doctype html>
<html lang="es">
  <head>
    <title>Plantilla fetch</title>
    <meta charset="utf-8">
  </head>
  <body>

    <h1>Currículum</h1>
    <p><strong>Nombre:</strong> <span id="nombre"></span></p>
    <p><strong>Apellidos:</strong> <span id="apellidos"></span></p>
    <p><strong>Correo:</strong> <span id="correo"></span></p>

    <script>
      fetch("curriculum.json")
        .then(function(respuesta){
          return respuesta.json(); // La info viene en json
        })
        .then(function(datos){
          console.log(datos); // Mostramos los datos en consola
          document.getElementById('nombre').innerText = datos.nombre;
          document.getElementById('apellidos').innerText = datos.apellidos;
          document.getElementById('correo').innerText = datos.correo;
        })
    </script>

  </body>
</html>
```

#### curriculum.json:
```
{
  "nombre": "Fabiana Victoria",
  "apellidos": "Sotillo",
  "correo": "info@fabiana.com"
}
```

#### 003-microservidor.py
```
''' 
Microservidor con Flask
2026 Fabiana Victoria Sotillo
Programa que crea un microservidor web con Flask para renderizar una plantilla HTML
y mostrar los datos de un archivo JSON utilizando Fetch desde el navegador.
'''
from flask import Flask, render_template  # Cargar archivos HTML

# Crear aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)
```

#### templates/index.html:
```
<!doctype html>
<html lang="es">
  <head>
    <title>Currículum con Flask</title>
    <meta charset="utf-8">
  </head>
  <body>

    <h1>Currículum</h1>
    <p><strong>Nombre:</strong> <span id="nombre"></span></p>
    <p><strong>Apellidos:</strong> <span id="apellidos"></span></p>
    <p><strong>Correo:</strong> <span id="correo"></span></p>

    <script>
      fetch("/static/curriculum.json")
        .then(function(respuesta){
          return respuesta.json();
        })
        .then(function(datos){
          document.getElementById('nombre').innerText = datos.nombre;
          document.getElementById('apellidos').innerText = datos.apellidos;
          document.getElementById('correo').innerText = datos.correo;
        })
    </script>

  </body>
</html>
```

Desde la terminal se ejecuta:
```
python 003-microservidor.py
```

Y luego abrir en el navegador:
```
http://127.0.0.1:5000/
```

---
Luego, al acceder a la página, se muestran dinámicamente los datos del archivo JSON:
```
Nombre: Fabiana Victoria
Apellidos: Sotillo
Correo: info@fabiana.com
```

En este ejercicio se ha trabajado la lectura de datos en formato JSON desde el navegador utilizando la API Fetch de JavaScript, permitiendo obtener información externa y mostrarla dinámicamente en una página web. Además, se ha implementado un microservidor con Flask para renderizar una plantilla HTML y servir archivos estáticos de forma local. Esta práctica permite comprender la integración entre frontend y backend, así como el uso de servidores ligeros para el desarrollo de aplicaciones web. El ejercicio refuerza los conceptos de arquitectura cliente-servidor y sienta las bases para el desarrollo de aplicaciones web dinámicas más complejas.
