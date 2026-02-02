sudo mysql -u root -p
CREATE DATABASE microtienda;
USE microtienda;

CREATE TABLE productos(
	nombre VARCHAR(255),
  descripcion TEXT,
  precio INT(255)
);

INSERT INTO productos VALUES(
  'Zapatillas',
  'Zapatillas chulas de deporte',
  30
);

INSERT INTO productos VALUES
('Sudadera', 'Sudadera cómoda de algodón', 35),
('Gorra', 'Gorra ajustable estilo urbano', 15),
('Chaqueta', 'Chaqueta ligera resistente al viento', 55),
('Calcetines', 'Calcetines deportivos transpirables', 5),
('Mochila', 'Mochila espaciosa para uso diario', 40),
('Reloj deportivo', 'Reloj digital resistente al agua', 60),
('Gafas de sol', 'Gafas con protección UV400', 25),
('Cinturón', 'Cinturón de piel sintética ajustable', 18),
('Botella térmica', 'Botella aislada de acero inoxidable', 22),
('Guantes', 'Guantes táctiles para invierno', 12);

SELECT * FROM productos;
+------------------+----------------------------------------+--------+
| nombre           | descripcion                            | precio |
+------------------+----------------------------------------+--------+
| Zapatillas       | Zapatillas chulas de deporte           |     30 |
| Sudadera         | Sudadera cómoda de algodón             |     35 |
| Gorra            | Gorra ajustable estilo urbano          |     15 |
| Chaqueta         | Chaqueta ligera resistente al viento   |     55 |
| Calcetines       | Calcetines deportivos transpirables    |      5 |
| Mochila          | Mochila espaciosa para uso diario      |     40 |
| Reloj deportivo  | Reloj digital resistente al agua       |     60 |
| Gafas de sol     | Gafas con protección UV400             |     25 |
| Cinturón         | Cinturón de piel sintética ajustable   |     18 |
| Botella térmica  | Botella aislada de acero inoxidable    |     22 |
| Guantes          | Guantes táctiles para invierno         |     12 |
+------------------+----------------------------------------+--------+

