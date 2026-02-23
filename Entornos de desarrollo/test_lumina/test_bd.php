<?php
use PHPUnit\Framework\TestCase;

require_once 'bd.php';

// Cambiamos el nombre de la clase a test_bd
class test_bd extends TestCase {
    public function testObtenerUsuarioPorCredencial() {
        $mockResult = $this->createMock(mysqli_result::class);
        $mockResult->method('fetch_assoc')->willReturn([
            'id' => 1,
            'nombre' => 'TestUser',
            'password' => 'hash_inventado',
            'rol' => 'user'
        ]);

        $mockStmt = $this->createMock(mysqli_stmt::class);
        $mockStmt->method('execute')->willReturn(true);
        $mockStmt->method('get_result')->willReturn($mockResult);

        $mockConexion = $this->createMock(mysqli::class);
        $mockConexion->method('prepare')->willReturn($mockStmt);

        $bd = new BaseDatos($mockConexion);
        $resultado = $bd->obtenerUsuarioPorCredencial("test@lumina.com");

        $this->assertEquals(1, $resultado['id']);
        $this->assertEquals('TestUser', $resultado['nombre']);
    }
}
?>
