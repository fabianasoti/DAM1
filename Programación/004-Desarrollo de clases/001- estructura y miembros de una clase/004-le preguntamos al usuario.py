# Declaramos una clase
# Las clases son contenedores de información
class Cliente(): 
    def _init_(self):
        self.email = "" # También se puede usar el None
        self.nombre = None
        self.direccion = None

# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = input("Introduce el email del cliente: ")
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.direccion = input("Introduce la dirección del cliente: ")

print(cliente1)



