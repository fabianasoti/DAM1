CREATE USER 
'el_jocarsa_noticias'@'localhost' 
IDENTIFIED  BY 'Periodico123$';

GRANT USAGE ON *.* TO 'el_jocarsa_noticias'@'localhost';

ALTER USER 'el_jocarsa_noticias'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON el_jocarsa_noticias.* 
TO 'el_jocarsa_noticias'@'localhost';

FLUSH PRIVILEGES;
