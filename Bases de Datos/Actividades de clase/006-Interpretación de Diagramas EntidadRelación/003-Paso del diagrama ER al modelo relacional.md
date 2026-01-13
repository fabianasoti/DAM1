```
Diagramas ER y Modelo Relacional (Relación 1 a N)
2026 Fabiana Sotillo
Modelo Relacional (Relación 1 a N) con aplicación práctica en MySQL
```

---
En este ejercicio se trabaja el concepto de diagramas Entidad-Relación (ER) y su traducción a modelos relacionales, fundamentales en el diseño de bases de datos. Un diagrama ER permite representar gráficamente las entidades, sus atributos y las relaciones entre ellas, mientras que el modelo relacional traduce esta información en tablas estructuradas que pueden implementarse en un gestor de bases de datos. El objetivo de esta práctica es analizar un diagrama ER con una relación de tipo uno a muchos (1:N), identificar sus elementos principales y transformarlos en un esquema relacional funcional, aplicando claves primarias y foráneas para garantizar la integridad de los datos.

El diagrama ER proporcionado representa un sistema sencillo de gestión de clientes y sus teléfonos. En él se identifican dos entidades principales: Cliente y Teléfono, unidas por una relación de tipo uno a muchos (1:N), donde un cliente puede tener varios teléfonos asociados.

### Entidades y atributos
- Entidad Cliente
	- id
	- nombre
	- apellidos

- Entidad Teléfono
	- id
	- id_cliente
	- tipo
	- numero

La relación se establece mediante el atributo id_cliente en la entidad Teléfono, que actúa como clave foránea y referencia al atributo id de la entidad Cliente.

### Traducción al modelo relacional

A partir del diagrama ER, se construyen dos tablas:
- Cliente: representa a los clientes del sistema.
- Telefono: almacena los teléfonos asociados a cada cliente.

La relación 1:N se implementa añadiendo una clave foránea en la tabla Teléfono que referencia a la clave primaria de la tabla Cliente.

---
A continuación se muestra la implementación del modelo relacional utilizando SQL.
```
CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255)
);

CREATE TABLE telefono (
  id INT PRIMARY KEY,
  id_cliente VARCHAR(255),
  tipo VARCHAR(255),
  numero VARCHAR(255),
  CONSTRAINT fk_telefono_1 FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);
```

Inserción de datos de ejemplo:
```
INSERT INTO Cliente (nombre, apellidos) VALUES
('Elga', 'Tito'),
('Susana', 'Horia');

INSERT INTO Telefono (id_cliente, tipo, numero) VALUES
(1, 'Móvil', '600123456'),
(1, 'Casa', '911223344'),
(2, 'Móvil', '677889900');
```

Consultas básicas

- Consultar todos los clientes con sus teléfonos:
```
SELECT Cliente.nombre, Cliente.apellidos, Telefono.tipo, Telefono.numero
FROM Cliente
JOIN Telefono ON Cliente.id = Telefono.id_cliente;
```

- Consultar los teléfonos de un cliente específico:
```
SELECT tipo, numero
FROM Telefono
WHERE id_cliente = 1;
```

Estas consultas permiten comprobar que la relación entre las tablas funciona correctamente y que cada teléfono está vinculado a su cliente correspondiente.

---
Este ejercicio permite comprender de forma práctica cómo un diagrama Entidad-Relación se transforma en un modelo relacional listo para ser implementado en una base de datos real. A través del análisis de las entidades, sus atributos y la relación uno a muchos, se refuerza el uso de claves primarias y foráneas para mantener la integridad referencial. 

Esta práctica resulta fundamental para el desarrollo de sistemas de información, ya que el diseño correcto de la base de datos es la base de cualquier aplicación informática. Además, estos conocimientos pueden aplicarse directamente en proyectos reales como sistemas de gestión de clientes, ventas o inventarios, facilitando el almacenamiento estructurado y seguro de la información.
