SELECT COUNT(color)
FROM productos; -- resumen

SELECT 
COUNT(color) AS numero,
color
FROM productos
GROUP BY color
ORDER BY color ASC;
+--------+-------------+
| numero | color       |
+--------+-------------+
|      1 | Arena       |
|      1 | Azul Marino |
|      1 | Beige       |
|      1 | Blanco      |
|      1 | Celeste     |
|      1 | Chocolate   |
|      1 | Crema       |
|      1 | Gris        |
|      1 | Lavanda     |
|      1 | Lila        |
|      1 | Menta       |
|      1 | Mostaza     |
|      1 | Perla       |
|      1 | Rojo        |
|      1 | Rosa        |
|      1 | Rosa Pastel |
|      1 | Terracota   |
|      1 | Turquesa    |
|      1 | Verde Claro |
|      1 | Verde Oliva |
+--------+-------------+

