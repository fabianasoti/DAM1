<?php
class Validador {
    // Valida que los campos no estén vacíos (basado en tu login.php)
    public function validarCamposLlenos($credencial, $pass) {
        $credencialLimpia = trim($credencial);
        if (empty($credencialLimpia) || empty($pass)) {
            return false;
        }
        return true;
    }

    // He añadido esta validación extra (basada en tu registro) 
    // para que tengas algo más interesante que testear en caja blanca
    public function validarLongitudPassword($pass) {
        return strlen($pass) >= 8;
    }
}
?>
