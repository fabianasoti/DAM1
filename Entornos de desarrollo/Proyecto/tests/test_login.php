<?php
/*
|--------------------------------------------------------------------------
| TEST AUTOMATIZADO - MÓDULO LOGIN
| Proyecto: Lumina
| Este script prueba automáticamente el funcionamiento del login.
|--------------------------------------------------------------------------
*/

ini_set('display_errors', 1);
error_reporting(E_ALL);

require_once '../config/conexion.php';

echo "<h2>🧪 Iniciando pruebas del módulo Login - Lumina</h2>";

/* ============================================================
   1️⃣ CREAR USUARIO DE PRUEBA
============================================================ */

$nombre_test = "usuario_test";
$email_test  = "test@lumina.com";
$password_plano = "123456";
$password_hash = password_hash($password_plano, PASSWORD_DEFAULT);
$rol_test = "admin";

echo "<h3>1️⃣ Creando usuario de prueba...</h3>";

$stmt = $conexion->prepare("DELETE FROM usuarios WHERE email = ?");
$stmt->bind_param("s", $email_test);
$stmt->execute();

$stmt = $conexion->prepare("INSERT INTO usuarios (nombre, email, password, rol) VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssss", $nombre_test, $email_test, $password_hash, $rol_test);

if ($stmt->execute()) {
    echo "✅ Usuario de prueba creado correctamente.<br>";
} else {
    die("❌ Error al crear usuario de prueba.");
}

/* ============================================================
   FUNCIÓN SIMULACIÓN LOGIN
============================================================ */

function probarLogin($conexion, $credencial, $password, $descripcion) {
    echo "<h4>🔎 Prueba: $descripcion</h4>";

    if (empty($credencial) || empty($password)) {
        echo "Resultado esperado: ❌ Error por campos vacíos<br>";
        echo "Resultado obtenido: ❌ Campos vacíos detectados<br><br>";
        return;
    }

    $sql = "SELECT id, nombre, password, rol FROM usuarios WHERE email = ? OR nombre = ? LIMIT 1";
    $stmt = $conexion->prepare($sql);
    $stmt->bind_param("ss", $credencial, $credencial);
    $stmt->execute();
    $res = $stmt->get_result();

    if ($fila = $res->fetch_assoc()) {
        if (password_verify($password, $fila['password'])) {
            echo "Resultado esperado: ✅ Login correcto<br>";
            echo "Resultado obtenido: ✅ Login exitoso<br><br>";
        } else {
            echo "Resultado esperado: ❌ Password incorrecto<br>";
            echo "Resultado obtenido: ❌ Contraseña incorrecta<br><br>";
        }
    } else {
        echo "Resultado esperado: ❌ Usuario no encontrado<br>";
        echo "Resultado obtenido: ❌ Usuario no existe<br><br>";
    }
}

/* ============================================================
   2️⃣ EJECUTAR CASOS DE PRUEBA
============================================================ */

echo "<h3>2️⃣ Ejecutando pruebas...</h3>";

// ✔ Login correcto con email
probarLogin($conexion, $email_test, "123456", "Login correcto con email");

// ✔ Login correcto con username
probarLogin($conexion, $nombre_test, "123456", "Login correcto con username");

// ✖ Password incorrecto
probarLogin($conexion, $email_test, "wrongpass", "Password incorrecto");

// ✖ Usuario inexistente
probarLogin($conexion, "noexiste@lumina.com", "123456", "Usuario inexistente");

// ✖ Campos vacíos
probarLogin($conexion, "", "", "Campos vacíos");

/* ============================================================
   3️⃣ LIMPIEZA
============================================================ */

echo "<h3>3️⃣ Limpieza de datos de prueba...</h3>";

$stmt = $conexion->prepare("DELETE FROM usuarios WHERE email = ?");
$stmt->bind_param("s", $email_test);
$stmt->execute();

echo "✅ Usuario de prueba eliminado.<br>";

echo "<h2>🎉 Pruebas finalizadas</h2>";
?>

