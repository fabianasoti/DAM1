```
'''
Update
2026 Fabiana Sotillo
Actualización de un registro en una base de datos
mediante formulario y script de procesamiento.
'''
```

---
El presente ejercicio tiene como objetivo aplicar los conceptos fundamentales relacionados con la actualización de registros en una base de datos, utilizando formularios web y scripts de procesamiento. A través de la identificación de un empleado mediante su ID, la conexión a la base de datos y la ejecución de una consulta de actualización, se busca comprender el funcionamiento completo del proceso de modificación de información en un entorno de desarrollo real, integrando bases de datos, programación del lado del servidor y formularios HTML.

---
En esta práctica se trabaja con un sistema que permite modificar la información de un empleado almacenado en una base de datos llamada empleados. Para ello, se utiliza un formulario que recoge el identificador del empleado, el cual es procesado por un script encargado de establecer la conexión con la base de datos, obtener los datos correspondientes y ejecutar la actualización solicitada.

Este proceso permite entender cómo se gestionan los cambios de información en una base de datos y cómo se integran distintos componentes de una aplicación web para realizar operaciones de mantenimiento de datos de forma segura y estructurada.

---
Aplicación práctica:
1. Acceso al entorno de desarrollo y revisión del código de ejemplo.

En primer lugar, se accede a los archivos del proyecto. Se revisa el código de ejemplo proporcionado con el fin de comprender la estructura general del sistema y el funcionamiento del proceso de actualización de registros.

La estructura de la base de datos es la siguiente:
```
-- 1. Create database
CREATE DATABASE IF NOT EXISTS empleados
    DEFAULT CHARACTER SET utf8mb4
    COLLATE utf8mb4_spanish_ci;

-- 2. Use database
USE empleados;

-- 3. Create table empleados
DROP TABLE IF EXISTS empleados;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    departamento VARCHAR(100)
);

-- 4. Insert sample data
INSERT INTO empleados (nombre, puesto, salario, fecha_contratacion, departamento) VALUES
('Ana Torres', 'Administrativa', 21000.00, '2021-03-15', 'Administración'),
('Luis Martínez', 'Desarrollador Backend', 32000.00, '2020-11-02', 'IT'),
('Marta López', 'Desarrolladora Frontend', 30000.00, '2022-01-10', 'IT'),
('Carlos Pérez', 'Comercial', 25000.00, '2019-07-08', 'Ventas'),
('Elena García', 'Marketing Specialist', 27000.00, '2021-09-23', 'Marketing'),
('Javier Ruiz', 'Técnico de Soporte', 24000.00, '2020-02-14', 'Soporte'),
('Patricia Sánchez', 'Recursos Humanos', 26000.00, '2018-06-20', 'RRHH'),
('Sergio Gómez', 'Data Analyst', 35000.00, '2022-05-01', 'Datos'),
('Raquel Navarro', 'Diseñadora UX/UI', 29000.00, '2021-12-01', 'IT'),
('David Fernández', 'Contable', 23000.00, '2019-10-30', 'Finanzas');
```

Archivo 001-Miniformulario.html del apartado Update:
```
<!doctype html>
<html lang="es">
	<head>
		<title>Fabiana Victoria Sotillo</title>
		<meta charset="utf-8">
	</head>
	<body>
		<form action="002-procesamodificar.php" method="POST">
			<p>Introduce el ID del elemento que quieres modificar</p>
			<input type="number" name="id" placeholder="id">
			<input type="submit">
		</form>
	</body>
</html>
```
Archivo 003-procesaractualizacion.php:
```
<?php
	// Primero cogemos la info que viene del formulario
  
  $nombre = $_POST['nombre'];
  $puesto = $_POST['puesto'];
  $salario = $_POST['salario'];
  $fecha_contratacion = $_POST['fecha_contratacion'];
  $departamento = $_POST['departamento'];
  
  $id = $_POST['id'];

	 // Y luego metemos esa información en la base de datos
  $host = "localhost";
  $user = "empleados";
  $pass = "Empleados123$";
  $db   = "empleados";

  $conexion = new mysqli($host, $user, $pass, $db);

	// Metemos los datos en la base de datos
  $sql = "
  	 UPDATE empleados SET
     	nombre = '".$nombre."',
      puesto = '".$puesto."',
      salario = '".$salario."',
      fecha_contratacion = '".$fecha_contratacion."',
      departamento = '".$departamento."' 
      WHERE id = ".$id."
    ;
  ";
  $conexion->query($sql);
	
  $conexion->close();
  
?>
```

Archivo 002-usuario con permisos.sql:
```
CREATE USER 
'empleados'@'localhost' 
IDENTIFIED  BY 'Empleados123$';

GRANT USAGE ON *.* TO 'empleados'@'localhost';

ALTER USER 'empleados'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON empleados.* 
TO 'empleados'@'localhost';

FLUSH PRIVILEGES;
```

Este análisis previo resulta fundamental para identificar las partes principales del sistema y comprender cómo se realiza la comunicación entre el formulario y el script de procesamiento.

2. Identificación del empleado mediante el formulario

A continuación, se utiliza el formulario 001-Miniformulario.html del apartado Update, en el cual se introduce el ID del empleado que se desea modificar. Este formulario permite enviar la información al servidor para que sea procesada por el script correspondiente. En este caso se ha seleccionado modificar el ID 2.

Con un script en MySQL se prueba ver sus datos antes de ejecutar la modificación:
```
SELECT * FROM empleados WHERE id = 2 LIMIT 1;
+----+----------------+-----------------------+----------+--------------------+--------------+
| id | nombre         | puesto                | salario  | fecha_contratacion | departamento |
+----+----------------+-----------------------+----------+--------------------+--------------+
|  2 | Luis Martínez  | Desarrollador Backend | 32000.00 | 2020-11-02         | IT           |
+----+----------------+-----------------------+----------+--------------------+--------------+
```

Una vez enviado el formulario, el sistema recibe el identificador del empleado y comienza el proceso de búsqueda y actualización de sus datos en la base de datos. Se ha modificado el sueldo y el puesto de trabajo.


3. Conexión a la base de datos y procesamiento de la actualización

El script 003-procesaractualizacion.php se encarga de establecer la conexión con la base de datos utilizando los permisos configurados en el archivo 002-usuario con permisos.sql. A través de esta conexión, el sistema obtiene los datos del empleado seleccionado y ejecuta la consulta SQL necesaria para actualizar su información.

Este paso permite aplicar los conceptos de conexión a bases de datos, ejecución de consultas y modificación de registros, garantizando que los cambios se realicen correctamente.

Se ejecuta el script en MySQL nuevamente para comprobar que se ha ejecutado el cambio:
```
SELECT * FROM empleados WHERE id = 2 LIMIT 1;
+----+----------------+-------------------------+----------+--------------------+--------------+
| id | nombre         | puesto                  | salario  | fecha_contratacion | departamento |
+----+----------------+-------------------------+----------+--------------------+--------------+
|  2 | Luis Martínez  | Desarrollador FullStack | 35000.00 | 2020-11-02         | IT           |
+----+----------------+-------------------------+----------+--------------------+--------------+
1 row in set (0,00 sec)

```

4. Cierre de la conexión

Una vez finalizada la actualización del registro, se procede al cierre de la conexión con la base de datos. Este paso es importante para liberar recursos del servidor y mantener un funcionamiento eficiente y seguro del sistema.

---
Como resultado del ejercicio, se obtiene un sistema funcional capaz de actualizar los datos de un empleado a partir de su identificador. El sistema permite modificar la información almacenada en la base de datos de forma controlada y estructurada, utilizando formularios web y scripts de procesamiento.

En este ejercicio se han aplicado los conceptos fundamentales relacionados con la actualización de registros en bases de datos mediante formularios web y scripts en PHP. Esta práctica permite comprender cómo se gestionan las modificaciones de información en un sistema real, reforzando el uso de consultas SQL, conexiones a bases de datos y procesamiento de formularios. Asimismo, este tipo de ejercicios resulta esencial para desarrollar aplicaciones web dinámicas y sistemas de información eficientes, donde la gestión y mantenimiento de datos es una tarea fundamental.
