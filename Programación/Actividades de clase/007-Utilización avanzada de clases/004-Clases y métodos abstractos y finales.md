```
Reloj analógico web
2026 Fabiana Sotillo
Uso de temporizadores reutilizables asincrónicos 
para dibujar un reloj analógico con el uso de setTimeout
```

---
En este ejercicio se desarrolla un reloj en un archivo html que implementa un temporizador reutilizable para mostrar la hora actual mediante un reloj analógico dibujado en un lienzo HTML utilizando el contexto 2D. 

El programa emplea conceptos fundamentales como variables, funciones, temporizadores, estructuras de control y manejo de fechas, con el objetivo de representar gráficamente el paso del tiempo mediante manecillas que se actualizan cada segundo. 

La finalidad principal es comprender el funcionamiento del temporizador y del sistema de coordenadas del lienzo, así como aplicar correctamente el uso de funciones matemáticas para convertir valores temporales en ángulos de rotación.

---
El programa se basa en el uso de un temporizador controlado mediante setTimeout, que permite ejecutar una función de forma recursiva cada segundo.

El lienzo se crea mediante la etiqueta ```<canvas>``` y se configura con un tamaño fijo. A través del contexto 2D se dibujan las manecillas del reloj, calculando sus ángulos a partir de la hora, los minutos y los segundos obtenidos del objeto Date.

Cada actualización limpia el lienzo para volver a dibujar el reloj completo, lo que genera la sensación de movimiento continuo. Para mejorar la apariencia visual, se han modificado los colores y grosores de las manecillas respecto al ejemplo original, manteniendo la misma lógica de funcionamiento.

---
A continuación se muestra el código funcional completo:
```
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Reloj con temporizador</title>
</head>
<body>

<canvas id="reloj"></canvas>

<script>
/*
Reloj analógico con temporizador
2026 Fabiana Victoria Sotillo
Programa que muestra un reloj analógico utilizando un temporizador asíncrono
que se actualiza cada segundo mediante el contexto 2D de Canvas.
*/

let temporizador = null; // Temporizador inicialmente desactivado
let lienzo = document.getElementById("reloj");
lienzo.width = 500;
lienzo.height = 500;

let contexto = lienzo.getContext("2d");
contexto.lineCap = "round";

// Función principal del bucle
function bucle() {
    let fecha = new Date();

    let hora = fecha.getHours();
    let minuto = fecha.getMinutes();
    let segundo = fecha.getSeconds();

    // Limpiar el lienzo
    contexto.clearRect(0, 0, lienzo.width, lienzo.height);

    let centroX = lienzo.width / 2;
    let centroY = lienzo.height / 2;

    // Manecilla de la hora
    contexto.lineWidth = 35;
    contexto.strokeStyle = "purple";
    let anguloHora = hora * (Math.PI * 2 / 12) - Math.PI / 2;

    contexto.beginPath();
    contexto.moveTo(centroX, centroY);
    contexto.lineTo(
        centroX + Math.cos(anguloHora) * 90,
        centroY + Math.sin(anguloHora) * 90
    );
    contexto.stroke();

    // Manecilla de los minutos
    contexto.lineWidth = 20;
    contexto.strokeStyle = "orange";
    let anguloMinuto = minuto * (Math.PI * 2 / 60) - Math.PI / 2;

    contexto.beginPath();
    contexto.moveTo(centroX, centroY);
    contexto.lineTo(
        centroX + Math.cos(anguloMinuto) * 140,
        centroY + Math.sin(anguloMinuto) * 140
    );
    contexto.stroke();

    // Manecilla de los segundos
    contexto.lineWidth = 4;
    contexto.strokeStyle = "black";
    let anguloSegundo = segundo * (Math.PI * 2 / 60) - Math.PI / 2;

    contexto.beginPath();
    contexto.moveTo(centroX, centroY);
    contexto.lineTo(
        centroX + Math.cos(anguloSegundo) * 180,
        centroY + Math.sin(anguloSegundo) * 180
    );
    contexto.stroke();

    // Círculo central
    contexto.fillStyle = "black";
    contexto.beginPath();
    contexto.arc(centroX, centroY, 10, 0, Math.PI * 2);
    contexto.fill();

    // Marco exterior del reloj
    contexto.lineWidth = 15;
    contexto.strokeStyle = "gray";
    contexto.beginPath();
    contexto.arc(centroX, centroY, 200, 0, Math.PI * 2);
    contexto.stroke();

    // Reinicio del temporizador
    clearTimeout(temporizador);
    temporizador = setTimeout(bucle, 1000);
}

// Activar temporizador
temporizador = setTimeout(bucle, 1000);

</script>

</body>
</html>
```

---
El programa muestra un reloj analógico funcional que se actualiza cada segundo de forma automática. Las manecillas giran suavemente y representan correctamente la hora actual del sistema. El temporizador se controla de forma asíncrónica y permite que el bucle se ejecute indefinidamente.

En este ejercicio se han aplicado correctamente los conceptos de temporización, funciones, variables, uso del objeto Date y dibujo mediante el contexto 2D de Canvas. 

La implementación del temporizador mediante llamadas con setTimeout permite controlar de forma precisa la actualización del reloj, garantizando un funcionamiento fluido y estable. 

Este tipo de ejercicios resulta fundamental para reforzar la lógica de programación y comprender el funcionamiento de los procesos que van a destiempo, sentando las bases para el desarrollo de aplicaciones gráficas más complejas e interactivas en entornos web.
