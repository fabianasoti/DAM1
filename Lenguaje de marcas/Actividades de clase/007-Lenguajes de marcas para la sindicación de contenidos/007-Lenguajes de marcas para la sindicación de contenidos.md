```
Estructura Curriculum
2025 Fabiana Victoria Sotillo
Curriculum Vitae con HTML y CSS
```

---
En este ejercicio se trabajó con HTML y CSS para crear una página web con buena estructura y presentación visual. El lenguaje HTML se usó para organizar el contenido del currículum —como los títulos, párrafos e imágenes—, mientras que CSS se aplicó para darle color, estilo y formato a cada elemento.

Se hizo uso de Flexbox, que es un sistema de diseño de CSS que permite ordenar y alinear los elementos de manera flexible dentro de un contenedor. Con propiedades como display: flex o flex: 1, se puede distribuir el espacio fácilmente sin usar medidas fijas, haciendo que la estructura se vea más equilibrada y adaptada. En este caso, Flexbox sirvió para dividir el cuerpo del currículum en dos partes: la columna izquierda con los datos personales y la derecha con la experiencia y formación.

También se aplicaron propiedades de color, bordes redondeados, márgenes y sombras para mejorar la apariencia y legibilidad. El objetivo principal fue modificar la sección derecha, agregando nuevos artículos con información y aplicando estilos CSS para lograr un diseño ordenado, limpio y profesional.

---
El trabajo se realizó sobre una estructura HTML existente, con su estructura básica + CSS, compuesta por dos secciones principales: #izquierda y #derecha, distribuidas mediante flexbox.

En la sección derecha se agregaron nuevos elementos ```<article>``` para simular experiencias profesionales y formación académica, incluyendo títulos, subtítulos, párrafos descriptivos e imágenes de logotipos.

En el código CSS se aplicaron las siguientes mejoras:

- Se definió un fondo claro (#f9f9ff) para la sección derecha, generando contraste con el panel lateral izquierdo.
```
	#derecha {
	flex: 4;
	padding: 20px;
	background: #f9f9ff;
	}
```

- Se añadieron bordes redondeados, sombras y márgenes internos (padding) para mejorar la legibilidad y el aspecto visual de los artículos.
```
#derecha article {
	display: flex;
	align-items: flex-start;
	gap: 15px;
	margin-bottom: 15px;
	background: white;
	padding: 10px;               /* ← margen interno (espaciado interno del artículo) */
	border-radius: 8px;          /* ← bordes redondeados */
	box-shadow: 0 0 4px rgba(0, 0, 0, 0.1); /* ← sombra ligera */
}
```

- Se personalizaron los encabezados (h1, h2, h3, h4, h5) mediante variaciones de color, peso tipográfico y espaciado.
```
#derecha h1 {
	margin-bottom: 0;
	color: #333366;              /* ← color personalizado */
}

#derecha h2 {
	margin-top: 2px;
	font-weight: normal;         /* ← peso tipográfico más ligero */
	color: #666;                 /* ← tono más suave */
}

#izquierda h3 {
	border-bottom: 1px solid #888; /* ← separación visual */
	padding-bottom: 5px;
	margin-bottom: 5px;
}

#derecha article h4 {
	margin: 0;
	color: #333366;              /* ← color igual al h1 */
}

#derecha article h5 {
	margin: 3px 0;
	color: #777;                 /* ← tono gris claro */
}
```

- Los artículos de experiencia profesional se organizaron con display: flex para alinear imágenes y texto lateralmente.
```
#derecha article {
	display: flex;               /* ← organiza los elementos en fila (imagen + texto) */
	align-items: flex-start;     /* ← alinea verticalmente arriba */
	gap: 15px;                   /* ← espacio entre la imagen y el texto */
}
```

- Se aplicaron colores suaves como Lavender y #333366 para crear una armonía entre los elementos.
	- El color Lavender se aplicó al fondo del panel izquierdo (#izquierda):
	```
	#izquierda {
		flex: 1;
		background: Lavender;        /* ← color suave del panel lateral */
		padding: 20px;
		color: black;
	}
	```
	- El color #333366 se aplicó en títulos para destacar manteniendo la armonía de colores:
	```
	#derecha h1, 
	#derecha article h4, 
	#formacion h3, 
	#formacion h4 {
		color: #333366;              /* ← tono azul grisáceo suave */
	}
	```
	
- Se mejoró la legibilidad general ajustando la fuente sans-serif y un tamaño de texto uniforme.
```
html {
	background: grey;
	font-family: sans-serif;     /* ← tipografía */
	font-size: 11px;             /* ← tamaño uniforme en todo el texto */
	text-align: justify;
}
```

Estos ajustes permitieron que el documento mostrara una estructura equilibrada, moderna y profesional, cumpliendo con los principios de jerarquía visual y consistencia tipográfica.

---
A continuación se ilustra el código de html funcional completo:

```
<!doctype html>
<html lang="es">
	<head>
		<title>Curriculum</title>
		<meta charset="utf-8">
		<style>
			html {
				background: grey;
				font-family: sans-serif;
				font-size: 11px;
				text-align: justify;
			}

			body {
				width: 600px;
				background: white;
				margin: auto;
				display: flex;
				box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
			}

			/* SECCIÓN IZQUIERDA */
			#izquierda {
				flex: 1;
				background: Lavender;
				padding: 20px;
				color: black;
			}
			#izquierda img {
				width: 100%;
				border-radius: 10px;
				margin-bottom: 15px;
			}
			#izquierda h3 {
				border-bottom: 1px solid #888;
				padding-bottom: 5px;
				margin-bottom: 5px;
			}
			#izquierda ul {
				list-style: none;
				padding: 0;
			}
			#izquierda li {
				margin-bottom: 5px;
			}

			/* SECCIÓN DERECHA */
			#derecha {
				flex: 4;
				padding: 20px;
				background: #f9f9ff;
			}
			#derecha h1 {
				margin-bottom: 0;
				color: #333366;
			}
			#derecha h2 {
				margin-top: 2px;
				font-weight: normal;
				color: #666;
			}
			#derecha p {
				margin-top: 10px;
				margin-bottom: 20px;
				line-height: 1.4;
			}

			/* ARTÍCULOS DE EXPERIENCIA */
			#derecha article {
				display: flex;
				align-items: flex-start;
				gap: 15px;
				margin-bottom: 15px;
				background: white;
				padding: 10px;
				border-radius: 8px;
				box-shadow: 0 0 4px rgba(0, 0, 0, 0.1);
			}
			#derecha article img {
				width: 60px;
				height: 60px;
				border-radius: 8px;
				object-fit: cover;
			}
			#derecha article h4 {
				margin: 0;
				color: #333366;
			}
			#derecha article h5 {
				margin: 3px 0;
				color: #777;
			}
			#derecha article p {
				margin: 5px 0 0;
			}

			/* SECCIÓN DE FORMACIÓN */
			#formacion h3 {
				color: #333366;
				border-bottom: 1px solid #aaa;
				padding-bottom: 5px;
				margin-top: 25px;
			}
			#formacion article {
				background: white;
				padding: 10px;
				margin-bottom: 10px;
				border-radius: 8px;
				box-shadow: 0 0 4px rgba(0, 0, 0, 0.1);
			}
			#formacion h4 {
				margin: 0;
				color: #333366;
			}
			#formacion h5 {
				margin: 3px 0;
				color: #777;
			}
		</style>
	</head>
	<body>
		<section id="izquierda">
			<img src="kermit cute.jpeg" alt="Foto de perfil">
			<article>
				<h3>Contacto</h3>
				<ul>
					<li>fsotillocuevas@gmail.com</li>
					<li>+34 663 966 940</li>
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
				<h3>Habilidades</h3>
				<ul>
					<li>Comunicación</li>
					<li>Trabajo en equipo</li>
					<li>Gestión del tiempo</li>
					<li>Adaptabilidad</li>
				</ul>
			</article>
		</section>

		<section id="derecha">
			<h1>Fabiana Sotillo</h1>
			<h2>Estudiante de DAM</h2>
			<p>Profesional dinámica y proactiva con experiencia en hostelería y análisis de inventarios. Destaco por mis habilidades comunicativas, capacidad de adaptación y orientación al trabajo en equipo. Experiencia en atención al cliente, protocolos de restauración y sistemas de gestión.</p>
			
			<div id="experiencia">
				<h3>Experiencia profesional</h3>

				<article>
					<img src="logo.png" alt="Logo empresa">
					<div class="texto">
						<h4>Camarera de Sala</h4>
						<h5>2024 - Actualidad | Restaurante La Perfumería</h5>
						<p>Atención al cliente. Desarrollé habilidades de multitarea y comunicación efectiva en un entorno dinámico.</p>
					</div>
				</article>

				<article>
					<img src="logo.png" alt="Logo empresa">
					<div class="texto">
						<h4>Analista de Inventario</h4>
						<h5>2020 - 2022 | Centro de Distribución Sodimac</h5>
						<p>Encargada del control de stock, registro de productos y seguimiento de pedidos. Implementé mejoras en la organización del almacén que optimizaron el proceso de revisión de inventario.</p>
					</div>
				</article>
			</div>

			<div id="formacion">
				<h3>Formación académica</h3>
				<article>
					<h4>Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM)</h4>
					<h5>2025 - Actualidad | CEAC FP</h5>
					<p>Formación enfocada en la programación, bases de datos y desarrollo de software multiplataforma. Uso de lenguajes como Python, HTML y SQL.</p>
				</article>
			</div>
		</section>
	</body>
</html>
```

---
El documento final presenta una apariencia profesional y armónica. Los artículos se organizan visualmente con claridad, las tipografías son legibles y los colores suaves contribuyen a una experiencia visual agradable. Además, el uso de sombras, bordes y flexbox mejora la distribución espacial y jerarquía de los elementos.

Este ejercicio permitió reforzar el uso de CSS como herramienta esencial para el diseño web, aplicando propiedades de estilo que mejoran la presentación de un documento HTML. Se practicó el uso de etiquetas, estilos, flexbox, colores, márgenes, padding y tipografía, logrando una composición equilibrada y visualmente agradable.
El resultado demuestra la importancia de lo visual en el desarrollo de interfaces web y su relación directa con la experiencia del usuario y la presentación del contenido.
Este tipo de práctica es fundamental para comprender cómo el diseño y la estructura HTML pueden integrarse de forma armoniosa mediante CSS, sentando las bases para el trabajo con estructuras más complejas y adaptativas en futuros proyectos.