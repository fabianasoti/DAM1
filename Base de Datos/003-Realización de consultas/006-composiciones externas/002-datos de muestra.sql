INSERT INTO alumnos (Identificador, nombre, apellidos) VALUES
(1, 'Lucía', 'Martínez Gómez'),
(2, 'Carlos', 'Ruiz Fernández'),
(3, 'María', 'López Sánchez'),
(4, 'Javier', 'Torres Delgado'),
(5, 'Ana', 'Hernández Pérez'),
(6, 'Diego', 'Castro Aguilar'),
(7, 'Elena', 'Mendoza López'),
(8, 'Sofía', 'Ramírez Cortés'),
(9, 'Pablo', 'Serrano Núñez'),
(10, 'Valeria', 'González Márquez');


INSERT INTO profesores (Identificador, nombre, apellidos) VALUES
(1, 'Rosa', 'Vega Morales'),
(2, 'Miguel', 'Durán Castillo'),
(3, 'Laura', 'Navarro Jiménez'),
(4, 'Héctor', 'Santos Paredes'),
(5, 'Patricia', 'Luna Cabrera');

INSERT INTO asignaturas (Identificador, nombre, id_profesor) VALUES
(1, 'Composición Musical I', 1),
(2, 'Armonía Moderna', 1),
(3, 'Historia de la Música', 3),
(4, 'Instrumentación y Orquestación', 4),
(5, 'Producción Digital', 2),
(6, 'Análisis Musical Avanzado', 3),
(7, 'Improvisación', 5),
(8, 'Composición Contemporánea', 4);

INSERT INTO matriculas (Identificador, id_asignatura, id_alumno) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 4),
(5, 2, 5),
(6, 3, 6),
(7, 3, 1),
(8, 4, 7),
(9, 4, 2),
(10, 5, 8),
(11, 6, 9),
(12, 6, 10),
(13, 7, 3),
(14, 7, 4),
(15, 8, 5),
(16, 8, 6),
(17, 5, 7),
(18, 2, 8),
(19, 3, 9),
(20, 4, 10);
