import zipfile

origen = 'Crepusculo PDF.pdf'

destino = 'crepusculo comprimido.zip'

archivo = zipfile.ZipFile(destino, 'w', compression = zipfile.ZIP_DEFLATED)
archivo.write(origen)
