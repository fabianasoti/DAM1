<?php
function validarEntradas($credencial, $pass) {
    $credencial = trim($credencial); [cite: 307]
    
    // Validación de campos vacíos
    if (empty($credencial) || empty($pass)) { [cite: 309]
        return "vacios";
    }
    
    // Validación de longitud (Sugerencia del profe)
    if (strlen($pass) < 6) {
        return "longitud_corta";
    }
    
    return "ok";
}
?>
