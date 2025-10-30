-- Paso 1: Cambiar el tipo de columna
ALTER TABLE emails
MODIFY COLUMN persona INT;

-- Paso 2: Crear la foreign key
ALTER TABLE emails
ADD CONSTRAINT fk_emails_personas
FOREIGN KEY (persona) 
REFERENCES personas(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE emails								-- Altera la tabla de emails
ADD CONSTRAINT fk_emails_personas	-- Crea una restricción con este nombre
FOREIGN KEY (persona) -- Creamos una clave hacia persona
REFERENCES personas(identificador)		-- que referencia el identificador
ON DELETE CASCADE		-- cuando elimines, cascada
ON UPDATE CASCADE;		-- Cuando actualices, cascada


SHOW TABLES;
