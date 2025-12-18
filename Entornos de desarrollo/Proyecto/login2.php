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
* LÓGICA LOGIN
****************************/
$errores = [];
$email = "";
$password = "";
 
if ($_SERVER["REQUEST_METHOD"] === "POST") {
 
    $email = trim($_POST["email"]);
    $password = trim($_POST["password"]);
 
    // EMAIL
    if (empty($email)) {
        $errores[] = "El email es obligatorio.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errores[] = "Formato de email inválido.";
    }
 
    // PASSWORD
    if (empty($password)) {
        $errores[] = "La contraseña es obligatoria.";
    } elseif (
        strlen($password) < 8 ||
        !preg_match('/[A-Z]/', $password) ||
        !preg_match('/[a-z]/', $password) ||
        !preg_match('/[0-9]/', $password) ||
        !preg_match('/[\W]/', $password)
    ) {
        $errores[] = "Mínimo 8 caracteres, mayúscula, minúscula, número y símbolo.";
    }
 
    // VALIDACIÓN BD
    if (empty($errores)) {
        $stmt = $conexion->prepare(
            "SELECT password FROM usuarios WHERE email = ?"
        );
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt->store_result();
 
        if ($stmt->num_rows === 1) {
            $stmt->bind_result($hash);
            $stmt->fetch();
 
            if (password_verify($password, $hash)) {
                $mensaje_exito = "Bienvenido/a 💜 Este es tu espacio seguro.";
            } else {
                $errores[] = "Credenciales incorrectas.";
            }
        } else {
            $errores[] = "Usuario no encontrado.";
        }
    }
}
?>
 
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Login emocional</title>
 
<style>
*{
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}
 
body{
    margin:0;
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#cdb4db,#bde0fe);
}
 
.login-container{
    background:#fff;
    width:100%;
    max-width:400px;
    padding:32px;
    border-radius:20px;
    box-shadow:0 18px 35px rgba(0,0,0,.15);
    animation:fade 1s ease;
}
 
@keyframes fade{
    from{opacity:0; transform:translateY(25px);}
    to{opacity:1; transform:translateY(0);}
}
 
.logo{
    text-align:center;
    font-size:44px;
    margin-bottom:10px;
}
 
h2{
    text-align:center;
    color:#4a4e69;
    margin:0;
}
 
.sub{
    text-align:center;
    color:#6d597a;
    font-size:14px;
    margin-bottom:25px;
}
 
label{
    font-size:14px;
    color:#4a4e69;
}
 
input{
    width:100%;
    padding:12px;
    border-radius:12px;
    border:1px solid #cdb4db;
    margin-top:6px;
    margin-bottom:18px;
}
 
input:focus{
    outline:none;
    border-color:#9d4edd;
    box-shadow:0 0 0 3px rgba(157,78,221,.25);
}
 
.password-wrapper{
    position:relative;
}
 
.toggle-password{
    position:absolute;
    right:14px;
    top:50%;
    transform:translateY(-50%);
    cursor:pointer;
}
 
button{
    width:100%;
    padding:12px;
    border:none;
    border-radius:14px;
    background:linear-gradient(135deg,#9d4edd,#5fa8d3);
    color:#fff;
    font-size:16px;
    font-weight:bold;
    cursor:pointer;
    transition:.3s;
}
 
button:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,.2);
}
 
.feedback{
    text-align:center;
    font-size:14px;
    color:#6d597a;
    display:none;
    margin-bottom:15px;
}
 
.errores{
    background:#fde2e4;
    border-left:5px solid #ff6b6b;
    padding:10px;
    border-radius:8px;
    margin-bottom:15px;
    font-size:14px;
}
 
.exito{
    background:#e0fbfc;
    border-left:5px solid #5fa8d3;
    padding:10px;
    border-radius:8px;
    margin-bottom:15px;
    font-size:14px;
}
</style>
</head>
<body>
 
<div class="login-container">
 
    <div class="logo">🧠</div>
<h2>Bienvenido/a</h2>
<p class="sub">Cuida tu bienestar emocional</p>
 
    <div class="feedback" id="feedback">
        Respira… estamos validando 🌿
</div>
 
    <?php if (!empty($errores)): ?>
<div class="errores">
<ul>
<?php foreach ($errores as $e): ?>
<li><?= $e ?></li>
<?php endforeach; ?>
</ul>
</div>
<?php endif; ?>
 
    <?php if (!empty($mensaje_exito)): ?>
<div class="exito"><?= $mensaje_exito ?></div>
<?php endif; ?>
 
    <form method="POST" onsubmit="mostrarFeedback()">
<label>Email</label>
<input type="email" name="email"
               value="<?= htmlspecialchars($email) ?>">
 
        <label>Contraseña</label>
<div class="password-wrapper">
<input type="password" id="password" name="password">
<span class="toggle-password" onclick="togglePassword()">👁️</span>
</div>
 
        <button type="submit">Iniciar sesión</button>
</form>
 
</div>
 
<script>
function togglePassword(){
    const p = document.getElementById("password");
    p.type = p.type === "password" ? "text" : "password";
}
function mostrarFeedback(){
    document.getElementById("feedback").style.display = "block";
}
</script>
 
</body>
</html>
