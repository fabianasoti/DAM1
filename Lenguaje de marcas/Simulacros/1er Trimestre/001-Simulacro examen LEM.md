```
Portafolio web
2025 Fabiana Victoria Sotillo
Página de un portafolio digital
```

---
HTML (HyperText Markup Language) permite definir la estructura y el contenido de un documento web mediante etiquetas, mientras que CSS (Cascading Style Sheets) se encarga del diseño y formato, controlando aspectos como colores, fuentes, márgenes y disposición de los elementos

En este ejercicio se desarrolla la estructura básica de una página web personal utilizando el lenguaje de marcas HTML junto con CSS para la presentación visual.

El objetivo es comprender cómo estructurar correctamente una web con secciones como cabecera, contenido principal y pie de página, aplicando estilos internos, fuentes personalizadas y modelos de maquetación modernos como Flexbox y Grid.

---
- El documento se estructura con etiquetas semánticas que organizan el contenido: ```<header>, <main> y <footer>```.
```
<!doctype html>
<html lang="es">
  <head>
	</head>
	<body>
		<header>
		</header>
		<main>
		</main>
		<footer>
		</footer>
	</body>
```
	
- En la cabeza se incluyen los metadatos, el título y las etiquetas Open Graph para redes sociales, también se incluye el bloque style, donde irá los estilos CSS.
```
<head>
    <title>Fabiana Victoria Sotillo</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    <meta name="description" content="Web de Fabiana Victoria Sotillo Cuevas, estudiante de DAM, crochetera en su tiempo libre">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="keywords" content="programación,desarrollo,clave3,...">
      <meta name="author" content="Fabiana Victoria Sotillo">
      <link rel="icon" href="kermit cute.jpeg" type="image/jpeg">
      <meta property="og:title" content="Fabiana Victoria Sotillo">
      <meta property="og:description" content="Web de Fabiana Victoria Sotillo Cuevas, estudiante de DAM, crochetera en su tiempo libre">
      <meta property="og:image" content="kermit cute.jpeg">
      <meta property="og:url" content="https://fabianasotillo.com">
      <meta property="og:type" content="website">
      <style>
			</style>
</head>
```

- En los estilos CSS se definen colores, fuentes y distribuciones mediante @font-face, Flexbox y Grid, logrando un diseño equilibrado y centrado. 
```
<style>
			/*
					@font-face{
					font-family: "ubuntu";
					src:url("https://static.jocarsa.com/fuentes/ubuntu-font-family-0.83/Ubuntu-R.ttf");
			*/
			@font-face{
					font-family: "ubuntu";
					src:url("BebasNeue-Regular.otf");
			}
			h1{
				color:MediumSlateBlue;
				font-family: "ubuntu";
				src:url("BebasNeue-Regular.otf");
			}
			h2,h3{
				color:MediumSlateBlue;
				font-family:monospace;
			}
			body{
				background:Lavender;
			}
			header,main,footer{
				width:750px; /* Establece el fondo de los elementos */
				background:white; /* Establece el fondo de los elementos */
				margin:auto; /* Centralo en la pantalla */
				padding:20px; /* Pon un poco de margen interior */
			}
			#inicio img{
				width:100px;        /* No quiero que la imagen se salga */
			}
			.bloque{
				display:flex; /* El bloque de texto e imagen quiero que sea flex */
				gap:20px; /* Distancia entre los elementos*/
			}
			.bloque img{
				flex:1; /* Ocupa una unidad flex */
				width:50%; /* Ocupa el 50% de la anchura */
				height:50%; /* Ocupa el 50% de la altura */
			}
			.bloque p{
				flex:1; /* Ocupa una unidad flex */
				font-size:10px; /* Edito el tamaño del texto */
				text-align:justify; /* Edito la alineación del texto*/
			}
			#diseño .bloque{
				flex-direction: row-reverse; /* Invertimos el orden  un elemento*/
			}
			#contenedor_portafolio{
				display:grid;   /* Este elemento es una rejilla*/
				grid-template-columns:auto auto auto; /* Y tiene tres columnas */
				gap:20px; /* Separación entre los elementos */
			}
			#contenedor_portafolio{
				width:100%; /* Quiero que la imagen no desborde */
			}
			form{
				display:flex; /* Quiero que el formulario sea flex */
				flex-direction:column; /* Y quiero que sea columna */
				flex:1; /* Tiene 1 unidad flex */
				gap:10px;
			}
</style>
```

- El cuerpo de la página presenta una sección de portafolio con varios artículos que combinan texto e imágenes, mostrando el uso práctico de la maquetación y la jerarquía visual. Y dentro de esta también se construye el footer.
```
<body>
    <header>
      <h1>Fabiana Victoria Sotillo</h1>
      <h2>fabiana.victoria.sotillo@alu.ceacfp.es</h2>
    </header>
    <main>
      <section id="portafolio">
        <h3>Portafolio</h3>
        <div id="contenedor_portafolio">
          <article>
          	<p>Categoría</p>
            <h4>Título</h4>
            <p>Descripción</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<p>Categoría</p>
            <h4>Título</h4>
            <p>Descripción</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<p>Categoría</p>
            <h4>Título</h4>
            <p>Descripción</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<p>Categoría</p>
            <h4>Título</h4>
            <p>Descripción</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
        </div>
      </section>
    </main>
    <footer>
          <p>&copy; 2025 Fabiana Sotillo</p>
    </footer>
```

---

A continuación se muestra el código de HTML completo:
```
<!doctype html>
<html lang="es">
  <head>
    <title>Fabiana Victoria Sotillo</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    <meta name="description" content="Web de Fabiana Victoria Sotillo Cuevas, estudiante de DAM, crochetera en su tiempo libre">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="keywords" content="programación,desarrollo,clave3,...">
      <meta name="author" content="Fabiana Victoria Sotillo">
      <link rel="icon" href="kermit cute.jpeg" type="image/jpeg">
      <meta property="og:title" content="Fabiana Victoria Sotillo">
      <meta property="og:description" content="Web de Fabiana Victoria Sotillo Cuevas, estudiante de DAM, crochetera en su tiempo libre">
      <meta property="og:image" content="kermit cute.jpeg">
      <meta property="og:url" content="https://fabianasotillo.com">
      <meta property="og:type" content="website">
      <style>
        /*
            @font-face{
            font-family: "ubuntu";
            src:url("https://static.jocarsa.com/fuentes/ubuntu-font-family-0.83/Ubuntu-R.ttf");
        */
        @font-face{
            font-family: "ubuntu";
            src:url("BebasNeue-Regular.otf");
        }
        h1{
          color:MediumSlateBlue;
          font-family: "ubuntu";
          src:url("BebasNeue-Regular.otf");
        }
        h2,h3{
          color:MediumSlateBlue;
          font-family:monospace;
        }
        body{
          background:Lavender;
        }
        header,main,footer{
          width:750px; /* Establece el fondo de los elementos */
          background:white; /* Establece el fondo de los elementos */
          margin:auto; /* Centralo en la pantalla */
          padding:20px; /* Pon un poco de margen interior */
        }
        #inicio img{
          width:100px;        /* No quiero que la imagen se salga */
        }
        .bloque{
          display:flex; /* El bloque de texto e imagen quiero que sea flex */
          gap:20px; /* Distancia entre los elementos*/
        }
        .bloque img{
          flex:1; /* Ocupa una unidad flex */
          width:50%; /* Ocupa el 50% de la anchura */
          height:50%; /* Ocupa el 50% de la altura */
        }
        .bloque p{
          flex:1; /* Ocupa una unidad flex */
          font-size:10px; /* Edito el tamaño del texto */
          text-align:justify; /* Edito la alineación del texto*/
        }
        #diseño .bloque{
          flex-direction: row-reverse; /* Invertimos el orden  un elemento*/
        }
        #contenedor_portafolio{
          display:grid;   /* Este elemento es una rejilla*/
          grid-template-columns:auto auto auto; /* Y tiene tres columnas */
          gap:20px; /* Separación entre los elementos */
        }
        #contenedor_portafolio{
          width:100%; /* Quiero que la imagen no desborde */
        }
        form{
          display:flex; /* Quiero que el formulario sea flex */
          flex-direction:column; /* Y quiero que sea columna */
          flex:1; /* Tiene 1 unidad flex */
          gap:10px;
        }
      </style>
  </head>
  <body>
    <header>
      <h1>Fabiana Victoria Sotillo</h1>
      <h2>fabiana.victoria.sotillo@alu.ceacfp.es</h2>
    </header>
    <main>
      <section id="portafolio">
        <h3>Portafolio</h3>
        <div id="contenedor_portafolio">
          <article>
          	<p>Categoría</p>
            <h4>Título</h4>
            <p>Descripción</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<p>Categoría</p>
            <h4>Título</h4>
            <p>Descripción</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<p>Categoría</p>
            <h4>Título</h4>
            <p>Descripción</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<p>Categoría</p>
            <h4>Título</h4>
            <p>Descripción</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
        </div>
      </section>
    </main>
    <footer>
          <p>&copy; 2025 Fabiana Sotillo</p>
    </footer>
  </body>
</html>
```

---	
El ejercicio permite afianzar el uso de HTML y CSS para crear páginas web limpias y funcionales. Se aplicaron principios de estructura, estilo y semántica, comprendiendo la importancia del diseño adaptable y la organización del contenido. Esta práctica sienta las bases para desarrollar sitios más complejos e interactivos en futuras etapas del aprendizaje.
