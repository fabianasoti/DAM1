<!doctype html>
<html lang="es">
  <head>
    <title>Tienda</title>
    <meta name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
      /* ===== Refined Mobile-first Enhancements ===== */
@media (max-width: 768px){

  body{
    font-size:16px;
    background:#fafafa;
    color:#222;
  }

  header{
    padding:14px 10px;background:black;color:white;padding:10px;text-align:center;
  }

  header h1{
    margin:0;
    font-size:1.5rem;
    font-weight:700;
  }

  main{
    padding:12px;
  }

  section{
    margin-bottom:24px;
  }

  h3{
    margin-bottom:12px;
    font-size:1.25rem;
    text-align:center;
    font-weight:600;
  }

  /* Product list */
  #productos > div{
    display:flex;
    flex-direction:column;
    gap:14px;
  }

  article{
    border:1px solid #e3e3e3;
    background:#fff;
    padding:14px 16px;
    border-radius:10px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
  }

  article h4{
    margin:0;
    font-size:1.05rem;
    font-weight:500;
  }

  button{
    padding:12px 18px;
    font-size:1rem;
    border:none;
    border-radius:8px;
    background:#000;
    color:#fff;
    cursor:pointer;
    transition:transform .08s ease, opacity .1s;
    touch-action:manipulation;
  }

  button:active{
    transform:scale(0.95);
    opacity:0.85;
  }

  /* Client data form */
  section:last-of-type > div{
    display:flex;
    flex-direction:column;
    gap:12px;
    background:#fff;
    padding:16px;
    border-radius:12px;
    border:1px solid #e3e3e3;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
  }

  input{
    padding:12px;
    font-size:1rem;
    border-radius:8px;
    border:1px solid #ccc;
    width:100%;
    box-sizing:border-box;
    background:#fdfdfd;
  }

  input:focus{
    outline:none;
    border-color:#000;
    background:#fff;
  }

  #enviar{
    margin-top:6px;
    padding:14px;
    text-align:center;
    background:#000;
    color:#fff;
    border-radius:10px;
    font-size:1.05rem;
    cursor:pointer;
    user-select:none;
    transition:transform .08s ease, opacity .1s;
  }

  #enviar:active{
    transform:scale(0.97);
    opacity:0.85;
  }

  footer{
    font-size:0.85rem;
    padding:10px;
    background:#000;
    color:#fff;
    text-align:center;
  }
}

    </style>
    <meta charset="utf-8">
  </head>
  <body>
    <header>
      <h1>Microtienda</h1>
    </header>
    <main>
      <section id="productos">
        <h3>Productos</h3>
        <div>
          <?php
            $host = "localhost";
            $user = "microtienda";
            $pass = "Microtienda123$";
            $db   = "microtienda";
            $conexion = new mysqli($host, $user, $pass, $db);
            $sql = "SELECT * FROM productos;";
            $resultado = $conexion->query($sql);
            while ($fila = $resultado->fetch_assoc()) {
          ?>
            <article>
              <h4><?= $fila['nombre'] ?></h4>
              <button nombre="<?= $fila['nombre'] ?>"><?= $fila['precio'] ?>€</button>
            </article>
          <?php }?>
        </div>
      </section>
      <section>
        <h3>Datos de cliente</h3>
        <div>
          <input type="text" id="nombre" placeholder="Nombre">
          <input type="text" id="apellidos" placeholder="Apellidos">
          <input type="text" id="email" placeholder="Email">
          <div id="enviar">Enviar pedido</div>
        </div>
      </section>
    </main>
    <footer>
      (c) 2026 Fabiana Victoria Sotillo
    </footer>
  </body>
  <script>
    var fecha = new Date();
    var pedido = {
    	cliente:{},
      productos:[],
      pedido:{
        "numero":Date.now(),
        "fecha":fecha.getFullYear()+"-"+(fecha.getMonth()+1)+"-"+fecha.getDate()
      }
    };
    /////// Atrapa productos y los mete en el carro
    let botones = document.querySelectorAll("button");
    botones.forEach(function(boton){
    	boton.onclick = function(){
      	pedido.productos.push({
          "nombre":this.getAttribute("nombre"),
        	"precio":this.textContent
        })
        console.log(pedido)
      }
    })
    /////// Atrapa los datos del cliente
    let boton_enviar = document.querySelector("#enviar");
    boton_enviar.onclick = function(){
      let nombre_cliente = document.querySelector("#nombre").value;
      let apellidos_cliente = document.querySelector("#apellidos").value;
      let email_cliente = document.querySelector("#email").value;
      pedido.cliente = {
        "nombre":nombre_cliente,
        "apellidos":apellidos_cliente,
        "email":email_cliente
      }
      console.log(pedido)
    }
  </script>
</html>
