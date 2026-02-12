<?php
session_start(); [cite: 275]
require_once 'validador.php';
require_once 'bd.php';

if ($_SERVER["REQUEST_METHOD"] !== "POST") { [cite: 303]
    header("Location: ../pages/index.php"); [cite: 304]
    exit();
}

$validacion = validarEntradas($_POST['credencial'] ?? '', $_POST['password'] ?? '');

if ($validacion !== "ok") {
    header("Location: ../pages/index.php?error=" . $validacion); [cite: 310]
    exit();
}

try {
    $resultado = autenticarUsuario($conexion, $_POST['credencial'], $_POST['password']); [cite: 314]
    
    if (is_string($resultado)) { // Si devuelve "usuario_no_existe" o "password_incorrecta"
        header("Location: ../pages/index.php?error=" . $resultado); [cite: 316, 319]
        exit();
    }

    // Login correcto
    $_SESSION['usuario_id'] = $resultado['id']; [cite: 324]
    $_SESSION['usuario_nombre'] = $resultado['nombre']; [cite: 325]
    $_SESSION['rol'] = $resultado['rol']; [cite: 326]
    
    actualizarUltimaConexion($conexion, $resultado['id']); [cite: 327]
    header("Location: ../pages/dashboard.php"); [cite: 328]
    exit();

} catch (Exception $e) {
    die("Error en el sistema: " . $e->getMessage()); [cite: 331]
}
?>
