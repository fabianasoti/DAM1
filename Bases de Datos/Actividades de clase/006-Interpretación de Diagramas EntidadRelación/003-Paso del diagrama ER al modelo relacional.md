El presente ejercicio tiene como objetivo aplicar los conceptos fundamentales del modelo Entidad-Relación (ER) y su traducción a modelos relacionales, comprendiendo cómo un diseño conceptual puede transformarse en una estructura de base de datos funcional. A partir del análisis de un diagrama ER proporcionado en formato HTML, se identifican las entidades, sus atributos y las relaciones existentes entre ellas para posteriormente diseñar los esquemas relacionales correspondientes. De este modo, se busca reforzar la comprensión del diseño de bases de datos y su implementación en sistemas gestores como MySQL.

---
En esta actividad se comienza analizando un diagrama Entidad-Relación que representa la estructura de un sistema de información. A partir de dicho diagrama, se identifican las entidades principales, sus atributos y las relaciones que las conectan.

Posteriormente, se realiza la traducción del modelo ER al modelo relacional, definiendo una tabla por cada entidad y estableciendo las claves primarias y foráneas necesarias para representar correctamente las relaciones entre ellas. Una vez diseñado el modelo relacional, se implementa en un entorno SQL mediante la creación de las tablas correspondientes y la ejecución de consultas básicas para comprobar la integridad y el correcto relacionamiento de los datos.

Finalmente, se reflexiona sobre la utilidad de este proceso en el diseño de sistemas reales y su importancia en el desarrollo de aplicaciones basadas en bases de datos.

---
Aplicación práctica
1. Revisión del diagrama Entidad-Relación

Se analiza el diagrama ER proporcionado en el archivo 005-diagrama-1aN.html, identificando las entidades principales, sus atributos y las relaciones entre ellas. Este diagrama permite visualizar de forma gráfica la estructura del sistema y comprender cómo se organizan los datos a nivel conceptual.

A partir del diagrama se reconocen las entidades del sistema y se estudian las relaciones de tipo uno a muchos (1:N) entre ellas, lo que permite definir correctamente la dependencia entre los distintos elementos.

2. Traducción al modelo relacional

Una vez identificadas las entidades y relaciones del diagrama ER, se procede a su traducción al modelo relacional. Para ello, se define una tabla por cada entidad, estableciendo sus atributos como columnas y asignando una clave primaria que permita identificar de forma única cada registro.

Las relaciones entre entidades se representan mediante claves foráneas, garantizando la integridad referencial y reflejando correctamente las dependencias existentes entre las tablas.

De este modo, el modelo conceptual se transforma en una estructura relacional lista para ser implementada en un gestor de bases de datos.

3. Implementación en un entorno SQL

A continuación, se implementa el modelo relacional en un entorno de desarrollo SQL como MySQL o PostgreSQL. Para ello, se crean las tablas correspondientes utilizando sentencias CREATE TABLE y se definen las claves primarias y foráneas necesarias.

Una vez creadas las tablas, se realizan consultas básicas para verificar:

Que las tablas se han creado correctamente.

Que las relaciones entre ellas funcionan de forma adecuada.

Que la integridad de los datos se mantiene al insertar nuevos registros.

Estas pruebas permiten comprobar que la traducción del modelo ER al modelo relacional se ha realizado correctamente.

---
Como resultado del ejercicio, se obtiene una base de datos estructurada a partir de un diagrama Entidad-Relación, en la que cada entidad se representa mediante una tabla y cada relación mediante claves foráneas. El sistema resultante permite almacenar información de forma organizada y mantener la coherencia entre los distintos datos relacionados.

En este ejercicio se han aplicado los conceptos del modelo Entidad-Relación y su traducción al modelo relacional mediante el análisis de un diagrama ER y su implementación en un sistema gestor de bases de datos. Esta práctica permite comprender cómo se diseña una base de datos desde su fase conceptual hasta su implementación técnica, reforzando el pensamiento lógico y el diseño estructurado de sistemas de información. Asimismo, constituye una base fundamental para el desarrollo de aplicaciones reales que dependen de bases de datos relacionales para la gestión eficiente de la información.
