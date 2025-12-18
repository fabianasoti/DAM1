CREATE DATABASE diarioemocional;
USE diarioemocional;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    edad INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    password VARCHAR(255) NOT NULL,
    CONSTRAINT chk_password_segura CHECK (
        CHAR_LENGTH(password) >= 8
        AND password REGEXP '[A-Za-z]'
        AND password REGEXP '[0-9]'
        AND password REGEXP '[^A-Za-z0-9]'
    )
);

CREATE USER 
'diarioemocional'@'localhost' 
IDENTIFIED  BY 'Diarioemocional123$';

GRANT USAGE ON *.* TO 'diarioemocional'@'localhost';

ALTER USER 'diarioemocional'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON diarioemocional.* 
TO 'diarioemocional'@'localhost';

FLUSH PRIVILEGES;

ALTER TABLE usuarios ADD CONSTRAINT chk_password_segura CHECK (
        CHAR_LENGTH(password) >= 8
        AND password REGEXP '[A-Za-z]'
        AND password REGEXP '[0-9]'
        AND password REGEXP '[^A-Za-z0-9]'
    );
    

INSERT INTO usuarios (nombre, apellido, email, edad, password) VALUES
('Ana', 'Martínez', 'ana.martinez@email.com', 25, 'Ana1234!'),
('Carlos', 'Gómez', 'carlos.gomez@email.com', 32, 'Carlo$89'),
('Lucía', 'Fernández', 'lucia.fernandez@email.com', 28, 'Lucia#45'),
('Miguel', 'Rodríguez', 'miguel.rodriguez@email.com', 40, 'Miguel@12'),
('Sofía', 'López', 'sofia.lopez@email.com', 22, 'Sofia*78'),
('Javier', 'Pérez', 'javier.perez@email.com', 35, 'Javi123!'),
('María', 'Sánchez', 'maria.sanchez@email.com', 30, 'Maria%90'),
('Daniel', 'Torres', 'daniel.torres@email.com', 27, 'Dani&456'),
('Elena', 'Ruiz', 'elena.ruiz@email.com', 34, 'Elena_33'),
('Pablo', 'Navarro', 'pablo.navarro@email.com', 29, 'Pablo+88');


INSERT INTO usuarios (nombre, apellido, email, edad, password) VALUES('Susana', 'Santana', 'info@susana.com', 23, 'Susana123$');

