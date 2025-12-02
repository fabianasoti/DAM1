archivo = open("basededatos.txt","r")
lineas = archivo.readlines()
for linea in lineas:    # “Para cada elemento que hay dentro de colección, ejecuta el bloque de código.”
  print(linea)
archivo.close()
