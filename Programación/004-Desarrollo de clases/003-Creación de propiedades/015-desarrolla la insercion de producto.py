'''
Aplicacion de gestión de productos
(c) 2025 Fabiana Sotillo
Esta aplicación gestiona productos
'''
#En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0

# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v01. Fabiana")
# Metemos al usuario en un bucle infinito
while True:
    # Le mostramos al usuario las opciones que tiene
    print("Selecciona una opción:")
    print("1.-Crear un nuevo producto")
    print("2.-Listar productos")
    print("3.-Actualizar productos")
    print("4.-Eliminar productos")
    opcion = int(input("Escoge tu opción: "))
    # En función de la opción que coja el usuario
    if opcion == 1:
        # O bien creamos un nuevo producto
        print("Creamos un nuevo producto")
        producto = Producto()   # Creo una nueva instancia de clase
        producto.nombre = input("Introduce el nombre del producto: ")   # Escribo la propiedad
        producto.precio = input("Introduce el precio del producto: ")   # Escribo la propiedadç
        productos.append(producto)  # Y añado el producto a la lista de productos
    elif opcion == 2:
        # O bien listamos los productos
        print("Vamos a listar los productos")
    elif opcion == 3:
        # O bien actualizamos los productos
        print("Vamos a actualizar los productos")
    elif opcion == 4:
        # O bien eliminamos los productos
        print("Vamos a eliminar los productos")
    # Y volvemos a repetir

