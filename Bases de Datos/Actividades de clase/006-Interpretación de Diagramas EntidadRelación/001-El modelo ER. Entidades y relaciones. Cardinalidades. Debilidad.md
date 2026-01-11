```
'''
Modelo Entidad-Relación
2026 Fabiana Sotillo
Implementación del modelo Entidad-Relación mediante diagrama ER,
bases de datos relacionales (SQL) y clases en Python
'''
```

---
El presente ejercicio tiene como objetivo aplicar el modelo Entidad-Relación (ER) para el diseño y estructuración de bases de datos relacionales, integrando la representación gráfica mediante un diagrama ER, la creación de tablas en MySQL y la implementación de las entidades a través de clases en Python. A partir de un diagrama exportado en formato HTML, se identifican las entidades Cliente, Pedido, LineaPedido y Producto, así como sus relaciones, para posteriormente trasladar dicha estructura a una base de datos relacional y a un modelo orientado a objetos. De este modo, se busca comprender cómo se diseñan sistemas de información basados en bases de datos y cómo se representan sus entidades y relaciones en aplicaciones reales.

En esta actividad se comienza analizando un diagrama Entidad-Relación proporcionado en formato HTML, el cual muestra de forma visual las entidades del sistema y las relaciones existentes entre ellas. A partir de dicho diagrama, se diseñan las tablas correspondientes en una base de datos relacional utilizando scripts SQL que definen las claves primarias y las relaciones mediante claves foráneas.

Posteriormente, se representan las entidades del modelo ER mediante clases en Python, creando una estructura orientada a objetos que refleja fielmente el diseño de la base de datos. Cada clase contiene los atributos correspondientes a las propiedades de su entidad y se documentan las relaciones entre ellas.

Finalmente, se plantea una aplicación práctica donde se utilizan dichas clases para crear instancias de clientes, pedidos, productos y líneas de pedido, estableciendo las relaciones entre los distintos objetos y mostrando la información resultante.

---
1. Revisión del diagrama Entidad-Relación

El diagrama ER proporcionado en formato HTML representa visualmente las siguientes entidades:

- Cliente: id, nombre, apellidos, email

- Pedido: id, fecha, cliente_id

- LineaPedido: id, pedido_id, producto_id

- Producto: id, nombre, precio

Las relaciones son unidireccionales y se representan mediante flechas:

- Un Cliente puede tener varios Pedidos

- Un Pedido puede contener varias LineasPedido

- Cada LineaPedido hace referencia a un Producto

Este diagrama permite comprender la estructura general del sistema y las dependencias entre las distintas entidades.

2. Creación de las tablas en la base de datos

A partir del modelo ER, se crean las tablas correspondientes en una base de datos relacional utilizando los siguientes scripts SQL:
```
CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE pedido (
  id INT PRIMARY KEY,
  fecha VARCHAR(255),
  cliente_id INT,
  CONSTRAINT fk_pedido_1 FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

CREATE TABLE producto (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  precio VARCHAR(255)
);

CREATE TABLE lineapedido (
  id INT PRIMARY KEY,
  pedido_id INT,
  producto_id INT,
  CONSTRAINT fk_lineapedido_1 FOREIGN KEY (pedido_id) REFERENCES pedido(id),
  CONSTRAINT fk_lineapedido_2 FOREIGN KEY (producto_id) REFERENCES producto(id)
);
```
Estas tablas reflejan la estructura del diagrama ER, definiendo las claves primarias y estableciendo las relaciones mediante claves foráneas, lo que garantiza la integridad referencial de los datos.

3. Representación de las entidades mediante clases en Python

Cada entidad del modelo ER se representa mediante una clase en Python. Los atributos de cada clase corresponden a las propiedades definidas en el diagrama, y se documentan las relaciones entre entidades mediante referencias.
```
from typing import Optional

class Cliente:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None,
                 apellidos: Optional[str] = None, email: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __repr__(self):
        return f"Cliente(id={self.id!r}, nombre={self.nombre!r}, apellidos={self.apellidos!r}, email={self.email!r})"


class Pedido:
    def __init__(self, id: Optional[int] = None, fecha: Optional[str] = None,
                 cliente_id: Optional[int] = None):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id

    def __repr__(self):
        return f"Pedido(id={self.id!r}, fecha={self.fecha!r}, cliente_id={self.cliente_id!r})"
    # FK1: cliente_id -> cliente.id


class Lineapedido:
    def __init__(self, id: Optional[int] = None, pedido_id: Optional[int] = None,
                 producto_id: Optional[int] = None):
        self.id = id
        self.pedido_id = pedido_id
        self.producto_id = producto_id

    def __repr__(self):
        return f"Lineapedido(id={self.id!r}, pedido_id={self.pedido_id!r}, producto_id={self.producto_id!r})"
    # FK1: pedido_id -> pedido.id
    # FK2: producto_id -> producto.id


class Producto:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None,
                 precio: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto(id={self.id!r}, nombre={self.nombre!r}, precio={self.precio!r})"
```

4. Aplicación práctica con instancias y relaciones

A continuación se muestra un ejemplo de utilización de las clases para crear instancias y establecer relaciones entre ellas:
```
# Crear clientes
cliente1 = Cliente(1, "Susana", "Horia", "susana@gmail.com")
cliente2 = Cliente(2, "Elga", "Tito", "elga@gmail.com")

# Crear productos
producto1 = Producto(1, "Ovillo de lana", "12.50")
producto2 = Producto(2, "Ganchillo 4mm", "5.99")

# Crear pedidos
pedido1 = Pedido(1, "2026-01-10", cliente1.id)
pedido2 = Pedido(2, "2026-01-11", cliente2.id)

# Crear líneas de pedido
linea1 = Lineapedido(1, pedido1.id, producto1.id)
linea2 = Lineapedido(2, pedido1.id, producto2.id)

# Mostrar información
print(cliente1)
print(pedido1)
print(producto1)
print(linea1)
```
Este pequeño programa permite simular el funcionamiento de un sistema de pedidos, estableciendo relaciones entre clientes, pedidos, productos y líneas de pedido.

---
Como resultado del ejercicio, se obtiene una estructura completa basada en el modelo Entidad-Relación, representada gráficamente mediante un diagrama ER, implementada en una base de datos relacional y trasladada a un modelo orientado a objetos en Python. Además, se comprueba su funcionamiento mediante la creación de instancias y la simulación de relaciones entre las entidades.

En este ejercicio se han aplicado los conceptos fundamentales del modelo Entidad-Relación mediante el diseño de un diagrama ER, la creación de una base de datos relacional y la representación de las entidades a través de clases en Python. Esta práctica permite comprender cómo se definen estructuras de datos, cómo se establecen relaciones entre entidades y cómo se trasladan estos conceptos a sistemas reales de gestión de información. Asimismo, refuerza el pensamiento lógico, el diseño de bases de datos y la programación orientada a objetos, constituyendo una base sólida para el desarrollo de aplicaciones más complejas basadas en bases de datos relacionales.
