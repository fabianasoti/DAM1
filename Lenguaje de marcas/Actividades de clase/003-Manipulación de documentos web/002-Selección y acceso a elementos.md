# Selección y acceso a elementos en JavaScript

El presente ejercicio tiene como objetivo afianzar los conocimientos sobre la selección y manipulación de elementos del DOM utilizando JavaScript. A través del acceso a elementos mediante identificadores, etiquetas y contenedores, se pretende comprender cómo JavaScript permite modificar dinámicamente el contenido de una página web, leer información existente y generar nuevos elementos de forma automática. Estos conceptos son fundamentales en el desarrollo de aplicaciones web interactivas.

---
En esta práctica se trabajan los conceptos de selección de elementos mediante ID y etiquetas, modificación de contenido mediante la propiedad textContent, lectura de elementos con document.write() y creación dinámica de nodos HTML utilizando bucles. Para ello, se utilizan distintos archivos HTML proporcionados en el entorno de trabajo, los cuales permiten observar de forma directa cómo se accede y manipula el contenido de una página desde JavaScript.

El uso del DOM (Document Object Model) permite representar la estructura del documento HTML como un conjunto de objetos accesibles desde JavaScript, facilitando la interacción con cada uno de sus elementos.

---
Aplicación práctica
1. Selección de elementos por ID y escritura de contenido

En el archivo 002-escribir.html se seleccionan los elementos que poseen los identificadores rojo, verde y azul, y se escribe contenido en cada uno de ellos utilizando la propiedad textContent.
```
<script>
  document.getElementById("rojo").textContent = "Este es el color rojo";
  document.getElementById("verde").textContent = "Este es el color verde";
  document.getElementById("azul").textContent = "Este es el color azul";
</script>
```
Este código permite modificar el contenido interno de cada elemento seleccionado, demostrando cómo JavaScript puede interactuar directamente con el HTML.

2. Selección de un elemento por etiqueta y lectura de contenido

En el archivo 001-lectura.html se selecciona un elemento mediante su etiqueta <p> y se muestra tanto el elemento completo como su contenido.
```
<script>
  let parrafo = document.querySelector("p");
  console.log(parrafo);
  document.write(parrafo.textContent);
</script>
```
Este fragmento permite observar el elemento completo en la consola y mostrar su contenido directamente en la página web.

3. Creación dinámica de artículos en un microblog

En el archivo 004-microblog.html se modifica el contenido para generar dinámicamente una lista de artículos utilizando un bucle for.
```
<script>
  let articulos = [
    "Primer artículo del blog",
    "Segundo artículo del blog",
    "Tercer artículo del blog"
  ];

  let contenedor = document.querySelector("main");

  for (let i = 0; i < articulos.length; i++) {
    let titulo = document.createElement("h3");
    titulo.textContent = articulos[i];
    contenedor.appendChild(titulo);
  }
</script>
```
Este código recorre una lista de artículos y crea dinámicamente elementos <h3> que se insertan dentro del contenedor <main>, generando así el contenido del blog de forma automática.

---
Como resultado de esta práctica, se obtiene una correcta comprensión del acceso a elementos HTML mediante diferentes métodos de selección, así como de la modificación y generación dinámica de contenido utilizando JavaScript. Se demuestra la capacidad de leer información existente, modificarla y crear nuevos elementos en tiempo real.

En este ejercicio se han aplicado de forma práctica los conceptos fundamentales de selección y acceso a elementos del DOM mediante JavaScript. Se ha trabajado la lectura y modificación de contenido, así como la creación dinámica de elementos mediante bucles, lo que permite construir interfaces interactivas y dinámicas. Estos conocimientos son esenciales en el desarrollo web moderno, ya que permiten adaptar el contenido de una página a las necesidades del usuario y a la lógica de la aplicación, sentando las bases para proyectos más complejos basados en JavaScript.
