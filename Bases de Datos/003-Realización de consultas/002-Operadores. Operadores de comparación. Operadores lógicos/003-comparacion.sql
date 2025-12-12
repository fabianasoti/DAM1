-- sudo mysql -u root -p

USE clientes;

SELECT 
nombre,
apellidos,
edad,
edad < 30
FROM clientes;

+----------+------------+------+-----------+
| nombre   | apellidos  | edad | edad < 30 |
+----------+------------+------+-----------+
| Juan     | Lopez      |   45 |         0 |
| Javier   | Martinez   |   46 |         0 |
| Ana      | Sánchez    |   34 |         0 |
| María    | Gómez      |   29 |         1 |
| Luis     | Fernández  |   51 |         0 |
| Carmen   | Ruiz       |   38 |         0 |
| Pablo    | Hernández  |   27 |         1 |
| Elena    | Jiménez    |   42 |         0 |
| Sergio   | Álvarez    |   33 |         0 |
| Laura    | Moreno     |   25 |         1 |
| Raúl     | Muñoz      |   48 |         0 |
| Isabel   | Romero     |   36 |         0 |
| David    | Navarro    |   31 |         0 |
| Patricia | Torres     |   40 |         0 |
| Alberto  | Domínguez  |   53 |         0 |
| Cristina | Vázquez    |   30 |         0 |
| Rubén    | Ramos      |   28 |         1 |
| Beatriz  | Gil        |   44 |         0 |
| Jorge    | Castro     |   39 |         0 |
| Natalia  | Ortiz      |   26 |         1 |
| Óscar    | Rubio      |   50 |         0 |
| Silvia   | Molina     |   32 |         0 |
| Víctor   | Delgado    |   41 |         0 |
| Rocío    | Cabrera    |   37 |         0 |
| Héctor   | Santos     |   35 |         0 |
| Lucía    | Iglesias   |   24 |         1 |
| Andrés   | Cortés     |   47 |         0 |
| Marta    | Peña       |   28 |         1 |
| Tomás    | Flores     |   52 |         0 |
| Noelia   | Cano       |   33 |         0 |
| Gonzalo  | León       |   45 |         0 |
| Irene    | Serrano    |   27 |         1 |
+----------+------------+------+-----------+

