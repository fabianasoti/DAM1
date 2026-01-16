En este ejercicio se desarrolla un sitio web personal. El proyecto consiste en crear una pequeña web compuesta por varias páginas en PHP que comparten una estructura común mediante la inclusión de bloques reutilizables. El objetivo principal es comprender cómo se organiza un sitio web modular utilizando PHP, aplicando la reutilización de código y la separación de contenidos en distintos archivos para mejorar la mantenibilidad y la claridad del proyecto.

El sitio web se compone de tres páginas principales: la página de inicio, la página sobre el autor y la página de contacto. Cada una de estas páginas está desarrollada en PHP y utiliza bloques comunes de cabecera y pie para mantener una estructura homogénea en todo el sitio.

Los bloques cabecera.php y pie.php contienen los elementos comunes de la web, como la estructura HTML base, el encabezado, el menú de navegación y el pie de página. Estos archivos se incluyen en cada página mediante la instrucción include, lo que permite reutilizar código y facilitar futuras modificaciones.

Cada archivo PHP contiene un contenido específico:

- index.php muestra un texto explicativo sobre la importancia de aprender programación web.

- sobremi.php describe los hobbies y la experiencia laboral relacionada con la programación y el arte latte.

- contacto.php ofrece un formulario o información de contacto para que los visitantes puedan comunicarse con el autor.

Esta organización permite crear un sitio web coherente, ordenado y fácil de mantener.

---
Archivo cabecera.php:
```
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Blog de Jose Vicente Carratala</title>
</head>
<body>
  <header>
    <h1>Blog de programación web y arte latte</h1>
    <nav>
      <a href="index.php">Inicio</a> |
      <a href="sobremi.php">Sobre mí</a> |
      <a href="contacto.php">Contacto</a>
    </nav>
    <hr>
  </header>

Archivo pie.php
  <hr>
  <footer>
    <p>&copy; 2026 - Blog personal de Jose Vicente Carratala</p>
  </footer>
</body>
</html>
```

Archivo index.php:
```
<?php include("cabecera.php"); ?>

<main>
  <p>
    Aprender a programar web es una habilidad fundamental en el mundo digital actual,
    ya que permite crear aplicaciones interactivas, sitios dinámicos y soluciones
    tecnológicas adaptadas a las necesidades de los usuarios.
  </p>
</main>

<?php include("pie.php"); ?>

Archivo sobremi.php
<?php include("cabecera.php"); ?>

<main>
  <h2>Sobre mí</h2>
  <p>
    Soy un apasionado de la programación web y del arte latte. Me encanta combinar
    la creatividad del café con el desarrollo de aplicaciones web modernas.
    He trabajado en distintos proyectos relacionados con diseño web, desarrollo
    backend y creación de plataformas interactivas.
  </p>
</main>

<?php include("pie.php"); ?>
```

Archivo contacto.php:
```
<?php include("cabecera.php"); ?>

<main>
  <h2>Contacto</h2>
  <p>Puedes ponerte en contacto conmigo a través del siguiente formulario:</p>

  <form>
    <p>Nombre</p>
    <input type="text" name="nombre">

    <p>Email</p>
    <input type="email" name="email">

    <p>Mensaje</p>
    <textarea name="mensaje"></textarea>

    <br><br>
    <input type="submit" value="Enviar">
  </form>
</main>

<?php include("pie.php"); ?>
```

---
Al ejecutar el sitio en un servidor con soporte PHP, se puede navegar entre las tres páginas manteniendo siempre la misma estructura visual. Los bloques comunes garantizan una presentación uniforme y facilitan la modificación global del diseño desde un único archivo.

Este ejercicio permite comprender cómo se estructura un sitio web real utilizando PHP y bloques reutilizables. La creación de páginas independientes que comparten una cabecera y un pie común demuestra la importancia de la modularidad y la reutilización de código en el desarrollo web. Estos conceptos son fundamentales para proyectos más grandes, donde mantener una estructura clara y organizada facilita el mantenimiento, la escalabilidad y la evolución del sitio. De este modo, la práctica refuerza los conocimientos adquiridos en la unidad sobre PHP y desarrollo web dinámico.
