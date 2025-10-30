-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER
'susana'@'localhost'
IDENTIFIED BY 'F0nt4n3r0*';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'susana'@'localhost';
-- [tuservidor] == localhost

-- quitale todos los límites que tenga
ALTER USER 'susana'@'localhost'
REQUIRE NONE
WITH MAX_QUERIES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 0
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON empresadam.*
TO 'susana'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
