```
'''
Eliminación de elementos y temporizadores en documentos web con JavaScript
2026 Fabiana Sotillo
Creación de una tabla interactiva y de un elemento animado con desplazamiento aleatorio
'''
```

---
El presente ejercicio tiene como objetivo aplicar los conceptos de manipulación dinámica de elementos y documentos mediante JavaScript, centrándose en la eliminación de elementos HTML a través de eventos interactivos y en el uso de temporizadores para generar movimiento automático en la interfaz. A través de la creación de una tabla interactiva y de un elemento animado que se desplaza de forma aleatoria, se pretende comprender cómo JavaScript permite controlar el comportamiento y la estructura de una página web en tiempo real, reforzando el uso de eventos, funciones y temporizadores.

En esta práctica se trabajan dos conceptos fundamentales del desarrollo web con JavaScript: la eliminación dinámica de elementos mediante eventos onclick y el uso de temporizadores con setTimeout para crear animaciones automáticas.

Por un lado, se genera una tabla con múltiples filas que pueden eliminarse al hacer clic sobre ellas, lo que permite comprender cómo interactuar con los elementos y modificarlos dinámicamente. Por otro lado, se crea un elemento visual que se mueve de forma automática por la pantalla mediante posiciones aleatorias, utilizando funciones y temporizadores.

---
## Aplicación práctica:

#### 1. Creación de una tabla interactiva con eliminación de filas
En el primer ejercicio se genera una tabla con 20 filas y tres celdas por fila. Cada fila contiene el texto "Prueba" y dispone de un evento onclick que permite eliminarla al hacer clic.
```
<!doctype html>
<html>
<head>
</head>
<body>
  <table></table>
  <script>
    let tabla = document.querySelector("table")
    for(let i = 0; i < 20; i++){
      let fila = document.createElement("tr")
      fila.innerHTML = "<td>Prueba</td><td>Prueba</td><td>Prueba</td>"
      tabla.appendChild(fila)
      fila.onclick = function(){
        this.remove()
      }
    }
  </script>
</body>
</html>
```
Este código permite crear una tabla dinámica donde cada fila se elimina al ser pulsada por el usuario.


#### 2. Movimiento de un elemento mediante temporizadores
En el segundo ejercicio se crea un cuadrado rojo que se desplaza de forma automática por la pantalla utilizando posiciones aleatorias y temporizadores.
```
<!doctype html>
<html>
<head>
  <style>
    #jugador{width:20px;height:20px;background:red;position:absolute;transition:all 1s;}
  </style>
</head>
<body>
  <div id="jugador"></div>
  <script>
    let temporizador = setTimeout("bucle()",1000);
    
    function bucle(){
      document.querySelector("#jugador").style.left = Math.random()*500+"px"
      document.querySelector("#jugador").style.top = Math.random()*500+"px"
      clearTimeout(temporizador)
      temporizador = setTimeout("bucle()",1000);
    }
  </script>
</body>
</html>
```
Este bloque de código permite mover el elemento cada segundo a una posición aleatoria, creando un efecto de animación.


#### 3. Integración de ambos conceptos
En el ejercicio final se combinan ambos ejemplos en una única página web que muestra una tabla interactiva y un cuadrado rojo en movimiento.
```
<!doctype html>
<html>
<head>
  <style>
    #jugador{width:20px;height:20px;background:red;position:absolute;transition:all 1s;}
  </style>
</head>
<body>
  <table></table>
  <div id="jugador"></div>
  <script>
    let tabla = document.querySelector("table")
    for(let i = 0; i < 20; i++){
      let fila = document.createElement("tr")
      fila.innerHTML = "<td>Prueba</td><td>Prueba</td><td>Prueba</td>"
      tabla.appendChild(fila)
      fila.onclick = function(){
        this.remove()
      }
    }
    
    let temporizador = setTimeout("bucle()",1000);
    
    function bucle(){
      document.querySelector("#jugador").style.left = Math.random()*500+"px"
      document.querySelector("#jugador").style.top = Math.random()*500+"px"
      clearTimeout(temporizador)
      temporizador = setTimeout("bucle()",1000);
    }
  </script>
</body>
</html>
```

---
Como resultado, se obtiene una página web interactiva en la que el usuario puede eliminar filas de una tabla con un solo clic y observar un elemento animado que se mueve automáticamente por la pantalla. Esto demuestra la capacidad de JavaScript para manipular elementos del DOM en tiempo real y generar interfaces dinámicas.

En este ejercicio se han aplicado los conceptos de eliminación dinámica de elementos y uso de temporizadores para crear movimiento automático en una interfaz web. La combinación de eventos onclick, manipulación de elementos y documentos y funciones con temporizadores permite construir aplicaciones interactivas que responden a las acciones del usuario y generan comportamientos dinámicos. Esta práctica refuerza el pensamiento algorítmico y constituye una base fundamental para el desarrollo de interfaces web.
