-- Crear base de datos
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;

-- Tabla clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);

-- Tabla productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Datos de prueba: clientes
INSERT INTO clientes (nombre, email, telefono)
VALUES
    ('Susana Santana', 'susana@ejemplo.com', '600123456'),
    ('Benito Bonito', 'benito@ejemplo.com', '611987654'),
    ('Elga Tito', 'elga@ejemplo.com', '622111222');

-- Datos de prueba: productos
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES 
('Ovillo Merino', 'Lana 100% merino suave 100g', 12.50, 45),
('Ganchillo 4mm', 'Aguja ergonómica mango silicona', 5.99, 30),
('Algodón Pima', 'Hilo algodón alta calidad crudo', 8.20, 60),
('Palillos Bambú', 'Agujas de madera 6mm ligeras', 7.50, 20),
('Marcadores', 'Set 50 marcadores tipo candado', 4.50, 100),
('Lana Alpaca', 'Mezcla alpaca y seda gris', 15.90, 15),
('Agujas Circulares', 'Metal 80cm de largo, 5mm grosor', 9.00, 25),
('Tijeras Cigüeña', 'Tijeras bordado diseño vintage', 11.50, 18),
('Cinta Métrica', 'Cinta retráctil de 150cm', 3.00, 75),
('Trapillo Bobina', 'Tela reciclada para cestas 800g', 14.00, 12);
