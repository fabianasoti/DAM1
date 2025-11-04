import os	# Para crear y manipular archivos .zip
import zipfile	# Para trabajar con rutas y carpetas

origen = "archivos"	# Es la carpeta que queremos comprimir.
destino = "archivos.zip" # Es el nombre del archivo ZIP que se va a crear.

# zipfile.ZIP_DEFLATED → indica que se usará compresión (no solo almacenamiento).
#'w' → modo escritura (crea un ZIP nuevo).
archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)	
#	Recorremos la carpeta origen:
# Devuelve tres cosas en cada paso:
# directorio: la ruta actual.
# carpetas: las subcarpetas dentro de esa ruta.
# archivos: los nombres de los archivos dentro de esa ruta.
for directorio, carpetas, archivos in os.walk(origen):	# os.walk() recorre la carpeta origen y todas sus subcarpetas.
  for archivo in archivos:
    # rutaarchivo → ruta completa al archivo (por ejemplo "archivos/texto.txt").
    rutaarchivo = os.path.join(directorio, archivo)
    # rutarelativa → ruta dentro del ZIP (por ejemplo "texto.txt" o "subcarpeta/texto.txt").
    rutarelativa = os.path.relpath(rutaarchivo, origen)
    # archivozip.write() → agrega el archivo al ZIP.
    archivozip.write(rutaarchivo, rutarelativa)
    
archivozip.close()	# Siempre hay que cerrarlo para guardar los cambios correctamente.

# Resultado: Crea un único archivo llamado archivos.zip.
# Dentro de él está toda la estructura de la carpeta “archivos”.