CREATE USER IF NOT EXISTS
'composiciones4'@'localhost' 
IDENTIFIED  BY 'ComposicionS14T325342523$';

GRANT USAGE ON *.* TO 'composiciones4'@'localhost';

ALTER USER 'composiciones4'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON composiciones.* 
TO 'composiciones4'@'localhost';

FLUSH PRIVILEGES;
