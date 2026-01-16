```
Uso de condicionales y funciones en PHP aplicadas al arte latte
2026 Fabiana Victoria Sotillo
Programa que muestra mensajes personalizados según la edad del usuario
y su nivel de conocimiento sobre arte latte utilizando funciones y condicionales.
```

---
En este ejercicio se desarrolla un programa en PHP que integra los hobbies y conocimientos del mundo del café, concretamente el arte latte, con la lógica de programación mediante el uso de funciones y estructuras condicionales. A través de la creación de una función que recibe la edad del usuario y su nivel de conocimiento en arte latte, se aplican condicionales if y else para mostrar mensajes personalizados. 

El objetivo principal es reforzar el uso de funciones, la toma de decisiones mediante estructuras condicionales y la comparación de cadenas, aplicando estos conceptos en un contexto cercano y creativo relacionado con el mundo del café.

---
El programa se basa en la definición de una función llamada mostrarMensaje, la cual recibe dos parámetros: la edad del usuario y su nivel de conocimiento sobre arte latte. Dentro de esta función se utilizan estructuras condicionales if y else para evaluar ambas variables y mostrar mensajes adecuados según cada caso.

En primer lugar, se evalúa la edad del usuario para determinar si es menor de 30 años o no, mostrando un mensaje acorde. A continuación, se emplea un segundo bloque condicional para analizar el nivel de conocimiento en arte latte, que puede ser “novato”, “intermedio” o “experto”. Para cumplir con las restricciones del ejercicio, se utilizan únicamente comparaciones con el operador == y no se emplean estructuras de control como switch.

Este enfoque permite integrar los intereses personales relacionados con el café dentro de una aplicación web funcional, demostrando cómo la programación puede adaptarse a contextos creativos y cotidianos.

---
Código completo funcional y comentado:
```
<?php
function mostrarMensaje($edad, $conocimientoLatte) {

    // Condicional para la edad
    if ($edad < 30) {
        echo "Eres un joven.<br>";
    } else {
        echo "Ya no eres un joven.<br>";
    }

    // Condicional para el nivel de conocimiento en arte latte
    if ($conocimientoLatte == "novato") {
        echo "Aprende más sobre arte latte.<br>";
    } else {
        if ($conocimientoLatte == "intermedio") {
            echo "Muy bien, eres un experto en arte latte.<br>";
        } else {
            if ($conocimientoLatte == "experto") {
                echo "¡Excelente conocimiento de arte latte!<br>";
            }
        }
    }

    echo "<hr>";
}

// Llamadas a la función con diferentes valores
mostrarMensaje(22, "novato");
mostrarMensaje(35, "intermedio");
mostrarMensaje(28, "experto");
?>
```

---
Al ejecutar el programa, se muestran distintos mensajes según la edad y el nivel de conocimiento en arte latte de cada usuario. Las diferentes llamadas a la función permiten comprobar que los condicionales funcionan correctamente y que los mensajes se adaptan a cada caso.

Este ejercicio permite reforzar el uso de funciones y estructuras condicionales en PHP dentro de un contexto creativo relacionado con el arte latte y el mundo del café. 

La correcta implementación de la función mostrarMensaje demuestra cómo es posible personalizar el comportamiento de una aplicación web según los datos del usuario, mejorando la interacción y la experiencia. Además, este tipo de prácticas resulta fundamental para desarrollar una lógica de programación sólida, que será esencial en proyectos reales donde sea necesario tomar decisiones automáticas basadas en datos introducidos por el usuario. De este modo, el ejercicio contribuye directamente al aprendizaje de estructuras más complejas y al desarrollo de aplicaciones web dinámicas y funcionales.
