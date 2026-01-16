```
Uso del método POST en formularios HTML
2026 Fabiana Victoria Sotillo
Programa que recibe datos enviados desde un formulario mediante el método POST
y muestra un mensaje de bienvenida utilizando PHP.
```

---
En este ejercicio se trabaja con los verbos HTTP, concretamente GET y POST, que son fundamentales para la comunicación entre un cliente y un servidor en aplicaciones web. El método GET se utiliza principalmente para solicitar información, mientras que el método POST permite enviar datos al servidor de forma segura y estructurada. A través de la creación de un formulario HTML y su posterior procesamiento en PHP, se aplican los conceptos de envío y recepción de datos, validación de información y generación de respuestas dinámicas, con el objetivo de comprender cómo funcionan las peticiones web en aplicaciones interactivas.

---
Se creará un formulario HTML que envíe datos al servidor utilizando el método POST y se desarrollará un script en PHP que reciba, procese y muestre dicha información.

El formulario se estructura mediante la etiqueta ```<form>``` y se configura con el atributo method="POST", indicando que los datos se enviarán al servidor utilizando este verbo HTTP. 

El atributo action especifica el archivo PHP que se encargará de procesar la información.

En el archivo PHP se utiliza la variable superglobal $_POST para acceder a los datos enviados desde el formulario. Además, se emplea la función isset() para comprobar si el usuario ha introducido un nombre, evitando errores y mostrando un mensaje alternativo en caso contrario. 

Para mejorar la seguridad, se usa la función htmlspecialchars() con el fin de evitar la inyección de código malicioso.

---
A continuación, el código funcional completo:
- Archivo formulario.html:
```
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Formulario con método POST</title>
</head>
<body>

<form action="procesar.php" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit" value="Enviar">
</form>

</body>
</html>
```

- Archivo procesar.php:
```
<?php
if (isset($_POST['nombre'])) {
    $nombre = $_POST['nombre'];
    echo "Hola, " . htmlspecialchars($nombre) . "! ¡Bienvenido/a!";
} else {
    echo "No se ha introducido ningún nombre.";
}
?>
```

---
Al ejecutar el formulario en un navegador e introducir un nombre, el sistema envía los datos al servidor mediante el método POST y el archivo procesar.php muestra un mensaje de bienvenida personalizado. Si el usuario no introduce ningún nombre, el programa muestra un mensaje informando de que no se ha recibido ningún dato.

Este ejercicio permite comprender de forma práctica el funcionamiento de los verbos HTTP, especialmente el método POST, y su uso en aplicaciones web interactivas. 

La creación de un formulario HTML y su procesamiento en PHP demuestra cómo se pueden enviar y recibir datos entre el cliente y el servidor de forma estructurada y segura. 

Este tipo de prácticas resulta esencial para el desarrollo de aplicaciones dinámicas, ya que sienta las bases para la creación de sistemas de registro, autenticación y gestión de información en proyectos web reales, reforzando así los conocimientos adquiridos en la unidad sobre comunicación cliente-servidor.
