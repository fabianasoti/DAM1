# Las propiedades son como las variables PERO dentro de una clase.
# Podemos crear tantas propiedades como queramos
# Arrays =  arreglos. Conjunto de cosas, listas.

class Cliente():
    def _init_(self):
        self.nombre = None # O le pongo "" para indicar que va a ser un string y su tipo de dato
        self.edad = 0 # Para que se sepa que será un número
        self.telefonos = ['66396', '66625'] # Objetos y listas pueden combinarse.

# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad

cliente1.nombre = "Jose Vicente"