Un modelo de datos es una representación estructurada de la información. Define qué datos se almacenan, cómo se clasifican y organizan, para qué se utilizan y cómo se conectan entre sí, de modo que pueda utilizarse y gestionarse de manera eficiente.

El objetivo de esta actividad es estructurar la información sobre la que se quiere trabajar, creando una tabla dentro de una base de datos para poder gestionarla.

Se utilizará el lenguaje SQL en MySQL para almacenar y estructurar la información sobre los clientes de una empresa. 

Para ello:

- Se definen los tipos de datos que se quiere almacenar junto con su tipo de dato/campo, para que la base de datos sepa exactamente qué está guardando y pueda hacerlo de la forma más ordenada y eficiente posible.

dni: un campo de tipo varchar con un tamaño adecuado para almacenar el número de DNI.
nombre: un campo de tipo varchar.
apellidos: un campo de tipo varchar.
email: un campo de tipo varchar.

- Luego, al entrar en mysql, accedemos a la base de datos:
```
mysql> USE funbiana;
Database changed
```

- Se procede a crear la tabla usando el comando "CREATE TABLE" y se define también el nombre de la tabla "Cliente", luego, entre paréntesis, los datos que queremos introducir a la base de datos, de la siguiente manera:
```
CREATE TABLE Cliente (
	dni VARCHAR(15) PRIMARY KEY,
	nombre VARCHAR(50),
	apellidos VARCHAR(100),
	email VARCHAR(100)
);
```
- Al ejecutar el comando, mysql demuestra que se ha creado la tabla con la respuesta: 
```
Query OK, 0 rows affected (0,05 sec)
```

Y para verificar que se ha creado correctamente, ejecutamos el comando "SHOW COLUMNS FROM Cliente;", donde muestra la siguiente respuesta con la tabla creada.
```
mysql> SHOW COLUMNS FROM Cliente;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| dni       | varchar(15)  | NO   | PRI | NULL    |       |
| nombre    | varchar(50)  | YES  |     | NULL    |       |
| apellidos | varchar(100) | YES  |     | NULL    |       |
| email     | varchar(100) | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
4 rows in set (0,01 sec)
```


El código completo en consola se ilustra de la siguiente manera:
```
mysql> CREATE DATABASE funbiana;
Query OK, 1 row affected (0,02 sec)

mysql> USE funbiana;
Database changed

mysql> CREATE TABLE Cliente (
    ->     dni VARCHAR(15) PRIMARY KEY,
    ->     nombre VARCHAR(50),
    ->     apellidos VARCHAR(100),
    ->     email VARCHAR(100)
    -> );
Query OK, 0 rows affected (0,05 sec)

mysql> SHOW COLUMNS FROM Cliente;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| dni       | varchar(15)  | NO   | PRI | NULL    |       |
| nombre    | varchar(50)  | YES  |     | NULL    |       |
| apellidos | varchar(100) | YES  |     | NULL    |       |
| email     | varchar(100) | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
4 rows in set (0,01 sec)

```

Este ejercicio permite comprender cómo un modelo de datos ayuda a estructurar y organizar la información antes de almacenarla. A través del uso de SQL en MySQL se creó la tabla Cliente, definiendo cada campo con su tipo de dato correspondiente para asegurar una gestión precisa y eficiente de los datos. La verificación mediante comandos como SHOW COLUMNS confirma que la tabla fue creada correctamente y que la base de datos está lista para recibir y administrar la información de los clientes.








