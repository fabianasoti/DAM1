# Eventos click y manipulación dinámica de elementos en JavaScript

---
El presente ejercicio tiene como objetivo aplicar los conceptos de eventos click y manipulación dinámica de elementos del DOM utilizando JavaScript, así como reforzar el consumo de datos en formato JSON para la creación de interfaces interactivas. A través de la creación dinámica de botones, la gestión de eventos y la generación de tablas a partir de datos externos, se busca comprender cómo JavaScript permite construir aplicaciones web dinámicas y orientadas a la interacción con el usuario.

---
En esta práctica se trabajan los conceptos fundamentales de creación dinámica de elementos HTML, asignación de eventos click, consumo de datos en formato JSON y generación de contenido dinámico como tablas. Se utilizan distintos archivos base que permiten observar cómo JavaScript interactúa con el DOM para crear botones, procesar información externa y modificar el contenido visual de una página web.

El uso de eventos permite capturar las acciones del usuario, mientras que el consumo de JSON facilita la carga de datos estructurados que pueden ser representados en forma de tablas o listados. Estos conceptos son esenciales en el desarrollo de aplicaciones web modernas.

---
Aplicación práctica
1. Creación dinámica de botones y eventos click

En el archivo 002-crear varios botones.html se generan varios botones de forma dinámica dentro de un contenedor ```<nav>``` y se les asigna un evento click que muestra un mensaje en consola.
```
<script>
  let botones = ["clientes", "productos", "pedidos"];
  let nav = document.querySelector("nav");

  for (let i = 0; i < botones.length; i++) {
    let boton = document.createElement("button");
    boton.textContent = botones[i];
    boton.addEventListener("click", function () {
      console.log("Has hecho click en el botón");
    });
    nav.appendChild(boton);
  }
</script>
```
Este código permite crear una interfaz de navegación básica con botones funcionales.

2. Consumo de datos JSON y evento click

En el archivo 005-consumo json.html se carga un archivo JSON y se muestra su contenido en consola. Además, se añade un evento click a un botón para mostrar el texto del botón pulsado.
```
<script>
  fetch("botones.json")
    .then(response => response.json())
    .then(datos => {
      console.log(datos);
    });

  let boton = document.querySelector("button");
  boton.addEventListener("click", function () {
    console.log(this.textContent);
  });
</script>
```
Este ejercicio permite comprender cómo consumir datos externos y trabajar con ellos desde JavaScript.

3. Recuperación de datos JSON y creación de una tabla

En el archivo 007-recuperamos json tabla.html se cargan datos desde un archivo JSON y se genera una tabla dinámicamente al hacer click en un botón.
```
<script>
  fetch("tabla.json")
    .then(response => response.json())
    .then(datos => {
      let boton = document.querySelector("button");
      boton.addEventListener("click", function () {
        console.log(this.textContent);
        crearTabla(datos);
      });
    });

  function crearTabla(datos) {
    let tabla = document.createElement("table");
    datos.forEach(fila => {
      let tr = document.createElement("tr");
      Object.values(fila).forEach(valor => {
        let td = document.createElement("td");
        td.textContent = valor;
        tr.appendChild(td);
      });
      tabla.appendChild(tr);
    });
    document.body.appendChild(tabla);
  }
</script>
```
Este bloque demuestra cómo transformar datos JSON en una tabla HTML.

4. Creación de una interfaz base con botones dinámicos

En el archivo 010-creo interfaz base.html se construye una interfaz básica con un contenedor ```<nav>``` y botones creados dinámicamente.
```
<script>
  let opciones = ["Inicio", "Clientes", "Productos", "Pedidos"];
  let nav = document.querySelector("nav");

  opciones.forEach(opcion => {
    let boton = document.createElement("button");
    boton.textContent = opcion;
    boton.addEventListener("click", function () {
      console.log("Has hecho click en el botón");
    });
    nav.appendChild(boton);
  });
</script>
```
Este ejercicio permite crear una estructura base para una aplicación web.

5. Estilo dinámico en una tabla

En el archivo 009-estilo en la tabla.html se añade un evento click que permite modificar el estilo de una tabla.
```
<script>
  let boton = document.querySelector("button");
  let tabla = document.querySelector("table");

  boton.addEventListener("click", function () {
    tabla.style.border = "2px solid black";
    tabla.style.backgroundColor = "#f3f4f6";
  });
</script>
```
Este código demuestra cómo JavaScript puede modificar estilos CSS dinámicamente.

---
Como resultado de la práctica, se obtiene una interfaz funcional con botones dinámicos, consumo de datos JSON, generación de tablas interactivas y modificación de estilos mediante eventos click. El usuario puede interactuar con la interfaz y observar cómo se actualiza el contenido de forma inmediata.

En este ejercicio se han aplicado los conceptos fundamentales de creación dinámica de elementos, asignación de eventos click, consumo de datos JSON y manipulación visual de tablas mediante JavaScript. Estas técnicas permiten construir interfaces interactivas, dinámicas y orientadas al usuario, facilitando el desarrollo de aplicaciones web modernas. El dominio de estos conceptos constituye una base sólida para proyectos más complejos que requieran interacción avanzada y gestión dinámica de datos.
