INSERT INTO producto VALUES
(1,  'Ovillo algodón 100g',          'Ovillo de algodón 100% peinado, ideal para amigurumi',          '4.50',  '120', 'ovillo_algodon.jpg'),
(2,  'Ovillo lana merino 50g',       'Lana merino suave para prendas de invierno',                    '6.90',  '80',  'ovillo_merino.jpg'),
(3,  'Ovillo acrílico 100g',         'Ovillo económico para proyectos básicos',                       '2.99',  '150', 'ovillo_acrilico.jpg'),
(4,  'Pack 10 ovillos algodón',      'Paquete surtido de 10 ovillos de algodón',                      '39.90', '40',  'pack_algodon.jpg'),
(5,  'Pack lana premium',            'Pack de lanas premium de colores variados',                     '49.90', '30',  'pack_premium.jpg'),
(6,  'Aguja de crochet 3.5mm',       'Aguja de aluminio ligera para crochet',                          '3.50',  '200', 'crochet35.jpg'),
(7,  'Aguja de crochet 5mm',         'Aguja ergonómica de 5mm',                                       '4.80',  '180', 'crochet5.jpg'),
(8,  'Agujas circulares 80cm',       'Agujas circulares de 4mm con cable de 80cm',                    '8.90',  '90',  'circulares80.jpg'),
(9,  'Agujas rectas 30cm',           'Agujas de tejer rectas de 5mm',                                 '6.50',  '110', 'rectas30.jpg'),
(10, 'Kit iniciación crochet',       'Kit básico con agujas, marcadores y tijeras',                   '19.90', '60',  'kit_crochet.jpg'),
(11, 'Kit amigurumi',                'Kit completo para realizar un amigurumi paso a paso',            '24.90', '45',  'kit_amigurumi.jpg'),
(12, 'Marcadores de puntos',         'Set de 20 marcadores de plástico',                              '2.50',  '220', 'marcadores.jpg'),
(13, 'Tijeras artesanales',          'Tijeras pequeñas de acero inoxidable para manualidades',        '5.99',  '70',  'tijeras.jpg'),
(14, 'Cinta métrica 150cm',          'Cinta métrica enrollable ideal para costura y tejido',          '1.99',  '150', 'cinta_metrica.jpg'),
(15, 'Bolsa organizadora',           'Bolsa de almacenamiento para lanas y accesorios',               '14.90', '50',  'bolsa_org.jpg'),
(16, 'Ovillo hilo macramé 200g',     'Hilo grueso especial para macramé',                             '7.90',  '90',  'macrame200.jpg'),
(17, 'Tela Aida punto de cruz',      'Tela para bordado punto de cruz 45x45 cm',                      '3.99',  '100', 'tela_aida.jpg'),
(18, 'Kit punto de cruz',            'Kit completo con patrón, hilos y aguja',                        '17.90', '30',  'kit_px.jpg'),
(19, 'Pegamento textil',             'Adhesivo especial para telas y manualidades',                   '4.20',  '85',  'pegamento_textil.jpg'),
(20, 'Luz LED para tejer',           'Lámpara LED portátil para tejer de noche',                      '12.90', '40',  'luz_led.jpg');

INSERT INTO cliente VALUES
(1,  'Ana',     'Martínez López',   'ana.martinez@email.com',     'C/ Mayor 12, Madrid',          '600123456'),
(2,  'Carlos',  'Pérez Gómez',      'carlos.perez@email.com',    'Av. Libertad 45, Valencia',    '611234567'),
(3,  'Laura',   'Sánchez Ruiz',     'laura.sanchez@email.com',   'C/ del Mar 8, Alicante',       '622345678'),
(4,  'Javier',  'López Torres',     'javier.lopez@email.com',    'Gran Vía 101, Madrid',         '633456789'),
(5,  'Marta',   'Gómez Fernández',  'marta.gomez@email.com',     'C/ Colón 3, Castellón',        '644567890'),
(6,  'David',   'Ruiz Molina',      'david.ruiz@email.com',      'Av. Europa 22, Murcia',        '655678901'),
(7,  'Lucía',   'Navarro Pérez',    'lucia.navarro@email.com',   'C/ Serranos 7, Valencia',      '666789012'),
(8,  'Pablo',   'Hernández Gil',    'pablo.hernandez@email.com', 'C/ San Juan 19, Elche',        '677890123'),
(9,  'Sonia',   'Romero Díaz',      'sonia.romero@email.com',    'Av. Mediterráneo 5, Benidorm', '688901234'),
(10, 'Alberto', 'Morales Cano',     'alberto.morales@email.com', 'C/ Alameda 14, Albacete',      '699012345');

INSERT INTO pedido VALUES
(1,  '2025-12-01 10:15:00', 1),
(2,  '2025-12-01 18:40:00', 2),
(3,  '2025-12-02 09:05:00', 1),
(4,  '2025-12-02 21:30:00', 3),
(5,  '2025-12-03 11:00:00', 4),
(6,  '2025-12-03 16:20:00', 5),
(7,  '2025-12-04 12:10:00', 6),
(8,  '2025-12-04 19:45:00', 7),
(9,  '2025-12-05 08:50:00', 8),
(10, '2025-12-05 14:35:00', 9),
(11, '2025-12-06 10:05:00', 10),
(12, '2025-12-06 17:25:00', 2),
(13, '2025-12-07 09:40:00', 3),
(14, '2025-12-07 20:10:00', 6),
(15, '2025-12-08 13:55:00', 1);

INSERT INTO lineaspedido VALUES
(1,  1,  '2',  1),   -- 2 ovillos algodón
(2,  1,  '1',  6),   -- aguja crochet 3.5
(3,  2,  '1', 10),   -- kit crochet
(4,  2,  '3',  3),   -- 3 ovillos acrílico
(5,  3,  '2',  2),   -- lana merino
(6,  3,  '1', 12),   -- marcadores
(7,  4,  '1', 18),   -- kit punto de cruz
(8,  4,  '2',  9),   -- agujas rectas
(9,  5,  '1',  4),   -- pack algodón
(10, 5,  '1',  7),   -- aguja crochet 5mm
(11, 6,  '1', 20),   -- luz LED
(12, 6,  '1',  5),   -- pack premium
(13, 7,  '2', 16),   -- hilo macramé
(14, 7,  '1', 11),   -- kit amigurumi
(15, 8,  '1', 14),   -- cinta métrica
(16, 8,  '3',  3),   -- ovillo acrílico
(17, 9,  '1', 15),   -- bolsa organizadora
(18, 9,  '1', 19),   -- pegamento textil
(19, 10, '2',  1),   -- 2 ovillos algodón
(20, 10, '2',  2),   -- 2 ovillos merino
(21, 11, '1',  8),   -- agujas circulares
(22, 11, '1', 12),   -- marcadores
(23, 12, '2', 17),   -- tela Aida
(24, 12, '1', 13),   -- tijeras
(25, 13, '1',  4),   -- pack algodón
(26, 13, '1', 10),   -- kit crochet
(27, 14, '1', 18),   -- kit punto de cruz
(28, 14, '2',  1),   -- 2 ovillos algodón
(29, 15, '1',  2),   -- merino
(30, 15, '1',  7);   -- aguja crochet 5mm

