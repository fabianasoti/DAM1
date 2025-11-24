En terminal:

sudo apt install apache2

De ahí en adelnate, todos los archivos que hagáis tendrán que estar en:
/var/www/html

Liberación de permisos:

cd /var/www
sudo chmod 777 -R html

sudo = El super usuario va a hacer algo
chmod = cambiamos permisos de archivo y carpeta
777 = los tres grupos pueden hacer de todo
-R = recursivo (se aplica a todo el contenido)
html = la carpeta de destino

sudo apt install php
