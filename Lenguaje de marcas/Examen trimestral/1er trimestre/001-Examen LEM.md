```
Portafolio personal
2025 Fabiana Victoria Sotillo
Página de un portafolio digital: HTML y CSS
```

---
HTML (HyperText Markup Language) permite definir la estructura y el contenido de un documento web mediante etiquetas, mientras que CSS (Cascading Style Sheets) se encarga del diseño y formato, controlando aspectos como colores, fuentes, márgenes y disposición de los elementos

A continuación, se desarrolla la estructura básica de un portafolio web personal utilizando el lenguaje de marcas HTML junto con CSS para la presentación visual.

Se hizo uso de Flexbox, que es un sistema de diseño de CSS que permite ordenar y alinear los elementos de manera flexible dentro de un contenedor. Con propiedades como display: flex o flex: 1, se puede distribuir el espacio fácilmente sin usar medidas fijas, haciendo que la estructura se vea más equilibrada y adaptada. En este caso, Flexbox sirvió para organizar la disposición de los artículos en una cuadrícula, y del contenido de estos a su vez, justificando el texto y estableciendo el tamaño de la imagen dentro del artículo.

También se aplicaron propiedades de color, bordes redondeados, márgenes y sombras para mejorar la apariencia y legibilidad. El objetivo principal fue modificar la sección derecha, agregando nuevos artículos con información y aplicando estilos CSS para lograr un diseño ordenado, limpio y profesional.

El objetivo es comprender cómo estructurar correctamente una web con secciones como cabecera, contenido principal y pie de página, aplicando estilos internos, fuentes personalizadas y modelos de maquetación como Flexbox y Grid.

---
A continuación se ejemplifica el desarrollo del html paso a paso:

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
	
- Luego, en la cabeza se incluyen los metadatos, el título y las etiquetas Open Graph para redes sociales, también se incluye el bloque style, donde irán los estilos CSS.
```
 <head>
    <title>Fabiana Victoria Sotillo</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    <meta name="description" content="Web de Fabiana Victoria Sotillo, estudiante de DAM, crochetera en su tiempo libre">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="keywords" content="programación,desarrollo,clave3,...">
      <meta name="author" content="Fabiana Victoria Sotillo">
      <link rel="icon" href="kermit cute.jpeg" type="image/jpeg">
      <meta property="og:title" content="Fabiana Victoria Sotillo">
      <meta property="og:description" content="Web de Fabiana Victoria Sotillo, estudiante de DAM.">
      <meta property="og:image" content="kermit cute.jpeg">
      <meta property="og:url" content="https://fabianasotillo.com">
      <meta property="og:type" content="website">
			<style>
			</style>
	</head>
```

- Posteriormente, se construye el bloque style,con los estilos CSS, que permite definir colores, fuentes y distribuciones mediante @font-face, Flexbox y Grid, logrando un diseño equilibrado y centrado. 
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
          color:#333366;
          font-family: "ubuntu";
          src:url("BebasNeue-Regular.otf");
        }
        h2,h3{
          color:#777;
          font-family:monospace;
        }
        body{
          background:#f9f9ff;
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
          grid-template-columns:auto auto; /* Y tiene tres columnas */
          gap:20px; /* Separación entre los elementos */
        }
        #contenedor_portafolio{
          width:100%; /* Quiero que la imagen no desborde */
        }
        #contenedor_portafolio article {
				display: flex;
				align-items: flex-start;
				gap: 15px;
				margin-bottom: 15px;
				background: white;
				padding: 10px;               /* ← margen interno (espaciado interno del artículo) */
				border-radius: 8px;          /* ← bordes redondeados */
				box-shadow: 0 0 4px rgba(0, 0, 0, 0.1); /* ← sombra ligera */
				}
      </style>
```

- Se empieza a crear el cuerpo de la página, que presenta una sección de portafolio con varios artículos, los que se multiplican como plantilla para visualizar cómo se verían ingresados muchos artículos, mostrando el uso práctico de la maquetación y la jerarquía visual. Y dentro de esta también se construye el footer.
```
 <body>
    <header>
      <h1>Fabiana Victoria Sotillo</h1>
      <h3>fabiana.victoria.sotillo@alu.ceacfp.es</h3>
    </header>
    <main>
      <section id="portafolio">
        <h3>Portafolio</h3>
        <div id="contenedor_portafolio">
          <article>
          	<h4>Título</h4>
            <p>Descripción</p>
            <p>Categoría</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<h4>Título</h4>
            <p>Descripción</p>
            <p>Categoría</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<h4>Título</h4>
            <p>Descripción</p>
            <p>Categoría</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<h4>Título</h4>
            <p>Descripción</p>
            <p>Categoría</p>
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

A continuación se muestra el código de HTML completo:
```
<!doctype html>
<html lang="es">
  <head>
    <title>Fabiana Victoria Sotillo</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    <meta name="description" content="Web de Fabiana Victoria Sotillo, estudiante de DAM, crochetera en su tiempo libre">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="keywords" content="programación,desarrollo,clave3,...">
      <meta name="author" content="Fabiana Victoria Sotillo">
      <link rel="icon" href="kermit cute.jpeg" type="image/jpeg">
      <meta property="og:title" content="Fabiana Victoria Sotillo">
      <meta property="og:description" content="Web de Fabiana Victoria Sotillo, estudiante de DAM.">
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
          color:#333366;
          font-family: "ubuntu";
          src:url("BebasNeue-Regular.otf");
        }
        h2,h3{
          color:#777;
          font-family:monospace;
        }
        body{
          background:#f9f9ff;
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
          grid-template-columns:auto auto; /* Y tiene tres columnas */
          gap:20px; /* Separación entre los elementos */
        }
        #contenedor_portafolio{
          width:100%; /* Quiero que la imagen no desborde */
        }
        #contenedor_portafolio article {
				display: flex;
				align-items: flex-start;
				gap: 15px;
				margin-bottom: 15px;
				background: white;
				padding: 10px;               /* ← margen interno (espaciado interno del artículo) */
				border-radius: 8px;          /* ← bordes redondeados */
				box-shadow: 0 0 4px rgba(0, 0, 0, 0.1); /* ← sombra ligera */
				}
      </style>
  </head>
  <body>
    <header>
      <h1>Fabiana Victoria Sotillo</h1>
      <h3>fabiana.victoria.sotillo@alu.ceacfp.es</h3>
    </header>
    <main>
      <section id="portafolio">
        <h3>Portafolio</h3>
        <div id="contenedor_portafolio">
          <article>
          	<h4>Título</h4>
            <p>Descripción</p>
            <p>Categoría</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<h4>Título</h4>
            <p>Descripción</p>
            <p>Categoría</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<h4>Título</h4>
            <p>Descripción</p>
            <p>Categoría</p>
            <img src="kermit cute.jpeg" alt="Lovely Kermit The Frog">            
          </article>
          <article>
          	<h4>Título</h4>
            <p>Descripción</p>
            <p>Categoría</p>
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
El documento final presenta una apariencia estructurada y profesional. Los artículos se organizan visualmente con claridad, las tipografías son legibles y los colores suaves contribuyen a una experiencia visual agradable. Además, el uso de sombras, bordes y flexbox mejora la distribución espacial y jerarquía de los elementos.

El documento realizado permite afianzar el uso de HTML y CSS para crear páginas web limpias y funcionales. Se aplicaron principios de estructura, estilo y semántica, comprendiendo la importancia del diseño adaptable y la organización del contenido. Esta práctica sienta las bases para desarrollar sitios más complejos e interactivos en futuras etapas del aprendizaje.

Además, se refuerza el uso de CSS como herramienta esencial para el diseño web, aplicando propiedades de estilo que mejoran la presentación de un documento HTML, aplicando el uso de etiquetas, estilos, flexbox, colores, márgenes, padding y tipografía, logrando una composición equilibrada. 

Al crear la sección de artículos, permite generar una plantilla para ir registrando los futuros proyectos que se realicen, sin necesidad de estructurarlo todo desde cero, y además, aporta orden y estructura al mantener todos los artículos con el mismo formato. Esto también permite sincronizarlo con el formato de una base de datos para poder realizar registros de manera consistente y mantener la información almacenada de manera segura y ordenada.

Es fundamental comprender cómo el diseño y la estructura HTML pueden integrarse de forma armoniosa, permitiendo crear un portafolio personal en la web, lo que puede aportar a construir una identidad digital beneficiosa en el mundo laboral, sentando las bases para el trabajo con estructuras más complejas y adaptativas en futuros proyectos.
