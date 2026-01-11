```
'''
Codificación y descodificación de cadenas en PHP mediante Base64
2026 Fabiana Sotillo

'''
```

---
El presente ejercicio tiene como objetivo aplicar el concepto de codificación y descodificación de cadenas en el lenguaje PHP mediante el uso de la codificación Base64. Este tipo de técnicas se utilizan para transformar información sensible en un formato diferente que pueda ser transmitido o almacenado de forma segura. A través del uso de las funciones base64_encode() y base64_decode(), se busca comprender cómo convertir una cadena original en una versión codificada y cómo recuperar posteriormente su contenido original, reforzando así la manipulación de datos y el tratamiento de información en aplicaciones web.

---
En esta actividad se trabaja con una cadena de texto que representa una contraseña, la cual se codifica utilizando la función base64_encode() de PHP. Esta función convierte la cadena original en una versión codificada en Base64, que puede ser utilizada para su almacenamiento o transmisión.

Posteriormente, se emplea la función base64_decode() para revertir el proceso y obtener nuevamente la cadena original a partir de su versión codificada. Además, se desarrolla una función personalizada que permite descodificar una cadena varias veces mediante un bucle, reforzando el uso de estructuras repetitivas y funciones en PHP. De este modo, se integran conceptos de programación estructurada con el manejo de cadenas codificadas.

---
A continuación, se presentan los fragmentos de código utilizados en el ejercicio junto con su explicación.

1. Codificación de una contraseña en Base64
<?php
$contrasena = "contraseñasegura1234";
echo $contrasena; // Contraseña original
echo "<br>";
$codificado = base64_encode($contrasena);
echo $codificado; // Contraseña codificada en Base64
?>


En este bloque se define una variable que almacena la contraseña original y se muestra por pantalla. A continuación, se utiliza la función base64_encode() para obtener su versión codificada y se imprime el resultado.

2. Descodificación de la contraseña
<?php
$descodificado = base64_decode($codificado);
echo $descodificado; // Contraseña original nuevamente
?>


En este fragmento se emplea la función base64_decode() para convertir la cadena codificada nuevamente en su forma original.

3. Función personalizada para descodificar múltiples veces
<?php
function funcion_descodificar($cadena) {
    for ($i = 0; $i < 9; $i++) {
        $cadena = base64_decode($cadena);
    }
    return $cadena;
}

$contrasena = "contraseñasegura1234";
$codificado = base64_encode($contrasena);
echo $codificado; // Contraseña codificada en Base64
echo "<br>";
$descodificado = funcion_descodificar($codificado);
echo $descodificado; // Contraseña original nuevamente
?>


En este bloque se define una función llamada funcion_descodificar() que recibe una cadena codificada y la descodifica nueve veces mediante un bucle for. Posteriormente, se prueba la función con una contraseña codificada.

---
Como resultado del ejercicio, se obtiene la contraseña original, su versión codificada en Base64 y la posterior recuperación del valor inicial mediante la descodificación. Esto permite comprobar el funcionamiento correcto de las funciones de codificación y descodificación en PHP.

Este ejercicio permite comprender el funcionamiento de la codificación y descodificación de cadenas en PHP mediante Base64, así como su aplicación práctica en el tratamiento de información sensible. El uso de funciones integradas como base64_encode() y base64_decode(), junto con la creación de funciones personalizadas y el uso de bucles, refuerza el aprendizaje de estructuras fundamentales del lenguaje PHP. Estas técnicas resultan esenciales en el desarrollo de aplicaciones web seguras y en la manipulación eficiente de datos.
