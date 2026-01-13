<?php
// Configuración de credenciales
$host     = "localhost";
$usuario  = "el_jocarsa_noticias";
$password = "Periodico123$";
$base_datos = "el_jocarsa_noticias";

// Crear la conexión
$conexion = new mysqli($host, $usuario, $password, $base_datos);

// Verificar si hay errores
if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

$conexion->set_charset("utf8mb4");

echo "Conexión exitosa a la base de datos.";
?>
