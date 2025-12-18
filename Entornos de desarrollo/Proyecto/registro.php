<?php
/****************************
* CONFIGURACIÓN MYSQL
****************************/
$host = "localhost";
$user = "diarioemocional";
$pass = "Diarioemocional123$";
$db   = "diarioemocional";

$conexion = new mysqli($host, $user, $pass, $db);
if ($conexion->connect_error) {
    die("Error de conexión");
}

/****************************
* LÓGICA DE REGISTRO
****************************/
$errores = [];
$exito = false;

// 1. INICIALIZAMOS VARIABLES
// Definimos las variables vacías para que existan en el primer "load" de la página
// y no tengamos errores de "Undefined variable" en el HTML.
$nombre   = "";
$apellido = "";
$email    = "";
$edad     = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Recogida de datos
    // Al asignar aquí, las variables ya tienen el valor que escribió el usuario
    $nombre   = trim($_POST["nombre"]);
    $apellido = trim($_POST["apellido"]);
    $email    = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $edad     = $_POST["edad"]; // Mantenemos el string para el value, luego convertimos a int
    $password = $_POST["password"];

    // 2. VALIDACIONES DE PHP
    if (empty($nombre) || empty($apellido) || empty($email) || empty($password)) {
        $errores[] = "Todos los campos son obligatorios.";
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errores[] = "El formato del email no es válido.";
    }

    // Validación de edad (convertimos a entero para validar, pero usaremos $edad en el form)
    if (empty($edad) || intval($edad) < 1) {
        $errores[] = "La edad no es válida.";
    }

    if (strlen($password) < 8 || !preg_match('/[A-Z]/', $password) || !preg_match('/[0-9]/', $password)) {
        $errores[] = "La contraseña debe tener al menos 8 caracteres, una mayúscula y un número.";
    }

    // 3. VERIFICAR SI EL EMAIL YA EXISTE
    if (empty($errores)) {
        $checkEmail = $conexion->prepare("SELECT id FROM usuarios WHERE email = ?");
        $checkEmail->bind_param("s", $email);
        $checkEmail->execute();
        $checkEmail->store_result();
        
        if ($checkEmail->num_rows > 0) {
            $errores[] = "Este email ya está registrado.";
        }
        $checkEmail->close();
    }

    // 4. INSERTAR SI NO HAY ERRORES
    if (empty($errores)) {
        $passwordHash = password_hash($password, PASSWORD_DEFAULT);
        $edadInt = intval($edad); // Convertimos para la BD

        $stmt = $conexion->prepare("INSERT INTO usuarios (nombre, apellido, email, edad, password) VALUES (?, ?, ?, ?, ?)");
        $stmt->bind_param("sssis", $nombre, $apellido, $email, $edadInt, $passwordHash);

        if ($stmt->execute()) {
            $exito = true;
            // Opcional: Limpiar variables tras éxito para vaciar el formulario
            // $nombre = $apellido = $email = $edad = ""; 
        } else {
            $errores[] = "Error al registrar el usuario en la base de datos.";
        }
        $stmt->close();
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro Emocional</title>
    <style>
        /* Estilos (Sin cambios) */
        *{ box-sizing:border-box; font-family:'Segoe UI',sans-serif; }
        body{ margin:0; min-height:100vh; display:flex; justify-content:center; align-items:center; background:linear-gradient(135deg,#cdb4db,#bde0fe); }
        .login-container{ background:#fff; width:100%; max-width:450px; padding:32px; border-radius:20px; box-shadow:0 18px 35px rgba(0,0,0,.15); }
        h2{ text-align:center; color:#4a4e69; margin-bottom: 20px; }
        label{ font-size:13px; color:#4a4e69; font-weight: bold; }
        input{ width:100%; padding:10px; border-radius:10px; border:1px solid #cdb4db; margin-top:5px; margin-bottom:15px; }
        button{ width:100%; padding:12px; border:none; border-radius:14px; background:linear-gradient(135deg,#9d4edd,#5fa8d3); color:#fff; font-size:16px; font-weight:bold; cursor:pointer; }
        .errores{ background:#fde2e4; border-left:5px solid #ff6b6b; padding:10px; border-radius:8px; margin-bottom:15px; font-size:14px; color: #721c24; }
        .exito{ background:#d4edda; border-left:5px solid #28a745; padding:10px; border-radius:8px; margin-bottom:15px; font-size:14px; color: #155724; }
        .link{ display: block; text-align: center; margin-top: 15px; font-size: 13px; color: #9d4edd; text-decoration: none; }
    </style>
</head>
<body>

<div class="login-container">
    <h2>Crear Cuenta</h2>

    <?php if (!empty($errores)): ?>
        <div class="errores">
            <?php foreach ($errores as $e): echo "<p style='margin:0'>• $e</p>"; endforeach; ?>
        </div>
    <?php endif; ?>

    <?php if ($exito): ?>
        <div class="exito">¡Cuenta creada con éxito! Ya puedes <a href="login.php">iniciar sesión</a>.</div>
    <?php else: ?>

        <form method="POST">
            <div style="display: flex; gap: 10px;">
                <div style="flex:1">
                    <label>Nombre</label>
                    <input type="text" name="nombre" required 
                           value="<?= htmlspecialchars($nombre) ?>">
                </div>
                <div style="flex:1">
                    <label>Apellido</label>
                    <input type="text" name="apellido" required 
                           value="<?= htmlspecialchars($apellido) ?>">
                </div>
            </div>

            <label>Email</label>
            <input type="email" name="email" required 
                   value="<?= htmlspecialchars($email) ?>">

            <label>Edad</label>
            <input type="number" name="edad" required 
                   value="<?= htmlspecialchars($edad) ?>">

            <label>Contraseña</label>
            <input type="password" name="password" required>
            
            <small style="display:block; margin-top:-10px; margin-bottom:15px; font-size:11px; color:#666;">
                Mínimo 8 caracteres, una mayúscula y un número.
            </small>

            <button type="submit">Registrarme</button>
        </form>
    <?php endif; ?>

    <a href="index.php" class="link">¿Ya tienes cuenta? Inicia sesión</a>
</div>

</body>
</html>
