<?php
	$host = "localhost";
	$user = "el_jocarsa_noticias";
	$pass = "Periodico123$";
	$db   = "periodico";
	$conexion = new mysqli($host, $user, $pass, $db);
	$sql = "SELECT * FROM noticias";
	$resultado = $conexion->query($sql);
	while ($fila = $resultado->fetch_assoc()) {
		echo '
			<article>
				<h3>'.$fila['titulo'].'</h3>
				<time>'.$fila['fecha_publicacion'].'</time>
				<p>'.$fila['id_autor'].'</p>
				<p>'.$fila['contenido'].'</p>
			</article>
		';
	}
	$conexion->close();
			
?>
