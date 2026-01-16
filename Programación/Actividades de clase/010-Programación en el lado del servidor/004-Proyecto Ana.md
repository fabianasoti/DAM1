En este ejercicio se amplía el desarrollo de un mini intérprete de Python utilizando Flask, integrando una interfaz web que permite a los usuarios escribir, compilar y ejecutar código Python de forma segura y controlada. El proyecto se contextualiza dentro de un entorno creativo inspirado en el arte latte y el crocheting, dos hobbies que fomentan la precisión, la creatividad y la atención al detalle, valores que también son fundamentales en la programación. A través de este enfoque, se busca aplicar los conocimientos adquiridos en programación web y backend para crear una herramienta interactiva que permita experimentar con código Python desde el navegador.

El objetivo principal es reforzar el uso de endpoints en Flask, la gestión de sesiones y la ejecución de procesos externos mediante Python, comprendiendo cómo se comunican el frontend y el backend en una aplicación web.

---
El sistema se compone de dos partes principales: una interfaz web y un backend en Flask.

En primer lugar, se crea un archivo HTML denominado 002-front.html, que actúa como interfaz del mini intérprete. Este archivo incluye un editor de texto donde el usuario puede escribir código Python, un botón para compilar y una ventana de terminal donde se muestra el resultado de la ejecución. La interfaz simula una pequeña consola, ofreciendo una experiencia visual sencilla y clara.

En el backend, se modifica el archivo 010-mejoras.py para añadir nuevos endpoints que permitan gestionar sesiones de ejecución de Python. Para ello, se importan librerías estándar como subprocess, threading, queue, uuid, os y tempfile, que permiten ejecutar código en procesos independientes y controlar su salida.

Se define una clase llamada PythonSession, cuya función es ejecutar el código Python en un proceso separado. Esta clase incluye métodos internos para leer la salida del proceso en segundo plano, escribir código en la sesión activa, recuperar todo el output generado y comprobar si la sesión sigue en ejecución.

Además, se implementan tres nuevos endpoints en Flask:

api_start, que inicia una nueva sesión de ejecución.

api_write, que envía código Python a la sesión activa.

api_read, que recupera la salida del intérprete y el estado del proceso.

Gracias a esta arquitectura, cada usuario puede ejecutar su propio código Python en un entorno aislado, manteniendo la seguridad y estabilidad del servidor.

---
Interfaz de usuario (002-front.html):

La interfaz permite al usuario escribir código Python en un editor visual, pulsar el botón “Compilar” y ver el resultado en la terminal integrada. El diseño imita una pequeña ventana de programación, facilitando la interacción.

Funcionamiento del sistema:

1. El usuario accede a la interfaz web.

2. Escribe código Python en el editor.

3. Pulsa el botón “Compilar”.

4. El sistema inicia una sesión mediante el endpoint api_start.

5. El código se envía al servidor con api_write.

6. El resultado se recupera con api_read y se muestra en la terminal.

De esta forma, el usuario puede probar fragmentos de código Python de manera inmediata, igual que si estuviera usando una pequeña consola interactiva.

- Ejemplo de uso

El usuario puede escribir en el editor:
```
print("Hola desde el mini intérprete Python")
```

Al pulsar “Compilar”, el sistema ejecuta el código en el servidor y muestra en la terminal:
```
Hola desde el mini intérprete Python
```

Esto demuestra que el intérprete funciona correctamente y que los endpoints gestionan adecuadamente la comunicación entre el navegador y el servidor.

---
El sistema permite crear sesiones independientes de ejecución de Python, escribir código desde la interfaz web y mostrar el resultado en tiempo real. Los endpoints funcionan correctamente y la ejecución se realiza en procesos separados, evitando bloqueos y manteniendo la seguridad del entorno.

Este ejercicio ha permitido aplicar de forma práctica los conceptos aprendidos en clase sobre Flask, endpoints, ejecución de procesos y comunicación entre frontend y backend.

El desarrollo de este mini intérprete refuerza la comprensión del funcionamiento interno de las aplicaciones web dinámicas y sienta las bases para proyectos más complejos, como plataformas educativas interactivas o entornos de programación online. En el futuro, esta aplicación podría mejorarse añadiendo autenticación de usuarios, historial de sesiones o soporte para múltiples lenguajes, ampliando así los conocimientos adquiridos en esta unidad.
