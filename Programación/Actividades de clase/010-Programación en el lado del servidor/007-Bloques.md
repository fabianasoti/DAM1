En este ejercicio se desarrolla un panel de control para una aplicación web orientada a la gestión de usuarios registrados. Un panel de control es una herramienta fundamental en cualquier sistema web, ya que permite visualizar, organizar y administrar información de forma clara y estructurada. Mediante el uso de HTML para la estructura visual y PHP para la inclusión de archivos, se construye una interfaz con navegación lateral y una tabla de usuarios. El objetivo principal es aplicar los conceptos básicos de desarrollo web aprendidos en clase para crear una aplicación modular y reutilizable, siguiendo una estructura clara y profesional.

---
El ejercicio se divide en tres bloques principales: la estructura del panel, la navegación lateral y la tabla de usuarios.

#### 1. Estructura principal del panel de control

Se crea el archivo paneldecontrol.php, que contiene la estructura HTML base del panel. En él se definen las etiquetas principales ```(<!doctype html>, <html>, <head>, <body>)```, así como un menú lateral de navegación y un área principal donde se mostrará la tabla de usuarios.

Se utilizan archivos incluidos para separar la navegación y la tabla, facilitando la organización del código y su reutilización.

#### 2. Archivo de navegación lateral

Se crea el archivo bloques/navegacion.php, que contiene una lista desordenada con enlaces a distintas secciones del panel, como usuarios, productos y configuración. Este menú simula un panel real de administración, como los utilizados en proyectos de diseño y desarrollo web.

#### 3. Archivo de la tabla de usuarios

Se desarrolla el archivo bloques/tabla.php, donde se construye una tabla HTML con los datos de los usuarios. La tabla incluye encabezados y varias filas de ejemplo, simulando un sistema real de gestión de clientes de una tienda de crochet online.

---
A continuación se muestra el código:
#### paneldecontrol.php
```
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Panel de Control - Crochet & Diseño Web</title>
</head>
<body>

    <nav>
        <?php include("bloques/navegacion.php"); ?>
    </nav>

    <main>
        <h1>Panel de Control - Usuarios Registrados</h1>
        <?php include("bloques/tabla.php"); ?>
    </main>

</body>
</html>
```

#### bloques/navegacion.php
```
<ul>
    <li><a href="#">Usuarios</a></li>
    <li><a href="#">Productos de Crochet</a></li>
    <li><a href="#">Diseño Web</a></li>
    <li><a href="#">Configuración</a></li>
</ul>
```

#### bloques/tabla.php:
```
<table border="1">
    <tr>
        <th>Nombre</th>
        <th>Apellidos</th>
        <th>Email</th>
        <th>Dirección</th>
    </tr>
    <tr>
        <td>Laura</td>
        <td>Tejedora Ruiz</td>
        <td>laura@crochetart.com</td>
        <td>Calle Lana 12</td>
    </tr>
    <tr>
        <td>Mario</td>
        <td>Diseño Web</td>
        <td>mario@disenoweb.com</td>
        <td>Avenida Código 45</td>
    </tr>
    <tr>
        <td>Clara</td>
        <td>Punto Creativo</td>
        <td>clara@handmade.com</td>
        <td>Plaza Agujas 7</td>
    </tr>
    <tr>
        <td>David</td>
        <td>Frontend</td>
        <td>david@webstudio.com</td>
        <td>Calle HTML 99</td>
    </tr>
</table>
```
Para ejecutar el proyecto hay que guardar los archivos en la estructura indicada:
```
paneldecontrol.php
/bloques
   navegacion.php
   tabla.php
```
Luego hay que abrir el archivo paneldecontrol.php desde el navegador mediante un servidor local (Apache).

---
Finalmente, obtenemos:
- Un menú lateral con enlaces de navegación.
- Un área principal con una tabla de usuarios.
- Una estructura modular gracias a la inclusión de archivos PHP.

En este ejercicio se ha desarrollado un panel de control funcional utilizando HTML y PHP mediante la inclusión de archivos, aplicando los conceptos básicos de estructuración web aprendidos en clase. Se ha implementado una navegación lateral y una tabla de usuarios que simula un entorno real de administración, como los utilizados en proyectos de diseño y desarrollo web o tiendas online de productos artesanales como crochet. Esta práctica permite comprender cómo se organizan las aplicaciones web profesionales y cómo se separan los distintos bloques de contenido para mejorar la organización y el mantenimiento del código. El panel de control desarrollado sienta las bases para futuras aplicaciones más complejas orientadas a la gestión de usuarios.
