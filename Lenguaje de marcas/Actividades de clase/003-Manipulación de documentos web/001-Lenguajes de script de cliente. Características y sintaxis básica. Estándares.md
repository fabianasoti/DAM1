#Uso de fechas y funciones con retorno en JavaScript

El presente ejercicio tiene como objetivo reforzar los conocimientos fundamentales sobre el manejo de fechas y la utilización de funciones con retorno en JavaScript, aplicando distintos métodos de salida de información en una página web. A través de la creación de objetos de tipo Date, la definición de funciones con return y la generación de contenido dinámico mediante bucles, se busca comprender cómo JavaScript permite trabajar con datos temporales y mostrar información de forma interactiva en el navegador.

---
En esta práctica se trabajan tres conceptos principales: la creación de objetos de fecha mediante la clase Date, el uso de funciones que devuelven valores mediante la instrucción return y la generación dinámica de contenido utilizando bucles. Para ello, se desarrollan varios archivos HTML que permiten observar el funcionamiento de estos conceptos directamente en el navegador.

El ejercicio permite comprender cómo JavaScript puede utilizarse tanto para procesar información como para mostrarla al usuario mediante distintos métodos de salida, como la consola del navegador y la escritura directa en el documento HTML.

---
Aplicación práctica
1. Creación de un objeto de fecha

En primer lugar, se crea un archivo HTML (index.html) en el que se instancia un objeto de tipo Date y se muestra su contenido en la consola del navegador.
```
<script>
  // new quiere decir que instancio un objeto
  let hoy = new Date();
  console.log(hoy);
</script>
```
Este código permite obtener la fecha y hora actual del sistema y visualizarla en la consola, lo que resulta útil para depuración y comprobaciones internas.

2. Uso de funciones con retorno

A continuación, se crea un segundo archivo HTML (salidaConReturn.html) donde se define una función que recibe parámetros y devuelve un mensaje personalizado utilizando la instrucción return.
```
<script>
  function diHola(nombre, edad) {
    return "Hola, " + nombre + " tienes " + edad + " años, ¿cómo estás?";
  }
  document.write(diHola("Jose Vicente", 47));
</script>
```
En este caso, la función procesa los datos recibidos y devuelve un texto que posteriormente se muestra en la página web mediante document.write. Esto demuestra la utilidad de las funciones para encapsular lógica y reutilizar código.

3. Generación dinámica de contenido con bucles

Por último, se desarrolla un tercer archivo HTML (calendario.html) que genera un calendario simple utilizando un bucle for.
```
<script>
  // Esto es un calendario
  for (let dia = 1; dia <= 31; dia++) {
    document.write("<div>" + dia + "</div>");
  }
</script>
```
Este código permite crear dinámicamente una lista de días del 1 al 31, demostrando cómo JavaScript puede generar contenido de forma automática sin necesidad de escribir cada elemento manualmente.

---
Como resultado de esta práctica, se obtiene una comprensión clara del uso del objeto Date para trabajar con fechas, del uso de funciones con return para devolver información procesada y del empleo de bucles para generar contenido dinámico en una página web. Además, se aplican distintos métodos de salida, como console.log y document.write, lo que permite visualizar los resultados tanto en la consola como directamente en el documento.

En este ejercicio se han aplicado de forma práctica los conceptos fundamentales relacionados con el manejo de fechas, el uso de funciones con retorno y la generación dinámica de contenido en JavaScript. La utilización del objeto Date permite trabajar con información temporal, mientras que las funciones con return facilitan el procesamiento y reutilización de datos. Asimismo, el uso de bucles permite automatizar la creación de contenido, lo que resulta esencial en el desarrollo de aplicaciones web dinámicas. Este tipo de prácticas resulta fundamental para afianzar la lógica de programación y sentar las bases para el desarrollo de sistemas más complejos en JavaScript.
