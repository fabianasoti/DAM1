SELECT * FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;

-- Selecciona email pero crúzalo con personas
