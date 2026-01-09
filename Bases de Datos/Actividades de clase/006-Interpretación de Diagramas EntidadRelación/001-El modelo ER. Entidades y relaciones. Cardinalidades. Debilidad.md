# Aplicación del modelo Entidad-Relación en bases de datos y programación en Python

El presente ejercicio tiene como objetivo aplicar los conceptos fundamentales del modelo Entidad-Relación (ER) para el diseño de bases de datos relacionales y su posterior representación mediante programación orientada a objetos en Python. El modelo ER permite representar de forma estructurada las entidades de un sistema, sus atributos y las relaciones existentes entre ellas, facilitando la correcta organización de la información. En este contexto, se trabaja con las entidades Cliente, Pedido, LineaPedido y Producto, estableciendo sus relaciones y trasladando esta estructura tanto a una base de datos relacional como a clases Python, con el propósito de comprender cómo se implementan estos conceptos en entornos reales.

---
En esta actividad se comienza revisando un diagrama Entidad-Relación proporcionado en formato HTML, en el que se identifican las entidades principales del sistema y las relaciones unidireccionales entre ellas. A partir de este diagrama, se definen las tablas correspondientes en una base de datos relacional, estableciendo las claves primarias y foráneas necesarias para mantener la integridad de los datos.

Posteriormente, se trasladan estas entidades al ámbito de la programación mediante la creación de clases en Python que representan cada una de las entidades del modelo ER. Cada clase contiene los atributos definidos en el diagrama y mantiene referencias a otras clases para representar las relaciones entre los objetos. Finalmente, se desarrolla un programa práctico que permite crear instancias de las entidades, relacionarlas entre sí y mostrar la información resultante, integrando así los conceptos de bases de datos y programación orientada a objetos.

---
A continuación, se describe el procedimiento seguido para llevar a cabo la actividad.

1. Revisión del diagrama Entidad-Relación

Se analiza el diagrama ER proporcionado en formato HTML, en el que se identifican las siguientes entidades:

Cliente

Pedido

LineaPedido

Producto

Asimismo, se observan las relaciones unidireccionales representadas mediante flechas, que indican cómo se vinculan los pedidos con los clientes y las líneas de pedido con los productos.

2. Creación de las tablas en la base de datos

Basándose en el diagrama ER, se crean las tablas correspondientes en una base de datos relacional utilizando scripts SQL. Cada tabla incluye su clave primaria y las claves foráneas necesarias para representar las relaciones entre entidades, garantizando la coherencia y la integridad referencial de los datos.

3. Representación de las entidades mediante clases Python

Se desarrollan clases en Python para representar cada una de las entidades del modelo ER. Cada clase incluye los atributos definidos en el diagrama y referencias a otras clases para modelar las relaciones. Por ejemplo, la clase Pedido contiene una referencia a un objeto de la clase Cliente, y la clase LineaPedido contiene referencias a Pedido y Producto.

4. Implementación de la aplicación práctica

Se implementa un programa que permite:

Crear instancias de clientes, pedidos, líneas de pedido y productos.

Establecer relaciones entre los objetos creados.

Mostrar por pantalla información relevante sobre los pedidos realizados y los productos asociados.

Este programa permite comprobar el correcto funcionamiento de la estructura diseñada y la relación entre las entidades.

---
Como resultado de esta actividad, se obtiene una base de datos estructurada según el modelo ER y un conjunto de clases Python que representan las mismas entidades y relaciones. Además, se dispone de un programa funcional que permite crear y relacionar objetos, mostrando la información de forma organizada y coherente.

Este ejercicio permite aplicar de forma práctica el modelo Entidad-Relación en el diseño de bases de datos relacionales y su implementación mediante programación orientada a objetos en Python. La correcta identificación de entidades, atributos y relaciones facilita la organización de la información y mejora la eficiencia en la gestión de datos. Esta práctica refuerza la comprensión del modelo ER como una herramienta fundamental en el diseño de sistemas de información y sienta las bases para el desarrollo de aplicaciones más complejas en entornos profesionales.
