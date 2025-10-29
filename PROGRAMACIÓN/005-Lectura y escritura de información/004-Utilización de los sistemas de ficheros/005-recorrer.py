import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

suma = 0

for directorio,carpetas,archivo in os.walk(carpeta):
    print(directorio)
    print(carpetas)
    print(archivo)
  
