En este ejercicio se desarrolla un sistema sencillo orientado al mundo del café en el que los clientes pueden responder preguntas y recibir información relacionada con esta temática. Para ello, se trabaja con arrays nombrados en PHP y su conversión al formato JSON, una estructura muy utilizada en aplicaciones web para el almacenamiento e intercambio de datos. 

El objetivo principal es comprender cómo se organizan los datos en arrays asociativos y cómo pueden transformarse en formato JSON para su visualización y posible persistencia, integrando estos conceptos en un proyecto relacionado con los hobbies y el entorno cafetero.

---
El programa comienza con la creación de un array nombrado llamado cliente, que almacena los datos básicos de un usuario, como su nombre, apellidos y correo electrónico. Este tipo de array permite asociar cada valor a una clave, facilitando la organización y el acceso a la información.

A continuación, se utiliza la función json_encode() para convertir el array a formato JSON, guardando el resultado en una variable llamada $json. Este formato es ampliamente utilizado en aplicaciones web modernas por su simplicidad y compatibilidad con distintos lenguajes de programación.

Además, se implementa un formulario HTML que permite al usuario introducir una pregunta y una respuesta sobre el café. Al enviar el formulario mediante el método POST, los datos se recuperan en PHP y se convierten también a formato JSON, mostrándose en la parte inferior de la página para verificar que la información se ha procesado correctamente.

---
Código completo funcional y comentado:
```
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Formulario de preguntas sobre café</title>
</head>
<body>

<?php
// Creación del array nombrado cliente
$cliente = array(
    "nombre" => "Carlos",
    "apellidos" => "García López",
    "email" => "carlos@email.com"
);

// Conversión del array a JSON
$json = json_encode($cliente);

// Mostrar el JSON del cliente
echo "<h3>Datos del cliente en formato JSON:</h3>";
echo $json;
echo "<hr>";

// Procesamiento del formulario
if (isset($_POST['pregunta']) && isset($_POST['respuesta'])) {

    $datosCafe = array(
        "pregunta" => $_POST['pregunta'],
        "respuesta" => $_POST['respuesta']
    );

    $jsonCafe = json_encode($datosCafe);
}
?>

<h3>Formulario de preguntas sobre café</h3>

<form method="POST">
  <p>Introduce una pregunta sobre café</p>
  <input type="text" name="pregunta">

  <p>Introduce la respuesta</p>
  <input type="text" name="respuesta">

  <br><br>
  <input type="submit" value="Enviar">
</form>

<?php
// Mostrar el JSON generado al enviar el formulario
if (isset($jsonCafe)) {
    echo "<hr>";
    echo "<h3>Datos enviados en formato JSON:</h3>";
    echo $jsonCafe;
}
?>

</body>
</html>
```

---
Al ejecutar el programa, se muestra inicialmente el array del cliente convertido a formato JSON. A continuación, el usuario puede introducir una pregunta y una respuesta relacionada con el café en el formulario. Al enviar los datos, estos se recuperan mediante el método POST, se convierten a formato JSON y se muestran en la parte inferior de la página, comprobando así el correcto funcionamiento del sistema.

Un error habitual es no comprobar si los datos han sido enviados antes de utilizarlos, lo que puede provocar avisos o errores en PHP. También es frecuente olvidar utilizar json_encode() para convertir correctamente los arrays al formato JSON. Otro fallo común es no utilizar arrays nombrados, lo que dificulta la organización de los datos y su posterior tratamiento.

Este ejercicio permite comprender el uso de arrays nombrados en PHP y su conversión al formato JSON, una técnica fundamental en el desarrollo de aplicaciones web modernas. La implementación de un formulario para introducir preguntas y respuestas sobre el café demuestra cómo se pueden integrar los intereses personales en proyectos de programación, haciendo el aprendizaje más cercano y práctico. Además, esta práctica refuerza la base necesaria para trabajar con sistemas de almacenamiento de datos, APIs y aplicaciones interactivas, sentando las bases para proyectos más complejos en el ámbito del desarrollo web.
