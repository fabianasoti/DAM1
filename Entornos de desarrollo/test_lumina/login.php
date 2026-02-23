<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Iniciar Sesión - Lumina</title>
</head>
<body>
    <div class="login-container">
        <h1>Lumina - Login</h1>
        <form action="procesar.php" method="POST">
            <input type="text" name="credencial" placeholder="Correo o Usuario" required>
            <input type="password" name="password" id="passInput" placeholder="Contraseña" required>
            <button type="submit">Entrar</button>
        </form>
    </div>
</body>
</html>
