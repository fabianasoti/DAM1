git push origin main

fabiana@fabiana-VirtualBox:/var/www/html/pruebadam2026$ git push origin main
Username for 'https://github.com': fabianasoti
Password for 'https://fabianasoti@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Autenticación falló para 'https://github.com/fabianasoti/pruebadam2026/'

Vamos a crear un token de autenticación

Primero creamos el token:

https://github.com/settings/tokens
creamos token clásico
Seleccionamos todos los permisos

Mostrará un token que empezará por ghp_XXXXXXXXXXXXXXXXXX

Ahora lo introducimos en la terminal:
git config --global credential.helper store
