<?php
	$cliente = [];
	$cliente['nombre'] = "Fabiana Victoria";
	$cliente['apellidos'] = "Sotillo Cuevas";
	$cliente['email'] = "info@fabiana.com";
	
	$json = json_encode($cliente);
	echo $json;
?>
