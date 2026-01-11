# Implementación y validación de un sistema de inicio de sesión con base de datos

El presente ejercicio tiene como objetivo aplicar los conceptos fundamentales relacionados con la validación de usuarios mediante bases de datos, comprendiendo el funcionamiento de un sistema de inicio de sesión a través de consultas SQL y scripts en PHP. A partir de la creación de una base de datos, la configuración de un usuario, la comprobación de credenciales correctas e incorrectas y la integración con un formulario web, se busca entender cómo se gestionan los accesos a un sistema y cómo se valida la autenticación de usuarios en aplicaciones web.

---
En esta actividad se comienza configurando la base de datos y el usuario necesarios para almacenar la información de acceso. Posteriormente, se ejecutan consultas SQL que permiten comprobar tanto un inicio de sesión exitoso como uno fallido, lo que facilita la comprensión del proceso de validación de credenciales.

A continuación, se revisan los archivos PHP encargados de procesar las solicitudes del formulario de inicio de sesión y de verificar si el usuario ha sido autenticado correctamente. De forma complementaria, se analiza el formulario HTML que permite introducir los datos de acceso y enviarlos al servidor.

Finalmente, se revisan los archivos del diagrama exportado, los cuales representan visualmente la arquitectura general del sistema de inicio de sesión, permitiendo comprender de forma gráfica la estructura y el flujo de funcionamiento del proyecto.

---
Aplicación práctica
1. Creación de la base de datos y del usuario

Se ejecutan los scripts 001-creamos base de datos.sql y 002-creamos usuario.sql para crear la base de datos y el usuario necesarios para el sistema de inicio de sesión. Estos scripts permiten configurar el entorno donde se almacenarán los datos de los usuarios y desde donde se realizarán las comprobaciones de acceso.

Este paso es fundamental para garantizar que el sistema dispone de una estructura adecuada para gestionar la información de autenticación.

2. Comprobación de inicio de sesión exitoso

Se utiliza el script 003-comprobacion exitosa.sql para verificar que la consulta funciona correctamente cuando se introducen las credenciales válidas:

Usuario: jlopez

Contraseña: 1234segura

La ejecución de esta consulta permite comprobar que el sistema es capaz de localizar al usuario en la base de datos y validar correctamente sus datos de acceso.

3. Comprobación de inicio de sesión fallido

Se ejecuta el script 004-comprobacion fallida.sql utilizando credenciales incorrectas:

Usuario: jlopez

Contraseña: 1234seguraZ

Esta comprobación permite observar cómo el sistema gestiona un intento de acceso erróneo, devolviendo un resultado vacío o un mensaje de error, lo que demuestra que la validación se realiza de forma correcta.

4. Procesamiento de datos con procesa.php

Se revisa el archivo procesa.php, el cual se encarga de establecer la conexión con la base de datos y procesar los datos enviados desde el formulario de inicio de sesión. Este script recibe el usuario y la contraseña introducidos, ejecuta la consulta correspondiente y envía el resultado al sistema de validación.

Este archivo constituye el núcleo lógico del sistema de autenticación.

5. Formulario de inicio de sesión con login.html

Se analiza el archivo login.html, que contiene el formulario donde el usuario introduce sus credenciales. El formulario está configurado para enviar los datos al archivo procesa.php mediante el método correspondiente al enviar la información.

Este archivo representa la interfaz de acceso al sistema.

6. Validación final con exito.php

El archivo exito.php contiene la lógica que comprueba si el usuario ha iniciado sesión correctamente y muestra un mensaje de éxito en caso afirmativo. Este script se encarga de interpretar el resultado devuelto por procesa.php y determinar si el acceso es válido o no.

7. Revisión del diagrama exportado

Se revisan los archivos diagrama.html, diagrama.svg y diagrama.json, los cuales representan de forma visual el diseño del sistema de inicio de sesión. Estos diagramas permiten comprender la arquitectura general del proyecto, así como la relación entre los distintos componentes.

---
Como resultado del ejercicio, se obtiene un sistema funcional de inicio de sesión que permite validar credenciales almacenadas en una base de datos. El sistema es capaz de gestionar tanto accesos correctos como intentos fallidos, mostrando el comportamiento esperado en cada caso.

En este ejercicio se han aplicado los conceptos fundamentales de autenticación de usuarios mediante bases de datos, integrando consultas SQL, scripts en PHP y formularios HTML para construir un sistema completo de inicio de sesión. Esta práctica permite comprender cómo se validan credenciales, cómo se gestionan accesos correctos e incorrectos y cómo se estructura una aplicación web segura desde el punto de vista de la autenticación. Asimismo, refuerza el uso de bases de datos y programación web como herramientas esenciales en el desarrollo de sistemas de información modernos.
