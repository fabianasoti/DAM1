<!doctype html>
<html lang="es">
	<head>
		<title>El fabianazo - Panel de control</title>
		<meta charset="utf-8">
		<link rel="stylesheet" href="css/estilo.css">
	</head>
	<body>
		<nav>
			<button>Noticias</button>
			<button>Autores</button>
		</nav>
		<main>
			<?php
			// Esto se conoce como router (enrutador) ///////////
				if(isset($_GET['accion'])){		// Si hay "accion" en la URL
					if($_GET['accion'] == "nuevo"){		// Si la acción es "nuevo"
						include "inc/create/formulario.php";	// En ese caso mete el formulario
					}else if($_GET['accion'] == "eliminar"){ // Defino la acción eliminar
						include "inc/delete/eliminar.php";		// En ese caso incluyo eliminar.php
					}else if($_GET['accion'] == "editar"){ // Defino la acción editar
          	include "inc/update/formularioactualizar.php";		// En ese caso incluyo el formulario de la edicion.php
          }
				}else{
					include "inc/read/leer.php";	// Enseñame la tabla
				}
			?>
			<a href="?accion=nuevo" id="nuevo">+</a>
		</main>
	</body>
</html>

