El objetivo de este ejercicio es diseñar y estructurar una página web tipo “Currículum Vitae” utilizando HTML y CSS. El propósito es aplicar los fundamentos de lenguaje de marcas para organizar información personal y profesional de forma clara, estética y semánticamente correcta.

Se utiliza HTML (HyperText Markup Language); lenguaje de marcado que estructura el contenido de la web mediante etiquetas jerárquicas. CSS (Cascading Style Sheets) para definir el estilo visual de los elementos HTML, incluyendo colores, márgenes, posiciones y fondos.
Se hacen uso de etiquetas semánticas: como ```<section>, <article>, <h1> o <p>```, que ayudan a organizar la información con significado lógico.

- El documento HTML empieza con su estructura inicial, su respectivo ```<!doctype html>```, y sus meta datos en el ```<head>```, donde se define el idioma en el que se trabajará,
```
<!doctype html>
<html lang="es">
		<head>
			<title>Curriculum</title>
			<meta charset="utf-8">
```

- Se introduce el bloque de css ```<style>```; donde se define el color de fondo, la tipografía y su tamaño, entre otros detalles visuales. Y además se usa "flexbox" para dividir el espacio entre dos secciones: la izquierda y la derecha, y la disposición de los elementos de cada una por separado:
```
		<style>
			html{background:grey;font-family:sans-serif;font-size:11px;text-align:justify;}
			body{
			width:600px;background:white;
			margin:auto;display:flex;}
			#izquierda img{width:90%;}
			#izquierda{flex:1;background:GhostWhite;padding:20px;color:black;}
			#derecha{flex:4;padding:20px;}
			#derecha article{display:flex;align-items:justify;gap:20px;}
			#derecha article *{padding:5px;margin:0px;}
            .texto{padding-left:20px !important;margin-left:10px;}
		</style>
	</head>
```

- Cada parte del currículum está estructurado con su respectiva etiqueta semántica, y todo lo visible de la página va dentro de la etiqueta ```<body>```:
	- La etiqueta ```<section>```  agrupa los bloques principales ("izquierda" por un lado, y "derecha" por el otro, para poder diseñarlos de maneras diferentes por separado sin que se mezcle su estilo), ejemplo:
		```
		<section id="izquierda">
		```

	- La etiqueta ```<article>``` organiza subapartados como “Sobre mí”, “Contacto”, “Idiomas” o “Experiencia profesional”. Y aquí mismo se evidencia la etiqueta ```<ul> y <li>```, que presentan listas con sangrías.
		```
		<article>
				<h3>Idiomas</h3>
				<ul>
					<li>Inglés - Intermedio</li>
					<li>Español - Nativo</li>
				</ul>
			</article>
		```
		
	- Los encabezados ```<h1>``` a ```<h5>``` jerarquizan el contenido informativo, creando títulos de distintos tamaños.
		```
		<h4>Analista de existencias</h4>
		<h5>Bodegas Sodimac. Lo Espejo, RM, Chile.</h5>
		<h5>Febrero 2020 - Agosto 2022</h5>
		```
	
Acontinuación se ilustra el código completo de HTML:
```
<!doctype html>
<html lang="es">
<head>
  <title>Curriculum</title>
  <meta charset="utf-8">
  <style>
    html{background:grey;font-family:sans-serif;font-size:11px;text-align:justify;}
    body{width:600px;background:white;margin:auto;display:flex;}
    #izquierda img{width:90%;}
    #izquierda{flex:1;background:GhostWhite;padding:20px;color:black;}
    #derecha{flex:4;padding:20px;}
    #derecha article{display:flex;align-items:justify;gap:20px;}
    #derecha article *{padding:5px;margin:0px;}
    .texto{padding-left:20px !important;margin-left:10px;}
  </style>
</head>
<body>
  <section id="izquierda">
    <img src="fvsc cv.jpg">
    <article>
      <h3>Sobre mí</h3>
      <p>Profesional proactiva con experiencia en atención al cliente...</p>
    </article>
    <article>
      <h3>Contacto</h3>
      <ul>
        <li>fsotillocuevas@gmail.com</li>
        <li>+34 663 966 940</li>
        <li>Valencia, España</li>
      </ul>
    </article>
    <article>
      <h3>Idiomas</h3>
      <ul>
        <li>Inglés - Intermedio</li>
        <li>Español - Nativo</li>
      </ul>
    </article>
    <article>
      <h3>Datos de interés</h3>
      <ul>
        <li>Modalidad de trabajo híbrida o remota.</li>
        <li>Facilidad para el trabajo en equipo.</li>
      </ul>
    </article>
    <article>
      <h3>Habilidades</h3>
      <ul>
        <li>Resolución de conflictos</li>
        <li>Trabajo bajo presión</li>
        <li>Organización</li>
      </ul>
    </article>
  </section>

  <section id="derecha">
    <h1>Fabiana Sotillo</h1>
    <h2>Estudiante de DAM</h2>

    <div id="experiencia">
      <h3>Experiencia profesional</h3>
      <article>
        <div>
          <h4>Camarera de hostelería</h4>
          <h5>MYR Hotels, Palacio Vallier. Valencia, España.</h5>
          <h5>Mayo 2024 - Actualmente</h5>
          <div class="texto">
            <ul>
              <li>Atención especializada orientada al cliente.</li>
              <li>Administración y gestión de material para eventos.</li>
              <li>Protocolos formales de restauración.</li>
            </ul>
          </div>
        </div>
      </article>
      <article>
        <div>
          <h4>Camarera de hostelería</h4>
          <h5>Taberna del Volapié. Valencia, España.</h5>
          <h5>Octubre 2022 - Mayo 2024</h5>
          <div class="texto">
            <ul>
              <li>Atención al cliente.</li>
              <li>Experiencia en sala y barra.</li>
              <li>Manejo de caja, PDA y TPV.</li>
            </ul>
          </div>
        </div>
      </article>
      <article>
        <div>
          <h4>Analista de existencias</h4>
          <h5>Bodegas Sodimac. Lo Espejo, RM, Chile.</h5>
          <h5>Febrero 2020 - Agosto 2022</h5>
          <div class="texto">
            <ul>
              <li>Análisis de existencias de productos inventariados.</li>
              <li>Creación y asignación de códigos de barra y SKU.</li>
              <li>Concatenación con la base de datos.</li>
            </ul>
          </div>
        </div>
      </article>
    </div>

    <div id="educacion">
      <h3>Educación</h3>
      <article>
        <div>
          <h4>Desarrollo de Aplicaciones Multiplataforma</h4>
          <h5>CEAC FP. 2025 - 2027</h5>
        </div>
      </article>
      <article>
        <div>
          <h4>Bachiller en ciencias</h4>
          <h5>Marzo, 2022. Título homologado en España.</h5>
        </div>
      </article>
    </div>
  </section>
</body>
</html>
```

Este ejercicio permite comprender la estructura jerárquica del HTML y la importancia del CSS para definir la presentación visual del contenido.
Se aplicaron conceptos fundamentales como el uso de secciones semánticas, listas, encabezados jerarquizados y estilos internos.
Además, se trabajó con el modelo de Flexbox para organizar el diseño en columnas, mejorando la legibilidad y la usabilidad del sitio.

En conjunto, este trabajo demuestra cómo los lenguajes de marcas son esenciales para la creación de interfaces web organizadas, accesibles y estéticamente coherentes, sentando las bases para proyectos más complejos en desarrollo front-end.
