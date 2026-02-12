CREATE DATABASE diarioemocional;
USE diarioemocional;

CREATE USER 
'if0_41114218'@'sql311.infinityfree.com"' 
IDENTIFIED  BY 'UT1NtmXinHsa';

GRANT USAGE ON *.* TO 'if0_41114218'@'sql311.infinityfree.com';

ALTER USER 'if0_41114218'@'sql311.infinityfree.com' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON diarioemocional.* 
TO 'if0_41114218'@'sql311.infinityfree.com';

FLUSH PRIVILEGES;


CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol VARCHAR(20) DEFAULT 'user',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    token_reset VARCHAR(64) NULL DEFAULT NULL,
    token_expira DATETIME NULL DEFAULT NULL,
    ultima_conexion DATETIME NULL DEFAULT NULL,
    ultimo_cambio_nombre DATETIME NULL DEFAULT NULL
);

CREATE TABLE entradas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    emocion VARCHAR(50),
    intensidad INT DEFAULT 5,
    nota TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

/* 3. ¡IMPORTANTE! Conviértete TÚ en el administrador */
/* Cambia 'tu_email@ejemplo.com' por TU email real con el que te registraste */
UPDATE usuarios SET rol = 'admin' WHERE email = 'tu-nombre@ejemplo.com';


