-- crea usuario nuevo con contraseña
CREATE USER 
'portafolio'@'localhost' 
IDENTIFIED  BY 'Portafolio123$';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'portafolio'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'portafolio'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `portafolio`.* 
TO 'portafolio'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
