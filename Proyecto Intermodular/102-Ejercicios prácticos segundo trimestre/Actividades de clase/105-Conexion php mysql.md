En este ejercicio se trabaja el acceso a bases de datos desde PHP mediante la extensión MySQLi, aplicando una consulta SQL para obtener los artículos de un blog y mostrar su contenido en formato HTML. Se utilizan los conceptos de conexión a base de datos, ejecución de consultas, recorrido de resultados mediante bucles y presentación de la información estructurada en etiquetas HTML. Además, se introducen técnicas básicas de detección y gestión de errores para facilitar el desarrollo y depuración del código. El objetivo del ejercicio es comprender cómo PHP interactúa con una base de datos y cómo se construye una salida web dinámica a partir de los datos almacenados.

---
El ejercicio se compone de cuatro partes principales:

#### 1. Conexión a la base de datos

Se establece una conexión con la base de datos blogphp utilizando la clase mysqli. Para ello se definen los datos de conexión (host, usuario, contraseña y base de datos) y se crea un objeto conexión.

#### 2. Ejecución de la consulta SQL

Se ejecuta una consulta SQL que selecciona todos los registros de la tabla blog. El resultado se almacena en la variable $resultado, que contiene todas las filas devueltas por la base de datos.

#### 3. Recorrido de resultados y presentación en HTML

Mediante un bucle while se recorren todas las filas obtenidas y se muestran dentro de etiquetas ```<article>```, mostrando el título, la fecha, el autor y el contenido de cada artículo.

#### 4. Cierre de la conexión

Una vez procesados todos los resultados, se cierra la conexión con la base de datos utilizando el método close() para liberar recursos.

---
A continuación se muestra el código funcional que se ha utilizado:
```
<?php
  '''
  Conexión y visualización de artículos en PHP
  2026 Fabiana Victoria Sotillo
  Programa que conecta con una base de datos MySQL, obtiene los artículos de un blog
  y los muestra en formato HTML utilizando PHP y MySQLi.
  '''
  
  // Mostrar errores durante el desarrollo
  error_reporting(E_ALL);
  ini_set('display_errors', 1);

  // Datos de conexión
  $host = "localhost";
  $user = "blogphp";
  $pass = "Blogphp123$";
  $db   = "blogphp";

  // Crear conexión
  $conexion = new mysqli($host, $user, $pass, $db);

  // Comprobar conexión
  if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
  }

  // Consulta SQL
  $sql = "SELECT * FROM blog";
  $resultado = $conexion->query($sql);

  // Recorrer resultados y mostrarlos en HTML
  while ($fila = $resultado->fetch_assoc()) {
    echo "<article>";
    echo "<h2>" . $fila["titulo"] . "</h2>";
    echo "<p><strong>Fecha:</strong> " . $fila["fecha"] . "</p>";
    echo "<p><strong>Autor:</strong> " . $fila["autor"] . "</p>";
    echo "<p>" . $fila["contenido"] . "</p>";
    echo "</article><hr>";
  }

  // Cerrar conexión
  $conexion->close();
?>
```

Para ejecutar el programa hay que guardar el archivo en el servidor web (por ejemplo, en /var/www/html/), luego abrir el archivo desde el localhost en el navegador.

---
Para detectar errores durante el desarrollo en php se utilizan:
```
error_reporting(E_ALL);
ini_set('display_errors', 1);
```

También se pueden revisar los registros del servidor en:

/var/log/apache2/error.log


En entornos de producción, estos errores deben ocultarse configurando el archivo php.ini.

---
Como resultado final, el navegador muestra una página web con todos los artículos del blog, cada uno dentro de una etiqueta ```<article>``` y con su información estructurada correctamente.

En este ejercicio se ha desarrollado un script en PHP que permite conectarse a una base de datos MySQL, ejecutar una consulta para obtener los artículos de un blog y mostrarlos en formato HTML mediante un bucle de recorrido de resultados. Se han aplicado los conceptos de conexión a bases de datos, ejecución de consultas SQL, procesamiento de resultados y generación de contenido dinámico. Además, se han introducido técnicas básicas de detección y gestión de errores que facilitan el desarrollo y mantenimiento del código. Este ejercicio refuerza los fundamentos del desarrollo web dinámico con PHP y bases de datos, y constituye una base sólida para aplicaciones web más completas.
