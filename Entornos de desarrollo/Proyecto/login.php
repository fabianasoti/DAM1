<?php
// Inicializamos variables
$errores = [];
$email = '';
$password = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Limpiar datos
    $email = trim($_POST["email"]);
    $password = trim($_POST["password"]);

    // Validar email
    if (empty($email)) {
        $errores[] = "El email es obligatorio.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errores[] = "El formato del email no es válido.";
    }

    // Validar contraseña
		if (empty($password)) {
				$errores[] = "La contraseña es obligatoria.";
		} elseif (strlen($password) < 8) {
				$errores[] = "La contraseña debe tener al menos 8 caracteres.";
		} elseif (!preg_match('/[\W_]/', $password)) {
				$errores[] = "La contraseña debe contener al menos un carácter especial.";
		}


    // Si no hay errores
    if (empty($errores)) {
        echo "<p style='color:green;'>Login validado correctamente </p>";
        // Aquí iría la validación contra la base de datos
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>

<h2>Iniciar sesión</h2>

<?php
// Mostrar errores
if (!empty($errores)) {
    echo "<ul style='color:red;'>";
    foreach ($errores as $error) {
        echo "<li>$error</li>";
    }
    echo "</ul>";
}
?>

<form method="POST" action="">
    <label>Email:</label><br>
    <input type="email" name="email" value="<?php echo htmlspecialchars($email); ?>"><br><br>

    <label>Contraseña:</label><br>
    <input type="password" name="password"><br><br>

    <button type="submit">Login</button>
</form>

</body>
</html>

