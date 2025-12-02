<?php
	class Gato{
		function __construct($nombre,$edad){
			$this->nombre = $nombre;
			$this->edad = $edad;
		}
	}
	
	$gato1 = new Gato("Micifu",1);
	$gato2 = new Gato("Lucifer",2);
	
	var_dump($gato1);
?>

