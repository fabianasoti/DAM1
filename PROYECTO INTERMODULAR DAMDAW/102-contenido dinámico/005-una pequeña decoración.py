import json

archivo = open("blog.json", 'r')

contenido = json.load(archivo)

for linea in contenido:
    print("========ARTÍCULO========")
    print(linea['titulo'])
    print(linea['fecha'])
    print(linea['autor'])
    print(linea['contenido'])
    print("========================")
    print("")
