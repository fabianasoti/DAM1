SELECT COUNT(color)
FROM productos; -- resumen
+--------------+
| COUNT(color) |
+--------------+
|           20 |
+--------------+

SELECT COUNT(color), color
FROM productos
GROUP BY color;
+--------------+-------------+
| COUNT(color) | color       |
+--------------+-------------+
|            1 | Blanco      |
|            1 | Rosa Pastel |
|            1 | Verde Claro |
|            1 | Rojo        |
|            1 | Azul Marino |
|            1 | Gris        |
|            1 | Beige       |
|            1 | Mostaza     |
|            1 | Lavanda     |
|            1 | Celeste     |
|            1 | Menta       |
|            1 | Arena       |
|            1 | Turquesa    |
|            1 | Crema       |
|            1 | Lila        |
|            1 | Rosa        |
|            1 | Terracota   |
|            1 | Verde Oliva |
|            1 | Perla       |
|            1 | Chocolate   |
+--------------+-------------+

