<?php
// 1. Incluimos la conexión primero
require_once 'conexion.php'; 

// 2. Realizamos la consulta (el código que tú pusiste)
$resultado = $conexion->query("SELECT noticias.titulo, noticias.contenido, autores.nombre 
FROM noticias 
JOIN autores ON noticias.id_autor = autores.id_autor");

// 3. Pintamos el HTML
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Listado de Noticias</title>
</head>
<body>
    <h1>Últimas Noticias</h1>
    <?php
    while ($fila = $resultado->fetch_assoc()) {
        echo "<div>";
        echo "<h2>".$fila['titulo']."</h2>";
        echo "<p>".$fila['contenido']."</p>";
        echo "<small>Autor: <strong>".$fila['nombre']."</strong></small>";
        echo "<hr>";
        echo "</div>";
    }
    ?>
</body>
</html>
