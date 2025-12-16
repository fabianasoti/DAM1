<?php

	$cliente = [
		"nombre" => "Fabiana Victoria",
		"apellidos" => "Sotillo",
		"email" => "info@fabiana.com"
	];
	
	foreach($cliente as $clave=>$valor){
		echo "<legend>".$clave."</legend>";	// También podemos usar "<label>"
		echo "<input type='text' value='".$valor."'>";
	}
	
?>
