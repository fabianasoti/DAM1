<!doctype html>
<html lang="es">
  <head>
    <title>Camaron viviendas</title>
    <meta charset="utf-8">
    <style>
      /* Reset & Basics */
      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: Arial, Helvetica, sans-serif;
      }

      body {
        background: #f5f5f5;
        color: #333;
        line-height: 1.6;
      }

      header, footer {
        background: #003366;     /* kept original color */
        color: #fff;
        text-align: center;
        padding: 1rem;
      }

      nav {
        background: #ffffff;
        padding: 1rem;
        border-bottom: 1px solid #ddd;
      }

      nav form {
        max-width: 600px;
        margin: auto;
        display: flex;
        gap: 0.5rem;
      }

      select, input[type="submit"] {
        padding: 0.5rem;
        font-size: 1rem;
      }

      select {
        flex: 1;
      }

      input[type="submit"] {
        background: #003366;      /* original color */
        border: none;
        color: #fff;
        cursor: pointer;
      }

      input[type="submit"]:hover {
        background: #00264d;      /* darker version of original color */
      }

      main {
        max-width: 1200px;
        margin: 2rem auto;
        padding: 0 1rem;
      }

      /* Grid layout you added */
      section {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 1rem;
      }

      article {
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 5px;       /* kept original smooth design */
        padding: 1rem;
      }

      article h3 {
        margin-bottom: 0.5rem;
        color: #003366;           /* original highlight color */
      }

      article p {
        font-size: 0.9rem;
        margin: 0.2rem 0;
      }

      footer {
        font-size: 0.85rem;
        margin-top: 2rem;
      }
    </style>
  </head>

  <body>
    <header>
      <h1>Camarón viviendas</h1>
    </header>

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

        <input type="number" name="precio_minimo" value=0 min=0>
        <input type="number" name="precio_maximo" value=1000000000 min=0>
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
            SELECT * FROM viviendas 
            WHERE 
            localidad LIKE '%".$_POST['localidad']."%'
            AND precio > ".$_POST['precio_minimo']."
            AND precio < ".$_POST['precio_maximo']."
            ;
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

    <footer>(c) 2026 No me puedo creer que este proyecto se llame Camarón</footer>
  </body>
</html>
