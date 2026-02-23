<?php
class BaseDatos {
    private $conexion;

    public function __construct($conexion) {
        $this->conexion = $conexion;
    }

    // Busca al usuario por email o nombre
    public function obtenerUsuarioPorCredencial($credencial) {
        $sql = "SELECT id, nombre, password, rol FROM usuarios WHERE email = ? OR nombre = ? LIMIT 1";
        $stmt = $this->conexion->prepare($sql);
        
        if (!$stmt) {
            return false; // Error en la consulta
        }

        $stmt->bind_param("ss", $credencial, $credencial);
        $stmt->execute();
        $res = $stmt->get_result();

        if ($fila = $res->fetch_assoc()) {
            return $fila; // Devuelve los datos si existe
        }
        
        return null; // No se encontró el usuario
    }
}
?>
