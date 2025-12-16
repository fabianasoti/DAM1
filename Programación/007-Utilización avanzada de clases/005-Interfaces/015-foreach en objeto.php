<?php

	$cliente = [
		"nombre" => "Fabiana Victoria",
		"apellidos" => "Sotillo",
		"email" => "info@fabiana.com"
	];
	
	foreach($cliente as $clave=>$valor){
		echo $clave.": ".$valor."<br>";
	}
	
?>
