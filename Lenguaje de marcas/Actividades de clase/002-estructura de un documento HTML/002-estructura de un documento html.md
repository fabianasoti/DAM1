```
'''
Primeros documentos con HTML
2025 Fabiana Victoria Sotillo
Creación de un documento HTML para comprender su estructura
'''
```

HTML (HyperText Markup Language) es un lenguaje de marcado utilizado para estructurar páginas web.
El objetivo de este ejercicio es comprender cómo se estructura un documento HTML, y aplicar el concepto de cabeza (head) y cuerpo (body) en un documento HTML, reconociendo su función dentro de la construcción de una página web.

En HTML, el elemento ```<head>``` contiene la información no visible directamente en el navegador, como el título, la codificación de caracteres y los metadatos. Por otro lado, el elemento ```<body>``` contiene todo el contenido visible para el usuario, como encabezados, párrafos, listas, imágenes y enlaces.

A través de esta práctica, se crea un documento HTML desde cero, se añaden elementos básicos a las secciones ```<head>``` y ```<body>```, y se visualiza el resultado en un navegador para analizar su estructura.

Para realizar este ejercicio, se ha realizado lo siguiente:

- Se abrió un editor de código y se creó un archivo con extensión .html.
- Se copió la estructura básica de un documento HTML5:
```
<!doctype html>
<html lang="es">
  <head>
  </head>
  <body>
  </body>
</html>
```

Se agrega información a la sección de la cabeza (head) del documento, que incluye el título de la página (define el texto que aparece en la pestaña del navegador) y la codificación de caracteres (que permite mostrar correctamente los caracteres especiales en español)
```
<head>
  <title>Fabiana Victoria Sotillo</title>
  <meta charset="utf-8">
</head>
```

- Se añade al cuerpo (body) los elementos visibles, y se hacen pruebas agregando más elementos, tales como;
	- encabezados (```<h1>``` y ```<h2>```), 
	-  listas (con ```<ul>``` se crea una lista desordenada y luego se señala cada elemento de la lista con ```<li>```) 
	-  y enlaces que redirigen a sitios externos, que se realizan con ```<a href="">```:
```
<body>
  <h1>Fabiana Victoria Sotillo</h1>
  <h2>Estudiante de DAM</h2>
  <ul>
    <li>Inicio</li>
    <li>Sobre mí</li>
    <li>Portafolio</li>
    <li>Contacto</li>
    <li>Crochet</li>
    <li>Diseño</li>
  </ul>
  <a href="https://instagram.com/fabiaganchillo">Instagram</a>
  <a href="https://github.com/fabianasoti">Github</a>
</body>
```

Para visualizar el resultado se guarda el archivo y se abre en un navegador web.

A continuación, el código completo funcional:
```
<!--Primeros documentos con HTML-->
<!--2025 Fabiana Victoria Sotillo-->
<!--Creación de un documento HTML para comprender su estructura-->

<!doctype html>
<html lang="es">
  <head>
    <title>Fabiana Victoria Sotillo</title>
    <meta charset="utf-8">
  </head>
  <body>
	 <!-- Se crean encabezados-->
      <h1>Fabiana Victoria Sotillo</h1>
      <h2>Estudiante de DAM</h2>
			 <!-- Se prueba agregar una lista-->
        <ul>
          <li>Inicio</li>
          <li>Sobre mi</li>
          <li>Portafolio</li>
          <li>Contacto</li>
          <li>Crochet</li>
          <li>Diseño</li>
        </ul>
      <!-- Se prueba agregar un link-->
      <a href="https://instagram.com/fabiaganchillo">Instagram</a>
      <a href="https://github.com/fabianasoti">Github</a>
  </body>
</html>
```

Este ejercicio permitió comprender la estructura fundamental de un documento HTML, diferenciando entre la información técnica y estructural (en el ```<head>```) y el contenido visible (en el ```<body>```).

Se aplicaron correctamente las etiquetas básicas, jerarquías de encabezados y creación de listas y enlaces. Y se experimentaron y corrigieron errores comunes, como olvidar cerrar etiquetas, por tanto, se aprendió a siempre verificar que cada etiqueta tenga su cierre correspondiente.

El conocimiento adquirido sienta las bases para el desarrollo web.