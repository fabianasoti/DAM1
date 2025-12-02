# Las propiedades son como las variables PERO dentro de una clase.
# Podemos crear tantas propiedades como queramos
# Arrays =  arreglos. Conjunto de cosas, listas.

class Cliente():
    def __init__(self):
        self.nombre = None # O le pongo "" para indicar que va a ser un string y su tipo de dato
        self.edad = 0 # Para que se sepa que será un número
        self.telefonos = [] # Objetos y listas pueden combinarse. Deben ser una lista vacia

# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad
cliente1.nombre = "Jose Vicente"

print("El nombre del cliente es: ", cliente1.nombre)

cliente1.telefonos.append("66643")
cliente1.telefonos.append("43564")

print(cliente1.telefonos)
