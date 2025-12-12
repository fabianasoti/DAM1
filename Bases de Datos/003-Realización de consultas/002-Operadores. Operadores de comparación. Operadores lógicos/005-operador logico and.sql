-- sudo mysql -u root -p

USE clientes;

SELECT
nombre,
apellidos,
edad,
edad < 30 AS 'Menor de 30 años',
edad >= 30 && edad < 40 AS 'Entre 30 y 40 años',
edad > 40 AS 'Mayor de 40 años'
FROM clientes;

+----------+------------+------+-------------------+---------------------+-------------------+
| nombre   | apellidos  | edad | Menor de 30 años  | Entre 30 y 40 años  | Mayor de 40 años  |
+----------+------------+------+-------------------+---------------------+-------------------+
| Juan     | Lopez      |   45 |                 0 |                   0 |                 1 |
| Javier   | Martinez   |   46 |                 0 |                   0 |                 1 |
| Ana      | Sánchez    |   34 |                 0 |                   1 |                 0 |
| María    | Gómez      |   29 |                 1 |                   0 |                 0 |
| Luis     | Fernández  |   51 |                 0 |                   0 |                 1 |
| Carmen   | Ruiz       |   38 |                 0 |                   1 |                 0 |
| Pablo    | Hernández  |   27 |                 1 |                   0 |                 0 |
| Elena    | Jiménez    |   42 |                 0 |                   0 |                 1 |
| Sergio   | Álvarez    |   33 |                 0 |                   1 |                 0 |
| Laura    | Moreno     |   25 |                 1 |                   0 |                 0 |
| Raúl     | Muñoz      |   48 |                 0 |                   0 |                 1 |
| Isabel   | Romero     |   36 |                 0 |                   1 |                 0 |
| David    | Navarro    |   31 |                 0 |                   1 |                 0 |
| Patricia | Torres     |   40 |                 0 |                   0 |                 0 |
| Alberto  | Domínguez  |   53 |                 0 |                   0 |                 1 |
| Cristina | Vázquez    |   30 |                 0 |                   1 |                 0 |
| Rubén    | Ramos      |   28 |                 1 |                   0 |                 0 |
| Beatriz  | Gil        |   44 |                 0 |                   0 |                 1 |
| Jorge    | Castro     |   39 |                 0 |                   1 |                 0 |
| Natalia  | Ortiz      |   26 |                 1 |                   0 |                 0 |
| Óscar    | Rubio      |   50 |                 0 |                   0 |                 1 |
| Silvia   | Molina     |   32 |                 0 |                   1 |                 0 |
| Víctor   | Delgado    |   41 |                 0 |                   0 |                 1 |
| Rocío    | Cabrera    |   37 |                 0 |                   1 |                 0 |
| Héctor   | Santos     |   35 |                 0 |                   1 |                 0 |
| Lucía    | Iglesias   |   24 |                 1 |                   0 |                 0 |
| Andrés   | Cortés     |   47 |                 0 |                   0 |                 1 |
| Marta    | Peña       |   28 |                 1 |                   0 |                 0 |
| Tomás    | Flores     |   52 |                 0 |                   0 |                 1 |
| Noelia   | Cano       |   33 |                 0 |                   1 |                 0 |
| Gonzalo  | León       |   45 |                 0 |                   0 |                 1 |
| Irene    | Serrano    |   27 |                 1 |                   0 |                 0 |
+----------+------------+------+-------------------+---------------------+-------------------+

