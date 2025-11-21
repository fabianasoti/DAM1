-- ====================================================
-- Tienda de ovillos (MySQL 8+) - esquema, vistas y datos de ejemplo
-- ====================================================

-- 0) Crear base de datos y usarla
CREATE DATABASE IF NOT EXISTS tienda_ovillos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE tienda_ovillos;

-- 1) Limpieza (eliminar vistas y tablas si existen, en orden)
DROP VIEW IF EXISTS vw_customer_orders_summary;
DROP VIEW IF EXISTS vw_order_details;
DROP VIEW IF EXISTS vw_product_stock_status;
DROP VIEW IF EXISTS vw_products_with_category;
DROP VIEW IF EXISTS vw_order_line_items;

DROP TABLE IF EXISTS stock_movements;
DROP TABLE IF EXISTS order_lines;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS customers;

-- ============================
-- Tablas principales (InnoDB)
-- ============================

-- Categorías / Materiales
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Productos orientados a ovillos
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(150) NOT NULL,
    color VARCHAR(50),
    weight_grams INT NOT NULL, -- peso por ovillo en gramos
    length_meters INT, -- metros por ovillo (opcional)
    ply VARCHAR(30), -- grosor: "DK", "Worsted", etc.
    price DECIMAL(10,2) NOT NULL,
    category_id INT,
    active TINYINT(1) NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_products_category FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Clientes
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(80) NOT NULL,
    last_name VARCHAR(80) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    phone VARCHAR(30),
    address TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Pedidos (orders)
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending','paid','shipped','cancelled','completed') NOT NULL DEFAULT 'pending',
    shipping_address TEXT,
    total_amount DECIMAL(12,2) NOT NULL DEFAULT 0,
    notes TEXT,
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Líneas de pedido (order_lines)
CREATE TABLE order_lines (
    order_line_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    line_total DECIMAL(12,2) NOT NULL,
    CONSTRAINT fk_orderlines_order FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_orderlines_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Gestión de stock: estado actual por producto (puede ampliarse por almacén)
CREATE TABLE stock (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL UNIQUE,
    quantity_on_hand INT NOT NULL DEFAULT 0,
    reserved_quantity INT NOT NULL DEFAULT 0,
    last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_stock_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Movimientos de stock (histórico)
CREATE TABLE stock_movements (
    movement_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    movement_type ENUM('in','out','adjustment','reserve','release') NOT NULL,
    quantity INT NOT NULL, -- positivo para entradas, negativo para salidas/reservas
    reference VARCHAR(100),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    note TEXT,
    CONSTRAINT fk_stockmov_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Índices útiles
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_stock_product ON stock(product_id);
CREATE INDEX idx_stockmov_product ON stock_movements(product_id);

-- ============================
-- Triggers
-- ============================
-- Trigger para asegurar/normalizar line_total en order_lines (antes de insert y antes de update)
DROP TRIGGER IF EXISTS trg_order_lines_bi;
DELIMITER $$
CREATE TRIGGER trg_order_lines_bi
BEFORE INSERT ON order_lines
FOR EACH ROW
BEGIN
    -- if unit_price or quantity are null, set to 0 (defensivo)
    IF NEW.unit_price IS NULL THEN
        SET NEW.unit_price = 0;
    END IF;
    IF NEW.quantity IS NULL THEN
        SET NEW.quantity = 0;
    END IF;
    SET NEW.line_total = ROUND(NEW.quantity * NEW.unit_price, 2);
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS trg_order_lines_bu;
DELIMITER $$
CREATE TRIGGER trg_order_lines_bu
BEFORE UPDATE ON order_lines
FOR EACH ROW
BEGIN
    IF NEW.unit_price IS NULL THEN
        SET NEW.unit_price = 0;
    END IF;
    IF NEW.quantity IS NULL THEN
        SET NEW.quantity = 0;
    END IF;
    SET NEW.line_total = ROUND(NEW.quantity * NEW.unit_price, 2);
END$$
DELIMITER ;

-- ============================
-- Vistas para mostrar información con FK
-- ============================

CREATE VIEW vw_products_with_category AS
SELECT
    p.product_id,
    p.sku,
    p.name,
    p.color,
    p.weight_grams,
    p.length_meters,
    p.ply,
    p.price,
    p.active,
    c.category_id,
    c.name AS category_name,
    c.description AS category_description,
    IFNULL(s.quantity_on_hand, 0) AS quantity_on_hand,
    IFNULL(s.reserved_quantity, 0) AS reserved_quantity,
    p.created_at
FROM products p
LEFT JOIN categories c ON p.category_id = c.category_id
LEFT JOIN stock s ON p.product_id = s.product_id;

CREATE VIEW vw_product_stock_status AS
SELECT
    p.product_id,
    p.sku,
    p.name AS product_name,
    IFNULL(s.quantity_on_hand, 0) AS quantity_on_hand,
    IFNULL(s.reserved_quantity, 0) AS reserved_quantity,
    (IFNULL(s.quantity_on_hand, 0) - IFNULL(s.reserved_quantity, 0)) AS available_quantity,
    s.last_updated,
    (SELECT sm.created_at FROM stock_movements sm WHERE sm.product_id = p.product_id ORDER BY sm.created_at DESC LIMIT 1) AS last_movement_at
FROM products p
LEFT JOIN stock s ON p.product_id = s.product_id;

CREATE VIEW vw_order_details AS
SELECT
    o.order_id,
    o.order_date,
    o.status,
    o.total_amount AS order_total,
    o.shipping_address,
    o.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email AS customer_email,
    ol.order_line_id,
    ol.product_id,
    p.sku,
    p.name AS product_name,
    ol.quantity,
    ol.unit_price,
    ol.line_total
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN order_lines ol ON ol.order_id = o.order_id
LEFT JOIN products p ON ol.product_id = p.product_id;

CREATE VIEW vw_order_line_items AS
SELECT
    ol.order_line_id,
    ol.order_id,
    ol.product_id,
    p.sku,
    p.name AS product_name,
    ol.quantity,
    ol.unit_price,
    ol.line_total
FROM order_lines ol
JOIN products p ON ol.product_id = p.product_id;

CREATE VIEW vw_customer_orders_summary AS
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    COUNT(o.order_id) AS orders_count,
    IFNULL(SUM(o.total_amount),0) AS total_spent,
    MAX(o.order_date) AS last_order_date
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
ORDER BY total_spent DESC;

-- ============================
-- Datos de ejemplo (INSERTs) - orden: categories -> products -> customers -> stock -> orders -> order_lines -> stock_movements
-- ============================

-- 1) Categorías / materiales
INSERT INTO categories (name, description) VALUES
('Lana', 'Ovillos de lana natural, caliente y elástica.'),
('Algodón', 'Ovillos de algodón, buena para prendas de verano y amigurumis.'),
('Acrílico', 'Acrílico resistente y fácil de lavar.'),
('Seda', 'Mezclas con seda, brillo y suavidad.'),
('Mezcla', 'Combinaciones (lana/seda/algodón/acrílico).');

-- 2) Productos (ovillos)
INSERT INTO products (sku, name, color, weight_grams, length_meters, ply, price, category_id, active)
VALUES
('OVL-LA-001','Ovillo Lana Súper Soft - 100g','Crudo',100,200,'DK',6.50, (SELECT category_id FROM categories WHERE name='Lana' LIMIT 1), 1),
('OVL-LA-002','Ovillo Lana Rústica - 50g','Gris',50,110,'Worsted',4.20, (SELECT category_id FROM categories WHERE name='Lana' LIMIT 1), 1),
('OVL-ALG-001','Ovillo Algodón Premium - 50g','Blanco',50,160,'Sport',5.00, (SELECT category_id FROM categories WHERE name='Algodón' LIMIT 1), 1),
('OVL-ACR-001','Ovillo Acrílico Economy - 100g','Azul',100,220,'Worsted',3.80, (SELECT category_id FROM categories WHERE name='Acrílico' LIMIT 1), 1),
('OVL-SD-001','Ovillo Seda Mix - 25g','Champán',25,90,'Fingering',9.50, (SELECT category_id FROM categories WHERE name='Seda' LIMIT 1), 1),
('OVL-MX-001','Ovillo Mezcla Deluxe - 100g','Multicolor',100,210,'DK',8.75, (SELECT category_id FROM categories WHERE name='Mezcla' LIMIT 1), 1);

-- 3) Clientes
INSERT INTO customers (first_name, last_name, email, phone, address)
VALUES
('Susana','Santana','info@susana.com','+34 600 111 222','Calle de Susana, 12, 28001 Madrid'),
('Carlos','Ramírez','c.ramirez@example.com','+34 611 222 333','Avenida del Sol 123, 28002 Madrid'),
('Laura','Mendoza','laura.mz@example.com','+34 622 333 444','Calle Primavera 45, 28003 Madrid'),
('Javier','López','j.lopez@example.com','+34 633 444 555','Paseo de los Olivos 78, 28004 Madrid'),
('Isabel','Torres','isatorres@example.com','+34 644 555 666','Camino del Río 12, 28005 Madrid');

-- 4) Stock inicial (uno por producto)
INSERT INTO stock (product_id, quantity_on_hand, reserved_quantity)
VALUES
((SELECT product_id FROM products WHERE sku='OVL-LA-001' LIMIT 1), 50, 0),
((SELECT product_id FROM products WHERE sku='OVL-LA-002' LIMIT 1), 120, 0),
((SELECT product_id FROM products WHERE sku='OVL-ALG-001' LIMIT 1), 80, 0),
((SELECT product_id FROM products WHERE sku='OVL-ACR-001' LIMIT 1), 200, 0),
((SELECT product_id FROM products WHERE sku='OVL-SD-001' LIMIT 1), 30, 0),
((SELECT product_id FROM products WHERE sku='OVL-MX-001' LIMIT 1), 60, 0);

-- 5) Pedidos (orders) - total_amount = 0 temporalmente; lo actualizaremos después
INSERT INTO orders (customer_id, order_date, status, shipping_address, total_amount, notes)
VALUES
((SELECT customer_id FROM customers WHERE email='info@susana.com' LIMIT 1), NOW() - INTERVAL 7 DAY, 'completed', 'Calle de Susana, 12, 28001 Madrid', 0, 'Pedido de prueba 1'),
((SELECT customer_id FROM customers WHERE email='c.ramirez@example.com' LIMIT 1), NOW() - INTERVAL 2 DAY, 'paid', 'Avenida del Sol 123, 28002 Madrid', 0, 'Envío urgente'),
((SELECT customer_id FROM customers WHERE email='laura.mz@example.com' LIMIT 1), NOW() - INTERVAL 1 DAY, 'pending', 'Calle Primavera 45, 28003 Madrid', 0, 'Pago pendiente');

-- 6) Líneas de pedido (order_lines) - ROUND para line_total; el trigger también lo calculará si omites line_total
-- Pedido 1 (Susana)
INSERT INTO order_lines (order_id, product_id, quantity, unit_price, line_total)
VALUES
((SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='info@susana.com' LIMIT 1) LIMIT 1),
 (SELECT product_id FROM products WHERE sku='OVL-LA-001' LIMIT 1), 2, (SELECT price FROM products WHERE sku='OVL-LA-001' LIMIT 1), ROUND(2 * (SELECT price FROM products WHERE sku='OVL-LA-001' LIMIT 1),2)
),
((SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='info@susana.com' LIMIT 1) LIMIT 1),
 (SELECT product_id FROM products WHERE sku='OVL-ALG-001' LIMIT 1), 3, (SELECT price FROM products WHERE sku='OVL-ALG-001' LIMIT 1), ROUND(3 * (SELECT price FROM products WHERE sku='OVL-ALG-001' LIMIT 1),2)
);

-- Pedido 2 (Carlos)
INSERT INTO order_lines (order_id, product_id, quantity, unit_price, line_total)
VALUES
((SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='c.ramirez@example.com' LIMIT 1) LIMIT 1),
 (SELECT product_id FROM products WHERE sku='OVL-ACR-001' LIMIT 1), 10, (SELECT price FROM products WHERE sku='OVL-ACR-001' LIMIT 1), ROUND(10 * (SELECT price FROM products WHERE sku='OVL-ACR-001' LIMIT 1),2)
),
((SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='c.ramirez@example.com' LIMIT 1) LIMIT 1),
 (SELECT product_id FROM products WHERE sku='OVL-MX-001' LIMIT 1), 1, (SELECT price FROM products WHERE sku='OVL-MX-001' LIMIT 1), ROUND(1 * (SELECT price FROM products WHERE sku='OVL-MX-001' LIMIT 1),2)
);

-- Pedido 3 (Laura) - pendiente
INSERT INTO order_lines (order_id, product_id, quantity, unit_price, line_total)
VALUES
((SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='laura.mz@example.com' LIMIT 1) LIMIT 1),
 (SELECT product_id FROM products WHERE sku='OVL-SD-001' LIMIT 1), 2, (SELECT price FROM products WHERE sku='OVL-SD-001' LIMIT 1), ROUND(2 * (SELECT price FROM products WHERE sku='OVL-SD-001' LIMIT 1),2)
);

-- 7) Actualizar total_amount en orders basándose en order_lines
UPDATE orders o
JOIN (
    SELECT order_id, SUM(line_total) AS total
    FROM order_lines
    GROUP BY order_id
) sub ON o.order_id = sub.order_id
SET o.total_amount = sub.total;

-- 8) Movimientos de stock (histórico) - reflejando salidas por los pedidos anteriores
INSERT INTO stock_movements (product_id, movement_type, quantity, reference, note)
VALUES
((SELECT product_id FROM products WHERE sku='OVL-LA-001' LIMIT 1), 'out', -2, CONCAT('order:', (SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='info@susana.com' LIMIT 1) LIMIT 1)), 'Salida por pedido completado Susana'),
((SELECT product_id FROM products WHERE sku='OVL-ALG-001' LIMIT 1), 'out', -3, CONCAT('order:', (SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='info@susana.com' LIMIT 1) LIMIT 1)), 'Salida por pedido completado Susana'),
((SELECT product_id FROM products WHERE sku='OVL-ACR-001' LIMIT 1), 'out', -10, CONCAT('order:', (SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='c.ramirez@example.com' LIMIT 1) LIMIT 1)), 'Salida por pedido Carlos'),
((SELECT product_id FROM products WHERE sku='OVL-MX-001' LIMIT 1), 'out', -1, CONCAT('order:', (SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='c.ramirez@example.com' LIMIT 1) LIMIT 1)), 'Salida por pedido Carlos'),
((SELECT product_id FROM products WHERE sku='OVL-SD-001' LIMIT 1), 'reserve', -2, CONCAT('order:', (SELECT order_id FROM orders WHERE customer_id=(SELECT customer_id FROM customers WHERE email='laura.mz@example.com' LIMIT 1) LIMIT 1)), 'Reserva por pedido pendiente Laura');

-- 9) Ajustar tabla stock según movimientos anteriores (ejecución explícita)
-- Resta para OVL-LA-001: -2
UPDATE stock SET quantity_on_hand = GREATEST(quantity_on_hand - 2, 0), last_updated = NOW()
WHERE product_id = (SELECT product_id FROM products WHERE sku='OVL-LA-001' LIMIT 1);

-- Resta para OVL-ALG-001: -3
UPDATE stock SET quantity_on_hand = GREATEST(quantity_on_hand - 3, 0), last_updated = NOW()
WHERE product_id = (SELECT product_id FROM products WHERE sku='OVL-ALG-001' LIMIT 1);

-- Resta para OVL-ACR-001: -10
UPDATE stock SET quantity_on_hand = GREATEST(quantity_on_hand - 10, 0), last_updated = NOW()
WHERE product_id = (SELECT product_id FROM products WHERE sku='OVL-ACR-001' LIMIT 1);

-- Resta para OVL-MX-001: -1
UPDATE stock SET quantity_on_hand = GREATEST(quantity_on_hand - 1, 0), last_updated = NOW()
WHERE product_id = (SELECT product_id FROM products WHERE sku='OVL-MX-001' LIMIT 1);

-- Reserva para OVL-SD-001: reserved_quantity +2
UPDATE stock SET reserved_quantity = reserved_quantity + 2, last_updated = NOW()
WHERE product_id = (SELECT product_id FROM products WHERE sku='OVL-SD-001' LIMIT 1);

-- ============================
-- Consultas de ejemplo con las vistas (opcional)
-- ============================
-- SELECT * FROM vw_products_with_category;
-- SELECT * FROM vw_product_stock_status;
-- SELECT * FROM vw_order_details WHERE order_id = 1;
-- SELECT * FROM vw_customer_orders_summary;

-- Fin del bloque SQL.

