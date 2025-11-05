Simulacro de examen:
Problema (común a los exámenes): Hacer un portafolio, que tenga una parte visible al público general (web), y un panel de administración interna.

Paso 1: Hacer una base de datos del portafolio. 
Existen dos entidades: 
- Pieza (Identificador PK, titulo, descripción, imagen, url, id_categoria FK), 
- y Categoria (Identificador PK, titulo, descripción). 

Debe existir una FK entre Pieza y Categoría. Hacer un join entre las dos tablas y una vista (view) de ese JOIN.

Paso 2: Hacer una aplicación en Python-consola:
a) Mensaje de Bienvenida
b) Que presente opciones CRUD
c) Bucle infinito
d) Atrapar las opciones con if-elif
e) Para cada una de las opciones, ejecutar MySQL INSERT, SELECT, UPDATE, DELETE

Paso 3: Hacer un front simulado, del portafolio, en HTML y CSS
a) Crea una estructura HTML básica y legal
b) En body, crea header, main, footer
