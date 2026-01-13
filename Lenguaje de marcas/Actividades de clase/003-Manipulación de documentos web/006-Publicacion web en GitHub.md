```
'''
CV web Fabiana Sotillo
2026 Fabiana Sotillo
Publicación de una web en GitHub Pages
'''
```

---
En este ejercicio se trabaja el proceso completo de publicación de una página web en Internet mediante el servicio GitHub Pages, utilizando repositorios públicos y estructuración básica en HTML y CSS. Se aplican conceptos fundamentales como la creación de repositorios, subida de archivos, configuración de publicación automática y verificación del despliegue web. El objetivo principal es aprender a publicar un currículum online accesible desde cualquier navegador y gestionarlo correctamente desde GitHub.

El ejercicio consiste en crear y configurar repositorios en GitHub para publicar una web personal y un portafolio, siguiendo las instrucciones de los archivos proporcionados en clase. Para ello, se ha trabajado con:

- Creación del repositorio curriculum en GitHub.
- Subida de los archivos HTML del currículum.
- Configuración de GitHub Pages desde la pestaña Settings > Pages.
- Verificación de la publicación final mediante la URL generada por GitHub.
Además, se ha aplicado una correcta estructura HTML semántica junto con estilos CSS integrados para maquetar el currículum en formato responsive.

---
A continuación, el paso a paso del desarrollo del ejercicio:

#### 1. Creación del repositorio y publicación
Se creó el repositorio público llamado Curriculum en GitHub y se subió el archivo index.html con el contenido del currículum. Posteriormente, se configuró GitHub Pages seleccionando la rama principal como fuente de publicación.
Tras realizar los commits y el push correspondiente, GitHub generó automáticamente la URL pública:
**<https://fabianasoti.github.io/Curriculum/>**

#### 2. Estructura del currículum en HTML
La página web está construida mediante una estructura clara y profesional utilizando HTML y CSS. Se emplean etiquetas semánticas como:
- ```<main>``` para el contenedor principal.
- ```<aside>``` para la columna lateral.
- ```<section>``` para los bloques de contenido.
- ```<article>``` para cada experiencia laboral.
La maquetación se realiza mediante CSS Grid para dividir el diseño en dos columnas, con un diseño responsive adaptable a dispositivos móviles.

#### 3. Maquetación y estilos CSS
Se aplican estilos CSS integrados en el propio documento que permiten:
- Diseño en dos columnas.
- Tipografía clara y legible.
- Diseño responsive mediante media queries.
- Separación visual por secciones.

#### 4. Verificación de la publicación
Tras esperar el tiempo de despliegue de GitHub Pages, se accedió correctamente a la URL pública y se comprobó que:
- La página carga correctamente.
- Los estilos se aplican correctamente.
- La estructura es responsive.
- El contenido se visualiza de forma correcta.

A continuación se muestra el código HTML que conforma la web del CV:

```
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Currículum Vitae de Fabiana Sotillo. Formación en Desarrollo de Aplicaciones Multiplataforma." />
  <title>CV | Fabiana Sotillo</title>

  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: Arial, Helvetica, sans-serif;
      background-color: #f4f4f4;
      color: #222;
      line-height: 1.5;
    }

    .cv {
      max-width: 900px;
      margin: 40px auto;
      background: #ffffff;
      display: grid;
      grid-template-columns: 1fr 2fr;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }

    /* Columna izquierda */
    .sidebar {
      background-color: #E6E6FA;
      color: #222;
      padding: 30px 25px;
    }

    .sidebar h1 {
      font-size: 2.2rem;
      margin-bottom: 20px;
      line-height: 1.1;
    }

    .sidebar section {
      margin-bottom: 30px;
    }

    .sidebar h2 {
      font-size: 1.1rem;
      text-transform: uppercase;
      margin-bottom: 10px;
      border-bottom: 1px solid #ffffff55;
      padding-bottom: 5px;
    }

    .sidebar p,
    .sidebar li {
      font-size: 0.95rem;
      margin-bottom: 6px;
    }

    .sidebar ul {
      list-style: none;
      padding-left: 0;
    }
    
    .imagen {
			width: 250px;
			height: 250px;
			margin: 0 auto 25px;
			border-radius: 5%;
			overflow: hidden;
			background-color: #bbb; /* color visible si aún no hay imagen */
		}

		.imagen img {
			width: 100%;
			height: 100%;
			object-fit: cover;
		}


    /* Columna derecha */
    .content {
			padding: 35px 40px;
			display: flex;
			flex-direction: column;
			justify-content: space-between;
		}


    .content section {
      margin-bottom: 35px;
    }

    .content h2 {
      font-size: 1.3rem;
      margin-bottom: 15px;
      border-bottom: 2px solid #ddd;
      padding-bottom: 5px;
    }

    .experience {
      margin-bottom: 20px;
    }

    .experience h3 {
      font-size: 1.05rem;
      font-weight: bold;
    }

    .experience span {
      font-size: 0.9rem;
      color: #555;
      display: block;
      margin-bottom: 5px;
    }

    .experience ul {
      padding-left: 18px;
    }

    .experience li {
      margin-bottom: 6px;
    }
    
    .formacion ul{
    	padding-left: 18px;
    }
    
    .formacion li {
      margin-bottom: 6px;
    }

    .profile {
      font-size: 0.95rem;
      text-align: justify;
    }

    /* Responsive */
    @media (max-width: 768px) {
      .cv {
        grid-template-columns: 1fr;
      }

      .sidebar {
        text-align: center;
      }
    }
  </style>
</head>
<body>

  <main class="cv">

    <aside class="sidebar">
    
		  <div class="imagen">
				<img src="imagen_cv.JPEG" alt="Foto de Fabiana Sotillo">
			</div>

      <h1>Fabiana<br />Sotillo</h1>

      <section>
        <h2>Contacto</h2>
        <p>📞 +34 663 966 940</p>
        <p>✉️ fsotillocuevas@gmail.com</p>
        <p>📍 C/ Democracia, Valencia, España</p>
      </section>

      <section>
        <h2>Idiomas</h2>
        <ul>
          <li>Inglés – Nivel Avanzado</li>
          <li>Español – Nativo</li>
        </ul>
      </section>

      <section>
        <h2>Competencias personales</h2>
        <ul>
          <li>Empatía y comunicación efectiva</li>
          <li>Organización y gestión de tareas</li>
          <li>Puntualidad y responsabilidad</li>
          <li>Capacidad resolutiva y adaptable</li>
          <li>Trabajo en equipo</li>
        </ul>
      </section>

      <section>
        <h2>Competencias técnicas</h2>
        <ul>
          <li>MySQL</li>
          <li>Python</li>
          <li>HTML y CSS</li>
          <li>Microsoft Office</li>
          <li>Warehouse Management OS</li>
        </ul>
      </section>
    </aside>

    <section class="content">

      <section>
        <h2>Perfil profesional</h2>
        <p class="profile">
          Profesional proactiva con experiencia en atención al cliente y análisis de existencias. En formación en Desarrollo de Aplicaciones Multiplataforma (DAM), con interés en el sector tecnológico. Destaco por mi adaptabilidad, comunicación y trabajo en equipo, con un fuerte compromiso con el aprendizaje continuo y la mejora de procesos.
        </p>
      </section>

      <section>
        <h2>Experiencia</h2>

        <article class="experience">
          <h3>MYR Hotels – Palacio Vallier</h3>
          <span>Valencia, España | Mayo 2024 – Actualmente</span>
          <ul>
            <li>Atención especializada orientada al cliente</li>
            <li>Administración y gestión de material para eventos</li>
            <li>Aplicación de protocolos formales de restauración</li>
          </ul>
        </article>

        <article class="experience">
          <h3>Taberna del Volapié</h3>
          <span>Valencia, España | Octubre 2022 – Mayo 2024</span>
          <ul>
            <li>Atención al cliente en sala y barra</li>
            <li>Manejo de caja, PDA y TPV</li>
          </ul>
        </article>

        <article class="experience">
          <h3>Bodegas Sodimac</h3>
          <span>Lo Espejo, Chile | Febrero 2020 – Agosto 2022</span>
          <ul>
            <li>Análisis de existencias de productos inventariados</li>
            <li>Creación y asignación de códigos de barra y SKU</li>
            <li>Integración de inventarios con base de datos</li>
          </ul>
        </article>
      </section>
      
      <article class="formacion">
		    <section>
		      <h2>Formación académica</h2>
		      <ul>
		        <li><strong>CEAC FP</strong> – Desarrollo de Aplicaciones Multiplataforma (Cursando)</li>
		        <li><strong>Título de Bachiller</strong> – Homologado en España (Marzo 2022)</li>
		      </ul>
		    </section>
      </article>

      <section>
        <h2>Datos de interés</h2>
        <p>
          Disponibilidad horaria flexible para trabajo presencial, híbrido o remoto, así como desplazamiento dentro de la ciudad de Valencia.
        </p>
      </section>

    </section>

  </main>

</body>
</html>
```

---
Este ejercicio permite comprender el proceso completo de publicación de una web utilizando GitHub Pages,pudiendo así publicar un CV o un portafolio web con estructura HTML semántica y diseño con CSS. 

La práctica refuerza la importancia de la organización de proyectos web y la gestión de repositorios, habilidades fundamentales en el desarrollo web. Además, la creación de un currículum online proporciona una herramienta profesional útil para la inserción laboral en el sector tecnológico.
