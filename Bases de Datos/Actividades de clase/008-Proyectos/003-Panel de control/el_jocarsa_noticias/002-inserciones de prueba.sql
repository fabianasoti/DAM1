INSERT INTO autores (nombre, email) VALUES
('Ana Martínez', 'ana.mtz@periodico.com'),
('Carlos Ruiz', 'c.ruiz@prensa.es'),
('Elena Galdós', 'elena_g@redaccion.net'),
('Marcos Solo', 'm.solo@freelance.com');

INSERT INTO usuarios (nombre, email, password) VALUES
('Juan Pérez', 'juanito99@gmail.com', '123456'),
('Marta Gómez', 'marta.gomez@yahoo.es', 'marta_2024'),
('Roberto Soler', 'rsoler@outlook.com', 'admin789'),
('Lucía Fernández', 'lucia.fer@gmail.com', 'password123');

INSERT INTO noticias (titulo, contenido, fecha_publicacion, id_autor) VALUES
('Nueva tecnología en IA', 'Hoy se ha presentado una nueva inteligencia artificial que promete...', '2024-01-15', 1),
('Descubrimiento en Marte', 'La sonda espacial ha encontrado restos de minerales que indican...', '2024-02-10', 2),
('El precio del pan sube', 'Debido a la escasez de trigo, las panaderías locales han anunciado...', '2024-02-12', 1),
('Final de la Champions', 'El partido de ayer dejó momentos inolvidables para la historia del...', '2024-05-20', 3),
('Consejos de Ciberseguridad', 'Para mantener tus cuentas a salvo, es vital utilizar contraseñas...', '2024-06-01', 4);
