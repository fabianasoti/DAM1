<?php
// Datos en formato JSON
$jsonData = '[
    {"label": "Enero", "value": 30},
    {"label": "Febrero", "value": 55},
    {"label": "Marzo", "value": 80},
    {"label": "Abril", "value": 60},
    {"label": "Mayo", "value": 40},
    {"label": "Junio", "value": 90},
    {"label": "Julio", "value": 70}
]';

$data = json_decode($jsonData, true);

// Colores para cada barra
$colors = [
    "#e74c3c", // rojo
    "#f1c40f", // amarillo
    "#2ecc71", // verde
    "#3498db", // azul
    "#9b59b6", // morado
    "#e67e22", // naranja
    "#1abc9c"  // turquesa
];

// Configuración del SVG
$svgWidth = 52.916666;
$svgHeight = 52.916666;
$chartHeight = 45;
$originX = 4;
$originY = 50;

$barWidth = 3.8;
$gap = 3;

$maxValue = max(array_column($data, 'value'));
$scale = $chartHeight / $maxValue;
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gráfico SVG con PHP</title>
</head>
<body>

<svg width="200" height="200" viewBox="0 0 52.916665 52.916666"
     xmlns="http://www.w3.org/2000/svg">

    <!-- Ejes -->
    <path d="M 1.2,1.1 V 51.9 H 51.6"
          style="fill:none;stroke:black;stroke-width:1.2"/>

    <?php
    $x = $originX;
    $i = 0;

    foreach ($data as $item) {
        $value = $item['value'];
        $height = $value * $scale;
        $y = $originY - $height;

        // Color cíclico
        $color = $colors[$i % count($colors)];

        echo "
        <rect 
            x='{$x}'
            y='{$y}'
            width='{$barWidth}'
            height='{$height}'
            fill='{$color}'
            stroke='{$color}'
            stroke-width='1'
        />
        ";

        $x += $barWidth + $gap;
        $i++;
    }
    ?>

</svg>

</body>
</html>

