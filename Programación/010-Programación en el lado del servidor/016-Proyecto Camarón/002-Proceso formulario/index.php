<!doctype html>
<html lang="es">
	<head>
  	<title>Camaron viviendas</title>
    <meta charset="utf-8">
    <style>
  /* Reset & Basics */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
  }

  body {
    background: #f5f5f5;
    color: #333;
    line-height: 1.6;
  }

  header {
    background: #003366;
    color: #fff;
    padding: 20px;
    text-align: center;
  }

  nav {
    background: #ffffff;
    padding: 15px;
    border-bottom: 1px solid #ddd;
    display: flex;
    justify-content: center;
  }

  nav form select,
  nav form input[type="submit"] {
    padding: 8px 12px;
    font-size: 14px;
    margin-right: 10px;
  }

  nav form input[type="submit"] {
    cursor: pointer;
    background: #003366;
    border: none;
    color: #fff;
    border-radius: 3px;
  }

  main {
    max-width: 900px;
    margin: 30px auto;
    padding: 0 15px;
  }

  article {
    background: #fff;
    padding: 20px;
    margin-bottom: 15px;
    border-radius: 5px;
    border: 1px solid #ddd;
  }

  article h3 {
    margin-bottom: 10px;
    color: #003366;
  }

  article p {
    margin: 4px 0;
  }

  footer {
    text-align: center;
    padding: 20px;
    margin-top: 40px;
    color: #666;
    font-size: 14px;
  }
</style>
  </head>
  <body>
  	<header><h1>Camarón viviendas</h1></header>
  	<nav>
  	  <form action="?" method="POST">
  	    <select name="localidad">
  	      <option>Selecciona una localidad...</option>
  	        <option value="Valencia">Valencia</option>
            <option value="Alboraya">Alboraya</option>
            <option value="Torrent">Torrent</option>
            <option value="Gandía">Gandía</option>
            <option value="Sagunto">Sagunto</option>
            <option value="Paterna">Paterna</option>
            <option value="Burjassot">Burjassot</option>
            <option value="Xàtiva">Xàtiva</option>
            <option value="Cullera">Cullera</option>
  	    </select>
  	    <input type="submit">
  	  </form>
  	</nav>
  	<main>
  	  <section>
  	    <?php
          $host = "localhost";
          $user = "camaron";
          $pass = "Camaron123$";
          $db   = "camaron";

          $conexion = new mysqli($host, $user, $pass, $db);
          $resultado = $conexion->query("
            SELECT * FROM viviendas WHERE localidad = '".$_POST['localidad']."';
          ");
          while ($fila = $resultado->fetch_assoc()) {
            echo '
            	<article>
              	<h3>'.$fila['localidad'].'</h3>
                <p>'.$fila['precio'].'</p>
                <p>'.$fila['metroscuadrados'].'</p>
                <p>'.$fila['aniodeconstruccion'].'</p>
                <p>'.$fila['direccion'].'</p>
                <p>'.$fila['altura'].'</p>
                <p>'.$fila['tipodevivienda'].'</p>
                <p>'.$fila['descripcion'].'</p>
                <p>'.$fila['estado'].'</p>
                <p>'.$fila['banios'].'</p>
                <p>'.$fila['habitaciones'].'</p>
                <p>'.$fila['teniente'].'</p>
              </article>
            ';
          }
    		?>
  	  </section>
  	</main>
  	<footer>(c) 2026 No me puedo creer que este proyecto se llame Camarón xd</footer>
  </body>
</html>
