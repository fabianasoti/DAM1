```
'''
Selección y Acceso a Elementos en JavaScript
2026 Fabiana Sotillo
Localización de elementos, lectura de contenido y modificación dinámica
'''
```

---
En este ejercicio se trabaja el concepto de selección y acceso a elementos del documento mediante JavaScript. Mediante los siguiente scripts, es posible localizar elementos HTML, leer su contenido y modificarlo de forma dinámica. El objetivo de esta práctica es aprender a seleccionar elementos utilizando distintos métodos, acceder a su contenido y crear nuevos elementos de forma automática mediante bucles, reforzando así la comprensión del funcionamiento interno de una página web interactiva.

El ejercicio se compone de tres archivos HTML que permiten practicar distintas formas de acceso y manipulación de elementos del documento.

#### Selección por ID y escritura de contenido
En el archivo 002-escribir.html se utilizan identificadores únicos (ID) para seleccionar tres elementos ```<div>``` con los nombres rojo, verde y azul. Estos elementos se seleccionan mediante el método document.querySelector() y se modifica su contenido utilizando la propiedad textContent.
Este método permite acceder a cualquier elemento del documento usando selectores CSS y modificar su contenido de forma directa.

#### Selección por etiqueta y lectura de contenido
En el archivo 001-lectura.html se selecciona un elemento utilizando su etiqueta HTML, en este caso ```<p>```. Una vez seleccionado, se muestra tanto el elemento completo como su contenido de texto utilizando document.write().
Este ejercicio permite observar la diferencia entre mostrar el nodo completo y mostrar únicamente el texto que contiene.

#### Creación dinámica de elementos con bucles

En el archivo 004-microblog.html se implementa un pequeño sistema de blog donde los artículos se almacenan en un array. Mediante un bucle for, se recorren los artículos y se generan dinámicamente etiquetas ```<h3>``` que se insertan dentro del contenedor ```<main>```.
Este proceso demuestra cómo se pueden crear contenidos dinámicos en una página web a partir de estructuras de datos.

---
A continuación se muestra la implementación completa de cada ejercicio.

Escritura de texto en elementos seleccionados por ID:
```
<script>
	document.querySelector("#rojo").textContent = "texto rojo"
	document.querySelector("#verde").textContent = "texto verde"
	document.querySelector("#azul").textContent = "texto azul"
</script>
```
En este código se seleccionan los elementos mediante su ID y se les asigna contenido de texto.


Lectura de un elemento por su etiqueta:
```
<script>
	const elemento = document.querySelector("p");
	document.write(elemento);
	document.write(elemento.textContent);
</script>
```
Aquí se selecciona el párrafo y se muestra tanto el objeto HTML como su contenido textual.


Creación dinámica de artículos en un microblog:
```
<script>
	const articulos = [
		"Primer articulo","Segundo artículo","Tercer artículo"
	];
	const contenedor = document.querySelector("main");
	for(let i = 0;i<articulos.length;i++){
		contenedor.innerHTML += "<h3>"+articulos[i]+"<h3>";			
	}
</script>
```
Este código recorre el array de artículos y genera automáticamente los títulos dentro del contenedor principal.

---
Este ejercicio permite comprender de forma práctica cómo JavaScript interactúa con el documento HTML a través de la Selección y Acceso a Elementos. Mediante la selección de elementos por ID y por etiqueta, la lectura de su contenido y la creación dinámica de nuevos elementos, se refuerza el concepto de manipulación de documentos web.

Estos conocimientos son esenciales para el desarrollo de aplicaciones interactivas, ya que, permiten modificar la estructura y el contenido de una página en tiempo real, mejorando la experiencia del usuario y ampliando las posibilidades de diseño y funcionalidad de los sitios web.
