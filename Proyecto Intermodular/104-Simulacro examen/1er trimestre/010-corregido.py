import mysql.connector                    # Importo el conector a base de datos
from flask import Flask                   # Importo la libreria Flask

conexion = mysql.connector.connect(
    host="localhost",      
    user="usuario1",    
    password="Portafolio123$",  
    database="portafolio"      
)                                          # Me conecto a la base de datos
                            
cursor = conexion.cursor()                # Creo un cursor
app = Flask(__name__)                     # Creo una aplicación Flask (web)

@app.route("/")                           # Atrapo la ruta raiz (/)
def holamundo():                          # Defino una funcion
    cursor.execute('''
        SELECT * FROM pieza_categoria;
    ''')                                  # Pido el contenido de la vista

    filas = cursor.fetchall()             # Lo guardo en una lista
    ######### AQUI PONGO EL INICIO HASTA EL MAIN
    cadena = '''
    <!doctype html>
<html lang="es">
  <head>
    <title>Fabiana Victoria Sotillo</title>
    <meta charset="utf-8">
    <!-- Etiquetas de posicionamiento -->
    <meta name="description" content="Web de Fabiana Victoria Sotillo Cuevas, estudiante de DAM, crochetera en su tiempo libre">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="programación,desarrollo,clave3,...">
    <meta name="author" content="Fabiana Victoria Sotillo">
    <link rel="icon" href="kermit cute.jpeg" type="image/jpeg">
    <meta property="og:title" content="Fabiana Victoria Sotillo">
    <meta property="og:description" content="Web de Fabiana Victoria Sotillo Cuevas, estudiante de DAM, crochetera en su tiempo libre">
    <meta property="og:image" content="kermit cute.jpeg">
    <meta property="og:url" content="https://fabianasotillo.com">
    <meta property="og:type" content="website">
    <style>
      @font-face{
          font-family: "ubuntu";
          src:url("BebasNeue-Regular.otf");
      }
      h1{
        color:MediumSlateBlue;
        font-family: "ubuntu";
      }
      h2,h3{
        color:MediumSlateBlue;
        font-family:monospace;
      }
      body{
        background:Lavender;
      }
      header,main,footer{
        width:750px;
        background:white;
        margin:auto;
        padding:20px;
      }
      #inicio img{
        width:100px;
      }
      .bloque{
        display:flex;
        gap:20px;
      }
      .bloque img{
        flex:1;
        width:50%;
        height:50%;
      }
      .bloque p{
        flex:1;
        font-size:10px;
        text-align:justify;
      }
      #diseño .bloque{
        flex-direction: row-reverse;
      }
      #contenedor_portafolio{
        display:grid;
        grid-template-columns:auto auto auto;
        gap:20px;
      }
      #contenedor_portafolio{
        width:100%;
      }
      form{
        display:flex;
        flex-direction:column;
        flex:1;
        gap:10px;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Fabiana Victoria Sotillo</h1>
      <h2>fabiana.victoria.sotillo@alu.ceacfp.es</h2>
    </header>
    <main>
    '''                               # Creo una cadena vacia
    ######### AQUI PONGO LO QUE SE REPITE
    for fila in filas:                        # Para cada elemento de la lista
        cadena += f'''
        <article>
            <p>{fila[4]}</p>
            <h4>{fila[0]}</h4>
            <p>{fila[1]}</p>
            <a href="{fila[3]}">Ver más</a>
            <img src="{fila[2]}">          
        </article>
        '''                                   # Añado el registro a la cadena
    ######### AQUI PONGO EL FINAL
    cadena += '''
    </main>
    <footer>
      <p>&copy; 2025 Fabiana Sotillo</p>
    </footer>
  </body>
</html>
    '''
    return cadena                             # Devuelvo la cadena como HTML en la web

if __name__ == "__main__":                # Si este es el archivo principal
    app.run(debug=True)                   # Ejecuta la web

