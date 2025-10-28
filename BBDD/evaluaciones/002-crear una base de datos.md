MySQL es un sistema de gestión de bases de datos relacionales que permite almacenar, organizar y administrar información de manera estructurada mediante tablas compuestas por filas y columnas. Es ampliamente utilizado en aplicaciones web y empresariales, funcionando bajo un modelo cliente-servidor y empleando SQL (Structured Query Language) para interactuar con los datos.

El objetivo de este ejercicio es que el alumno se familiarice con la instalación de MySQL, el inicio de sesión en el gestor de bases de datos y la creación de una base de datos propia. Estos pasos iniciales son fundamentales para comprender la estructura y administración de datos en un entorno relacional. 

- Para ello se instala MySQL en el sistema, accediendo a una terminal y ejecutando: 
```
sudo apt install mysql-server
```

- Una vez instalado, se ejecuta sudo "mysql_secure_installation" para los ajustes de seguridad, como por ejemplo, establecer la contraseña para el usuario root.

- Luego se procede a iniciar sesión en el gestor de bases de datos con:
```
sudo mysql -u root -p
```

- Para crear una nueva base de datos, se utiliza el comando:  "CREATE DATABASE + [el nombre de la base de datos] + ;"
```
CREATE DATABASE empresadam;
```

- Y por último, se selecciona la base de datos que se acaba de crear, con:
```
USE empresadam;
```

Y de esta manera, ya se obtiene acceso a la base de datos, para gestionarla en el futuro, creando tablas y modificándolas según sea conveniente.

El código completo en consola se ilustra de la siguiente manera:

```
sudo mysql -u root -p
[sudo] contraseña para fabiana: 
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.43-0ubuntu0.24.04.2 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE empresadam;
Query OK, 1 row affected (0,02 sec)

mysql> USE empresadam;
Database changed
```

Con la realización de este ejercicio, se ha aprendido a instalar MySQL, realizar ajustes de seguridad básicos, iniciar sesión como usuario root y crear y seleccionar una nueva base de datos. Estas acciones constituyen la base para futuras operaciones, como la creación de tablas, inserción de datos y consultas SQL. 
Al finalizar, se ha establecido un entorno funcional en el que se pueden gestionar datos de manera organizada y segura, sentando las bases para el aprendizaje de técnicas más avanzadas de manejo de bases de datos.

