En este ejercicio se trabaja el uso de sesiones en PHP para mantener información entre diferentes páginas web dentro de una pequeña aplicación personal. La aplicación está contextualizada en un entorno creativo, donde se gestionan proyectos de ganchillo y la música, dos aficiones que permiten comprender de forma práctica cómo los datos pueden conservarse entre distintas páginas. A través del uso de variables, enlaces y sesiones, se refuerzan los conceptos fundamentales de PHP orientados al desarrollo web dinámico.

---
El ejercicio se estructura en tres fases principales:

#### 1. Creación del archivo de origen

Se crea un archivo llamado 003-origen.php en el que se declara una variable $nombre, que representa al usuario aficionado al ganchillo y al canto. Este archivo contiene además un enlace que permite navegar hacia otra página.

#### 2. Creación del archivo destino

En el archivo 004-destino.php se intenta mostrar el contenido de la variable $nombre. Esto permite observar que las variables no se mantienen automáticamente entre páginas, lo que justifica la necesidad de usar sesiones.

#### 3. Uso de sesiones en PHP

Se crea un nuevo archivo 006-destino con sesiones.php donde se inicia una sesión mediante la función session_start(). A través de la variable global $_SESSION, se puede acceder al nombre del usuario desde cualquier página mientras la sesión esté activa.

Las sesiones permiten mantener información persistente durante la navegación del usuario, lo cual es fundamental en aplicaciones web reales, como por ejemplo una plataforma para gestionar proyectos de ganchillo o listas de canciones favoritas.

---
A continuación se muestra el código:
#### 003-origen.php
```
<?php
	$nombre = "Fabiana Victoria";
?>
<a href="004-destino.php">Vamos a otra página</a>
```
Este archivo define la variable $nombre, que representa a la persona que gestiona sus proyectos de ganchillo y canciones, y proporciona un enlace para continuar la navegación.

#### 004-destino.php
```
<?php
	echo $nombre;
?>
```

Este archivo intenta mostrar la variable $nombre, lo que permite comprobar que las variables no se comparten automáticamente entre páginas.

#### 006-destino con sesiones.php
```
<?php
	session_start();
	echo $_SESSION['nombre'];
?>
```

En este archivo se inicia la sesión y se muestra el valor almacenado en la variable de sesión ```$_SESSION['nombre']```, permitiendo acceder al nombre del usuario desde cualquier página de la aplicación.

---
Gracias al uso de sesiones, ahora es posible mantener la información del usuario entre diferentes páginas, lo cual permite simular una aplicación real donde una persona puede gestionar sus proyectos de ganchillo y su lista de canciones favoritas sin perder sus datos al cambiar de sección.

En este ejercicio se ha aprendido a utilizar sesiones en PHP para mantener información entre diferentes páginas web, aplicando conceptos básicos como variables, enlaces y variables globales. Este sistema es fundamental en aplicaciones web reales, ya que permite conservar datos del usuario durante su navegación, como sus proyectos de ganchillo o sus canciones favoritas. El uso de sesiones representa un paso importante en el desarrollo de aplicaciones dinámicas y refuerza los fundamentos del lenguaje PHP trabajados en esta unidad.
