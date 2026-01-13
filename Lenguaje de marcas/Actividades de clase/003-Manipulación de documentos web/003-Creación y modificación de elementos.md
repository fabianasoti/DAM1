```
'''
Concepto de eventos en JavaScript
2026 Fabiana Sotillo
Eventos Click y Manipulación Dinámica de Elementos en JavaScript
'''
```

---
En este ejercicio se trabaja el concepto de eventos en JavaScript, concretamente el evento click, junto con la creación y manipulación dinámica de elementos HTML y el consumo de datos en formato JSON. Los eventos permiten que una página web responda a las acciones del usuario, mientras que la manipulación del DOM posibilita crear interfaces interactivas y dinámicas. El objetivo de esta práctica es aprender a generar botones dinámicamente, asociarles eventos, consumir datos desde archivos JSON y representar la información en forma de tablas, reforzando así el desarrollo de aplicaciones web interactivas.

---
El ejercicio está compuesto por varios archivos que trabajan conjuntamente para practicar distintos aspectos de la programación con JavaScript.

#### Creación dinámica de botones
En el archivo 002-crear varios botones.html se generan botones dinámicamente a partir de un array de textos. Para cada elemento del array se crea un botón mediante document.createElement() y se añade al contenedor <nav>. A cada botón se le asocia un evento click para detectar la interacción del usuario.

#### Consumo de datos JSON
En el archivo 005-consumo json.html se utiliza la función fetch() para cargar un archivo JSON externo (botones.json). Los datos se convierten a formato JavaScript mediante el método .json() y se muestran en la consola. A uno de los botones se le añade un evento click que permite mostrar en consola el texto del botón pulsado.

#### Recuperación de datos JSON y creación de tabla
En el archivo 007-recuperamos json tabla.html se recuperan datos desde un archivo tabla.json. Estos datos se recorren y posteriormente se utilizan para crear dinámicamente una tabla HTML, generando filas y celdas según el contenido del JSON.

#### Creación de una interfaz base
En el archivo 010-creo interfaz base.html se construye una interfaz básica compuesta por un menú lateral (nav) y una zona principal (main). En el menú se añaden botones dinámicamente mediante JavaScript, a los cuales se les asocia un evento click que muestra en consola un mensaje indicando que se ha pulsado el botón.

#### Estilo dinámico en tablas
En el archivo 009-estilo en la tabla.html se crea una tabla a partir de un archivo JSON y se aplican estilos mediante CSS. Además, se añade un evento click a uno de los botones para modificar el estilo de la tabla de forma dinámica, permitiendo cambiar su apariencia según la interacción del usuario.

---
Aplicación práctica:

Creación dinámica de botones:
```
<script>
	let botones = ['clientes','productos','pedidos'];
	let contenedor = document.querySelector("nav");
	botones.forEach(function(texto_boton){
		let boton = document.createElement("button");
		boton.textContent = texto_boton;
		boton.addEventListener("click", function(){
			console.log("Has hecho click en el botón");
		});
		contenedor.appendChild(boton);
	});
</script>
```


Consumo de JSON:
```
<script>
	fetch("botones.json")
	.then(function(respuesta){
		return respuesta.json();				
	})
	.then(function(datos){
		console.log(datos);
	});
</script>
```


Creación de tabla a partir de JSON:
```
<script>
	fetch("tabla.json")
	.then(function(respuesta){
		return respuesta.json();
	})
	.then(function(datos){
		let contenedor = document.querySelector("body");
		let tabla = document.createElement("table");
		contenedor.appendChild(tabla);

		datos.forEach(function(linea){
			let fila = document.createElement("tr");
			linea.forEach(function(celda){
				let data = document.createElement("td");
				data.textContent = celda;
				fila.appendChild(data);
			});
			tabla.appendChild(fila);
		});
	});
</script>
```

---
Este ejercicio permite comprender de forma práctica cómo funcionan los eventos en JavaScript y cómo se pueden utilizar para crear interfaces interactivas. Mediante la creación dinámica de botones, la asignación de eventos click, el consumo de datos JSON y la generación automática de tablas, se refuerza el uso del DOM como herramienta fundamental para el desarrollo web moderno. Estos conocimientos son esenciales para crear aplicaciones dinámicas, ya que permiten reaccionar a las acciones del usuario y mostrar información de forma flexible y estructurada. Además, la combinación de JavaScript con JSON facilita la construcción de aplicaciones conectadas a datos externos, algo imprescindible en proyectos web.
