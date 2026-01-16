En este ejercicio se trabaja el diseño y creación de una base de datos relacional orientada a una tienda online de patos de goma, utilizando SQL para definir tablas, claves primarias y foráneas, así como vistas que facilitan la consulta de información relacionada. Además, se implementa una aplicación web sencilla con Flask para visualizar los datos mediante páginas HTML. El objetivo es comprender cómo se estructuran los datos de un sistema de venta, cómo se relacionan entre sí y cómo pueden ser utilizados desde una aplicación web.

---
El proyecto se divide en dos grandes bloques: la base de datos y la aplicación web.

1. Diseño de la Base de Datos

Se ha diseñado una base de datos relacional compuesta por varias tablas que representan los elementos principales de una tienda online:
- Categorías de patos
- Clientes
- Productos
- Pedidos
- Líneas de pedido
- Stock actual
- Movimientos de stock

Cada tabla dispone de su clave primaria (PK) y las relaciones se establecen mediante claves foráneas (FK), garantizando la integridad referencial.

2. Creación de Vistas

Las vistas permiten consultar información relacionada entre varias tablas sin necesidad de escribir consultas complejas. Se han creado, entre otras:
- vw_productos_pato: productos con su categoría y stock disponible
- vw_pedidos_con_clientes: pedidos con datos del cliente
- vw_lineas_pedido_detalle: detalle completo de cada pedido
- vw_movimientos_stock_detalle: movimientos de stock por producto

Estas vistas facilitan la visualización de los datos en la aplicación web.

3. Inserción de Datos de Ejemplo

Los datos se insertan respetando el orden lógico de dependencias:
	1- Categorías
	2- Clientes
	3- Productos
	4- Pedidos
	5- Stock
	6- Líneas de pedido
	7- Movimientos de stock

Esto permite evitar errores de claves foráneas y asegurar la coherencia de los datos.

4. Desarrollo de la Aplicación Web

Se ha creado una aplicación web sencilla con Flask que incluye tres páginas:
- Inicio
- Sobre mí
- Contacto

Desde la página de inicio se puede mostrar un listado de productos utilizando la vista vw_productos_pato.

---
A continuación se muestra el contenido de la estructura y código o scripts que conforman este ejercicio:

#### 002-multipagina.py:
```
''' 
Aplicación web multipágina con Flask
2025 Fabiana Victoria Sotillo
Programa que crea una aplicación web sencilla para la tienda de patos de goma,
mostrando páginas de inicio, sobre mí y contacto mediante plantillas HTML.
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/sobremi")
def sobremi():
    return render_template("sobremi.html")
	
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")
	
if __name__ == "__main__":
    app.run(debug=True)
```

#### Estructura del proyecto
```
tienda_patos/
│
├── 002-multipagina.py
├── templates/
│   ├── inicio.html
│   ├── sobremi.html
│   └── contacto.html
└── base_datos.sql
```

#### Base de datos: Script de instalación

Se utiliza el prompt del archivo 009-prompt_chatgpt.md:
- Creación de tablas con PK y FK
- Creación de vistas
- Inserción de datos de ejemplo
- Control de integridad referencial

Luego chatgpt crea este script de sql el cual permite instalar toda la base de datos en una sola ejecución.
```
-- =========================================================
-- Script de instalación: Tienda de patos de goma
-- Esquema orientado a MySQL/MariaDB (InnoDB, utf8mb4)
-- Incluye tablas, claves PK/FK, vistas e inserts de ejemplo
-- =========================================================

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- (Opcional) Borrado previo de tablas si existen
-- DROP TABLE IF EXISTS movimientos_stock;
-- DROP TABLE IF EXISTS lineas_pedido;
-- DROP TABLE IF EXISTS stock_actual;
-- DROP TABLE IF EXISTS pedidos;
-- DROP TABLE IF EXISTS productos_pato;
-- DROP TABLE IF EXISTS clientes;
-- DROP TABLE IF EXISTS categorias_pato;

SET FOREIGN_KEY_CHECKS = 1;

-- ==========================
-- TABLAS MAESTRAS
-- ==========================

-- Categorías de patos
CREATE TABLE categorias_pato (
    id_categoria    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    descripcion     VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Clientes
CREATE TABLE clientes (
    id_cliente      INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    apellidos       VARCHAR(150) NOT NULL,
    email           VARCHAR(150) NOT NULL UNIQUE,
    telefono        VARCHAR(30),
    direccion       VARCHAR(200),
    ciudad          VARCHAR(100),
    codigo_postal   VARCHAR(10),
    pais            VARCHAR(100),
    fecha_alta      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Productos (patos de goma)
CREATE TABLE productos_pato (
    id_producto     INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre          VARCHAR(150) NOT NULL,
    descripcion     TEXT,
    color           VARCHAR(50),
    tamano          VARCHAR(50),
    precio          DECIMAL(10,2) NOT NULL,
    activo          TINYINT(1) NOT NULL DEFAULT 1,
    id_categoria    INT UNSIGNED NOT NULL,
    CONSTRAINT fk_productos_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categorias_pato(id_categoria)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Pedidos (cabecera)
CREATE TABLE pedidos (
    id_pedido       INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_cliente      INT UNSIGNED NOT NULL,
    fecha_pedido    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    estado          VARCHAR(20) NOT NULL, -- p.ej.: PENDIENTE, PAGADO, ENVIADO, CANCELADO
    total           DECIMAL(10,2) NOT NULL DEFAULT 0,
    CONSTRAINT fk_pedidos_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Stock actual por producto
CREATE TABLE stock_actual (
    id_stock        INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_producto     INT UNSIGNED NOT NULL,
    cantidad        INT NOT NULL DEFAULT 0,
    CONSTRAINT fk_stock_producto
        FOREIGN KEY (id_producto)
        REFERENCES productos_pato(id_producto)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT uq_stock_producto UNIQUE (id_producto)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Movimientos de stock
CREATE TABLE movimientos_stock (
    id_movimiento       INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_producto         INT UNSIGNED NOT NULL,
    id_pedido           INT UNSIGNED NULL,
    fecha_movimiento    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipo_movimiento     ENUM('ENTRADA','SALIDA','AJUSTE') NOT NULL,
    cantidad            INT NOT NULL,
    descripcion         VARCHAR(255),
    CONSTRAINT fk_mov_stock_producto
        FOREIGN KEY (id_producto)
        REFERENCES productos_pato(id_producto)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_mov_stock_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES pedidos(id_pedido)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Líneas de pedido (detalle)
CREATE TABLE lineas_pedido (
    id_linea        INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_pedido       INT UNSIGNED NOT NULL,
    id_producto     INT UNSIGNED NOT NULL,
    cantidad        INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal        DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_lineas_pedido_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES pedidos(id_pedido)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_lineas_pedido_producto
        FOREIGN KEY (id_producto)
        REFERENCES productos_pato(id_producto)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==========================
-- VISTAS PARA MOSTRAR FKs
-- ==========================

-- Productos con categoría y stock
CREATE OR REPLACE VIEW vw_productos_pato AS
SELECT 
    p.id_producto,
    p.nombre,
    p.descripcion,
    p.color,
    p.tamano,
    p.precio,
    p.activo,
    c.nombre AS categoria,
    IFNULL(s.cantidad, 0) AS stock_disponible
FROM productos_pato p
JOIN categorias_pato c ON p.id_categoria = c.id_categoria
LEFT JOIN stock_actual s ON p.id_producto = s.id_producto;

-- Pedidos con datos básicos de cliente
CREATE OR REPLACE VIEW vw_pedidos_con_clientes AS
SELECT
    ped.id_pedido,
    ped.fecha_pedido,
    ped.estado,
    ped.total,
    cli.id_cliente,
    cli.nombre,
    cli.apellidos,
    cli.email
FROM pedidos ped
JOIN clientes cli ON ped.id_cliente = cli.id_cliente;

-- Detalle de líneas de pedido con cliente y producto
CREATE OR REPLACE VIEW vw_lineas_pedido_detalle AS
SELECT
    lp.id_linea,
    lp.id_pedido,
    ped.fecha_pedido,
    ped.estado,
    cli.id_cliente,
    cli.nombre AS nombre_cliente,
    cli.apellidos AS apellidos_cliente,
    lp.id_producto,
    prod.nombre AS nombre_producto,
    lp.cantidad,
    lp.precio_unitario,
    lp.subtotal
FROM lineas_pedido lp
JOIN pedidos ped   ON lp.id_pedido   = ped.id_pedido
JOIN clientes cli  ON ped.id_cliente = cli.id_cliente
JOIN productos_pato prod ON lp.id_producto = prod.id_producto;

-- Movimientos de stock con detalle de producto y pedido
CREATE OR REPLACE VIEW vw_movimientos_stock_detalle AS
SELECT
    ms.id_movimiento,
    ms.fecha_movimiento,
    ms.tipo_movimiento,
    ms.cantidad,
    ms.descripcion,
    ms.id_pedido,
    prod.id_producto,
    prod.nombre AS nombre_producto
FROM movimientos_stock ms
JOIN productos_pato prod ON ms.id_producto = prod.id_producto;

-- ==========================
-- DATOS DE EJEMPLO
-- Respeta orden por FKs:
-- 1) Categorías
-- 2) Clientes
-- 3) Productos
-- 4) Pedidos
-- 5) Stock actual
-- 6) Líneas de pedido
-- 7) Movimientos de stock
-- ==========================

-- 1) Categorías de patos
INSERT INTO categorias_pato (id_categoria, nombre, descripcion) VALUES
(1, 'Clásico amarillo',    'Patos de goma amarillos estándar'),
(2, 'Ediciones limitadas', 'Patos especiales de tiradas limitadas'),
(3, 'Profesiones',         'Patos disfrazados de diferentes profesiones'),
(4, 'Temáticos cine',      'Patos inspirados en películas y series');

-- 2) Clientes
INSERT INTO clientes (
    id_cliente, nombre, apellidos, email, telefono,
    direccion, ciudad, codigo_postal, pais, fecha_alta
) VALUES
(1, 'Ana',   'García', 'ana.garcia@example.com',   '600000001',
    'Calle Sol 1',   'Valencia',  '46001', 'España', '2025-01-01 10:00:00'),
(2, 'Carlos','López', 'carlos.lopez@example.com', '600000002',
    'Avenida Luna 5','Madrid',    '28001', 'España', '2025-01-02 11:00:00'),
(3, 'Marta', 'Ruiz',  'marta.ruiz@example.com',   '600000003',
    'Plaza Mar 3',   'Barcelona', '08001', 'España', '2025-01-03 12:00:00');

-- 3) Productos (patos de goma)
-- Precios enteros para cuadrar fácilmente totales de pedido
INSERT INTO productos_pato (
    id_producto, nombre, descripcion, color, tamano, precio, activo, id_categoria
) VALUES
(1, 'Pato clásico pequeño',
    'Pato de goma amarillo clásico tamaño pequeño',
    'amarillo', 'pequeño', 5.00, 1, 1),
(2, 'Pato programador',
    'Pato de goma con gafas y pequeño portátil',
    'negro', 'mediano', 10.00, 1, 3),
(3, 'Pato superhéroe',
    'Pato de goma con capa y antifaz',
    'azul', 'mediano', 8.00, 1, 4),
(4, 'Pato unicornio brillante',
    'Pato de goma con cuerno de unicornio y purpurina',
    'rosa', 'grande', 12.00, 1, 2);

-- 4) Pedidos (cabecera)
-- Totales cuadran con las líneas de pedido que se insertan más abajo
INSERT INTO pedidos (
    id_pedido, id_cliente, fecha_pedido, estado, total
) VALUES
(1, 1, '2025-02-01 09:30:00', 'PAGADO', 28.00),
(2, 2, '2025-02-02 16:15:00', 'ENVIADO', 25.00),
(3, 3, '2025-02-03 18:45:00', 'PAGADO', 25.00);

-- 5) Stock actual (después de ventas de ejemplo)
INSERT INTO stock_actual (id_stock, id_producto, cantidad) VALUES
(1, 1, 94),  -- partiendo de 100 y restando ventas
(2, 2, 48),  -- partiendo de 50
(3, 3, 28),  -- partiendo de 30
(4, 4, 19);  -- partiendo de 20

-- 6) Líneas de pedido (detalle)
-- Pedido 1 (Ana): 2x clásico, 1x programador, 1x superhéroe -> total 28
-- Pedido 2 (Carlos): 1x unicornio, 1x clásico, 1x superhéroe -> total 25
-- Pedido 3 (Marta): 3x clásico, 1x programador -> total 25
INSERT INTO lineas_pedido (
    id_linea, id_pedido, id_producto, cantidad, precio_unitario, subtotal
) VALUES
(1, 1, 1, 2,  5.00, 10.00),
(2, 1, 2, 1, 10.00, 10.00),
(3, 1, 3, 1,  8.00,  8.00),

(4, 2, 4, 1, 12.00, 12.00),
(5, 2, 1, 1,  5.00,  5.00),
(6, 2, 3, 1,  8.00,  8.00),

(7, 3, 1, 3,  5.00, 15.00),
(8, 3, 2, 1, 10.00, 10.00);

-- 7) Movimientos de stock
-- Entradas iniciales y salidas asociadas a los pedidos
INSERT INTO movimientos_stock (
    id_movimiento, id_producto, id_pedido, fecha_movimiento,
    tipo_movimiento, cantidad, descripcion
) VALUES
-- Entradas iniciales
(1, 1, NULL, '2025-01-31 08:00:00', 'ENTRADA', 100, 'Stock inicial producto 1'),
(2, 2, NULL, '2025-01-31 08:00:00', 'ENTRADA',  50, 'Stock inicial producto 2'),
(3, 3, NULL, '2025-01-31 08:00:00', 'ENTRADA',  30, 'Stock inicial producto 3'),
(4, 4, NULL, '2025-01-31 08:00:00', 'ENTRADA',  20, 'Stock inicial producto 4'),

-- Salidas por Pedido 1 (id_pedido = 1)
(5, 1, 1, '2025-02-01 10:00:00', 'SALIDA', 2, 'Venta pedido 1 - Pato clásico pequeño'),
(6, 2, 1, '2025-02-01 10:00:00', 'SALIDA', 1, 'Venta pedido 1 - Pato programador'),
(7, 3, 1, '2025-02-01 10:00:00', 'SALIDA', 1, 'Venta pedido 1 - Pato superhéroe'),

-- Salidas por Pedido 2 (id_pedido = 2)
(8, 4, 2, '2025-02-02 17:00:00', 'SALIDA', 1, 'Venta pedido 2 - Pato unicornio brillante'),
(9, 1, 2, '2025-02-02 17:00:00', 'SALIDA', 1, 'Venta pedido 2 - Pato clásico pequeño'),
(10,3, 2, '2025-02-02 17:00:00', 'SALIDA', 1, 'Venta pedido 2 - Pato superhéroe'),

-- Salidas por Pedido 3 (id_pedido = 3)
(11,1, 3, '2025-02-03 19:00:00', 'SALIDA', 3, 'Venta pedido 3 - Pato clásico pequeño'),
(12,2, 3, '2025-02-03 19:00:00', 'SALIDA', 1, 'Venta pedido 3 - Pato programador');

-- =========================================================
-- Fin del script de instalación
-- =========================================================
```


Luego se ejecuta desde la terminal:
```
python 002-multipagina.py
```
Y se abre http://127.0.0.1:5000/ en el navegador.

---
En este ejercicio se ha diseñado una base de datos relacional completa para una tienda online de patos de goma, aplicando correctamente claves primarias y foráneas para garantizar la integridad de los datos. Se han creado vistas que permiten consultar información relacionada de forma clara y estructurada, facilitando su uso desde una aplicación web. Además, se ha desarrollado una aplicación multipágina con Flask que permite visualizar los contenidos mediante plantillas HTML. Este ejercicio refuerza los conceptos de modelado de bases de datos, relaciones entre tablas y arquitectura cliente-servidor, sentando las bases para el desarrollo de aplicaciones web más complejas.

