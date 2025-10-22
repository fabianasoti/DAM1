CREATE VIEW personas_correos AS

SELECT
personas.identificador, -- Por si quiero que aparezca el identificador de la persona
emails.direccion,
personas.nombre,
personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;

SELECT * FROM personas_correos; -- Ahora se comporta como una tabla, pero es solo de lectura
+---------------+------------------+------------------+-----------+
| identificador | direccion        | nombre           | apellidos |
+---------------+------------------+------------------+-----------+
|             1 | info@fabiana.com | Fabiana Victoria | Sotillo   |
|             1 | fabiana@info.com | Fabiana Victoria | Sotillo   |
|             1 | f@biana.com      | Fabiana Victoria | Sotillo   |
+---------------+------------------+------------------+-----------+

-- Ahora se ve así 
