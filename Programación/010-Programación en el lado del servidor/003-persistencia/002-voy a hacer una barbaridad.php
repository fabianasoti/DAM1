Terminal:

sudo chmod 777 -R /var/www/html/DAM1

sudo = Realizo acción como administrador

chmod = cambio permisos

777 = le doy permiso a todo el mundo

-R = Lo quiero aplicar recursivo (a todo el contenido)

/var/www.... = la carpeta afectada

En el sistema de permisos UNIX (Linux, macOS)

1 número para el usuario
1 número para el grupo al que pertenece el usuario
1 número para todo el resto

0 = ningún permiso
1 = solo ejecutar
2 = solo escribir
3 = escribir y ejecutar
4 = solo leer
5 = leer y ejecutar
6 = leer y escribir
7 = leer, escribir y ejecutar

777 = permisible en tu máquina, no recomendable en producción
usuario leer, escribir y ejecutar
grupo leer, escribir y ejecutar
todo el mundo leer, escribir y ejecutar

755 = posible para produccion
usuario leer, escribir y ejecutar
grupo leer, escribir y ejecutar
todo el mundo leer, escribir y ejecutar

644 = más restrictivo para producción
usuario leer y escribir
grupo solo leer
todo el mundo solo leer
