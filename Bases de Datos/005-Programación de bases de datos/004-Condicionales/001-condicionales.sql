DELIMITER //

CREATE PROCEDURE insertar()
BEGIN

    IF (SELECT COUNT(*) 
        FROM clientes 
        WHERE email='info@fabiana.com') = 0
    THEN
        INSERT INTO clientes
        VALUES(
            NULL,
            'Fabiana Victoria',
            'Sotillo',
            'info@fabiana.com',
            'La calle de Fabiana'
        );
    END IF;

END //

DELIMITER ;
