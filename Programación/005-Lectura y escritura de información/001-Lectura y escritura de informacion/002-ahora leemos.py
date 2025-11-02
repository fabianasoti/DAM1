archivo = open("clientes.txt", 'r')     # R = read

contenido = archivo.readline()
#   También existe archivo.readlines()

print(contenido)

archivo.close()
