<?php
function validarEntradas($credencial, $pass) {
    $credencial = trim($credencial); [cite: 307]
    
    // Validación de campos vacíos
    if (empty($nombre) || empty($email) || empty($pass)) {
        header("Location: login.php?error=vacios");
        exit();
    }

    // Validar requisitos de contraseña (Regex)
    $patron = '/^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/';
    if (!preg_match($patron, $pass)) {
        header("Location: login.php?error=password_debil");
        exit();
    }
?>
