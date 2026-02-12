<?php
require_once 'validador.php';

echo "<h3>Pruebas Unitarias: Validador</h3>";
// Camino: Campos vacíos
echo "Test Vacíos: " . (validarEntradas("", "") === "vacios" ? "PASÓ" : "FALLÓ") . "<br>";
// Camino: Longitud corta
echo "Test Longitud: " . (validarEntradas("user", "123") === "longitud_corta" ? "PASÓ" : "FALLÓ") . "<br>";
// Camino: Todo OK
echo "Test OK: " . (validarEntradas("user", "123456") === "ok" ? "PASÓ" : "FALLÓ") . "<br>";
?>
