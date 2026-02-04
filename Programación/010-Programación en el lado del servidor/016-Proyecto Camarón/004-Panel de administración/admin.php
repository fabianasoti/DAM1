<?php
if(isset($_POST['localidad'])){
  $host = "localhost";
  $user = "camaron";
  $pass = "Camaron123$";
  $db   = "camaron";

  $conexion = new mysqli($host, $user, $pass, $db);
  $resultado = $conexion->query('
  	INSERT INTO viviendas 
    VALUES(
    	NULL,
      "'.@$_POST['localidad'].'",
      '.@$_POST['precio'].',
      '.@$_POST['metroscuadrados'].',
      '.@$_POST['aniodeconstruccion'].',
      "'.@$_POST['direccion'].'",
      '.@$_POST['altura'].',
      "'.@$_POST['tipodevivienda'].'",
      "'.@$_POST['descripcion'].'",
      "'.@$_POST['estado'].'",
      '.@$_POST['banios'].',
      '.@$_POST['habitaciones'].',
      "'.@$_POST['teniente'].'"
    )
  ;
  ');
  }
?>
<!doctype html>
<html>
	<head>
  	<style>
  /* Reset básico */
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Arial, Helvetica, sans-serif;
  }

  html, body {
    width: 100%;
    height: 100%;
  }

  body {
    display: flex;
    background: #f5f5f5;
    color: #333;
    line-height: 1.5;
  }

  /* NAV IZQUIERDA */
  nav {
    flex: 1;
    background: coral;
    color: white;
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 12px;
  }

  nav a {
    background: white;
    color: coral;
    padding: 10px;
    border-radius: 4px;
    text-decoration: none;
    font-weight: bold;
    border: 1px solid white;
    transition: 0.2s;
  }

  nav a:hover {
    background: #ffe1d6;
    border-color: #ffb79c;
  }

  /* MAIN */
  main {
    flex: 5;
    padding: 15px;
    display: flex;
    gap: 15px;
    align-items: flex-start;
  }

  /* TABLA */
  table {
    flex: 1;
    background: white;
    border-collapse: collapse;
    border: 2px solid coral;
    border-radius: 4px;
    overflow: hidden;
  }

  thead {
    background: coral;
    color: white;
  }

  th, td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    text-align: left;
    font-size: 0.95rem;
  }

  tr:hover td {
    background: #fff5f0;
  }

  /* FORMULARIO */
  form {
    flex: 1;
    background: white;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    border: 2px solid coral;
    border-radius: 4px;
  }

  form input {
    padding: 8px;
    border: 1px solid #bbb;
    border-radius: 4px;
    font-size: 0.95rem;
  }

  form input[type="submit"] {
    background: coral;
    color: white;
    border: none;
    cursor: pointer;
    font-weight: bold;
    transition: 0.2s;
  }

  form input[type="submit"]:hover {
    background: #d85430;
  }
</style>

  </head>
  <body>
  	<nav>
    	<a>Viviendas</a>
      <a>Imagenes</a>
      <a>Usuarios</a>
      <a>Propietarios</a>
      <a>Alquileres</a>
      <a>a</a>
      <a>b</a>
      <a>c</a>
      <a>d</a>
      <a>e</a>
    </nav>
    <main>
    	<table>
      	<thead>
        	<tr>
          	<th>localidad</th>
            <th>precio</th>
            <th>metroscuadrados</th>
            <th>aniodeconstruccion</th>
            <!--
            <th>direccion</th>
            <th>altura</th>
            <th>tipodevivienda</th>
            <th>descripcion</th>
            <th>estado</th>
            <th>banios</th>
            <th>habitaciones</th>
            <th>teniente</th>
            -->
          </tr>
        </thead>
        <tbody>
        	<?php
            $host = "localhost";
            $user = "camaron";
            $pass = "Camaron123$";
            $db   = "camaron";

            $conexion = new mysqli($host, $user, $pass, $db);
            $resultado = $conexion->query("
              SELECT * FROM viviendas 
              ;
            ");
            while ($fila = $resultado->fetch_assoc()) {
            	echo '<tr>
              	<td>'.$fila['localidad'].'</td>
                <td>'.$fila['precio'].'</td>
                <td>'.$fila['metroscuadrados'].'</td>
                <td>'.$fila['aniodeconstruccion'].'</td>
                
              </tr>';
              /*<td>'.$fila['direccion'].'</td>
                <td>'.$fila['altura'].'</td>
                <td>'.$fila['tipodevivienda'].'</td>
                <td>'.$fila['descripcion'].'</td>
                <td>'.$fila['estado'].'</td>
                <td>'.$fila['banios'].'</td>
                <td>'.$fila['habitaciones'].'</td>
                <td>'.$fila['teniente'].'</td> */
            }
        	?>
        </tbody>
      </table>
      <form action="?" method="POST">
      			<input name="localidad" placeholder="localidad">
            <input name="precio" placeholder="precio">
            <input name="metroscuadrados" placeholder="metroscuadrados">
            <input name="aniodeconstruccion" placeholder="aniodeconstruccion">
            <input name="direccion" placeholder="direccion">
            <input name="altura" placeholder="altura">
            <input name="tipodevivienda" placeholder="tipodevivienda">
            <input name="descripcion" placeholder="descripcion">
            <input name="estado" placeholder="estado">
            <input name="banios" placeholder="banios">
            <input name="habitaciones" placeholder="habitaciones">
            <input name="teniente" placeholder="teniente">
            <input type="submit">
      </form>
    </main>
  </body>
</html>
