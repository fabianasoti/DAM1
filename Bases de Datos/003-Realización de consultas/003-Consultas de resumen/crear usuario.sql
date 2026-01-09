CREATE USER
'clientes'@'localhost'
IDENTIFIED BY 'Clientes123$';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'clientes'@'localhost';
-- [tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len

-- quitale todos los límites que tenga
ALTER USER 'clientes'@'localhost'
REQUIRE NONE
WITH MAX_QUERIES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 0
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON clientes.*
TO 'clientes'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
