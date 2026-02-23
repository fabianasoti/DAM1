<?php
use PHPUnit\Framework\TestCase;

require_once 'validador.php';

// Cambiamos el nombre de la clase para que coincida EXACTAMENTE con el archivo
class test_validador extends TestCase {
    private $validador;

    protected function setUp(): void {
        $this->validador = new Validador();
    }

    public function testValidarCamposLlenosFallaConVacios() {
        $this->assertFalse($this->validador->validarCamposLlenos("", ""));
        $this->assertFalse($this->validador->validarCamposLlenos("usuario", ""));
    }

    public function testValidarCamposLlenosExitoso() {
        $this->assertTrue($this->validador->validarCamposLlenos("admin@lumina.com", "12345678"));
    }

    public function testValidarLongitudPassword() {
        $this->assertFalse($this->validador->validarLongitudPassword("corta"));
        $this->assertTrue($this->validador->validarLongitudPassword("passwordFuerte123"));
    }
}
?>
