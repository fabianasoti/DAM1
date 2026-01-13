```
'''
Login 
2026 Fabiana Sotillo
Sistema de Inicio de Sesión con Validación de Usuario
'''
```

---
En este ejercicio se trabaja el concepto de validación de usuarios mediante un sistema de inicio de sesión conectado a una base de datos, utilizando tecnologías web como HTML, PHP y SQL. Un sistema de autenticación permite comprobar si las credenciales introducidas por un usuario son correctas antes de permitir el acceso a una aplicación. El objetivo de esta práctica es comprender cómo funciona el proceso de verificación de usuarios, desde el envío de datos a través de un formulario hasta la comprobación en la base de datos y la gestión de sesiones para controlar el acceso a las páginas protegidas.

El sistema está compuesto por varios archivos que trabajan de forma conjunta para permitir el inicio de sesión y controlar el acceso a la aplicación.

### Base de datos y usuario
Se crea una base de datos llamada superaplicacion, que contiene una tabla llamada usuarios, donde se almacenan las credenciales y datos personales de los usuarios. Además, se crea un usuario de base de datos con los permisos necesarios para acceder a dicha base.

La tabla usuarios contiene los siguientes campos:
- id
- usuario
- contrasena
- nombrecompleto
- email
- creado_en

Esta tabla almacena la información necesaria para validar el inicio de sesión.

#### Formulario de inicio de sesión (login.html):
El archivo login.html contiene un formulario que permite al usuario introducir su nombre de usuario y contraseña. Este formulario envía los datos mediante el método POST al archivo procesa.php, que se encarga de procesar la autenticación.

#### Procesamiento del inicio de sesión (procesa.php):
El archivo procesa.php establece la conexión con la base de datos y ejecuta una consulta SQL que busca un usuario cuyo nombre y contraseña coincidan con los datos introducidos en el formulario. Si existe una coincidencia, se inicia una sesión y se redirige al usuario a la página de éxito. En caso contrario, se vuelve a la página de login.

#### Control de acceso (exito.php):
El archivo exito.php comprueba si existe una sesión activa. Si el usuario no ha iniciado sesión correctamente, se bloquea el acceso mostrando un mensaje de error. Si la sesión existe, se muestra un mensaje confirmando que el acceso ha sido correcto.

#### Diagrama del sistema:
El diagrama proporcionado representa visualmente el flujo del sistema:
- Login > Comprobación
- Si es correcto > Éxito > Panel
- Si es incorrecto > No éxito > Login

Este diagrama ayuda a entender la arquitectura general del sistema y el recorrido que siguen los datos durante el proceso de autenticación.


---
A continuación se describen los pasos realizados para implementar y comprobar el funcionamiento del sistema.

### Creación de la base de datos y la tabla de usuarios
```
CREATE DATABASE IF NOT EXISTS superaplicacion
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE superaplicacion;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    nombrecompleto VARCHAR(150) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Inserción de usuarios de prueba
```
INSERT INTO usuarios (usuario, contrasena, nombrecompleto, email)
VALUES
('jlopez', '1234segura', 'Juan López Martínez', 'juan.lopez@example.com'),
('mgarcia', 'clave2025', 'María García Sánchez', 'maria.garcia@example.com');
```

#### Comprobación exitosa
Se ejecuta la consulta con las credenciales correctas:
```
SELECT *
FROM usuarios
WHERE usuario = 'jlopez'
AND contrasena = '1234segura';
```
El resultado devuelve un registro, lo que indica que el inicio de sesión es válido.

#### Comprobación fallida
Se ejecuta la consulta con una contraseña incorrecta:
```
SELECT *
FROM usuarios
WHERE usuario = 'jlopez'
AND contrasena = '1234seguraZ';
```
En este caso no se obtiene ningún resultado, por lo que el sistema detecta un intento de acceso fallido.

Flujo completo del sistema:
1.-El usuario introduce sus datos en login.html.
2.-Los datos se envían a procesa.php.
3.-Se consulta la base de datos.
4.-Si las credenciales son correctas, se crea una sesión y se redirige a exito.php.
5.-Si las credenciales son incorrectas, se vuelve al formulario de login.

---
Este ejercicio permite comprender de forma práctica cómo funciona un sistema de autenticación de usuarios basado en una base de datos. A través de la creación de la base de datos, el diseño del formulario, el procesamiento de datos con PHP y la validación mediante consultas SQL, se refuerza el concepto de control de acceso y gestión de sesiones. Este tipo de sistemas es fundamental en cualquier aplicación web que requiera identificar a sus usuarios, proteger información sensible y garantizar un acceso seguro. Además, los conocimientos adquiridos en esta práctica pueden aplicarse directamente en proyectos reales como plataformas educativas, tiendas online o sistemas de gestión empresarial.
