import zipfile	# Para crear y manipular archivos .zip
import os # Para trabajar con rutas y carpetas

carpeta = "archivos"

for directorio, subcarpetas, archivos in os.walk(carpeta):
    for nombre_archivo in archivos: # Por cad archivo que encontramos, entramos a procesarlo individualmente
        # Creamos las rutas:
        origen = os.path.join(directorio, nombre_archivo) # el archivo original.
        destino = os.path.join(directorio, nombre_archivo + ".zip") # el nuevo archivo ZIP que se va a crear (con el mismo nombre, pero .zip al final).
        archivo =  zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED) # Se crea un archivo ZIP nuevo por cada archivo original.
        archivo.write(origen, arcname=nombre_archivo) # arcname indica cómo se llamará dentro del ZIP (solo el nombre, sin la ruta completa).

archivo.close()
