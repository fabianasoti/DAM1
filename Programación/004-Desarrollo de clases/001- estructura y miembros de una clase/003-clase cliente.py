# Declaramos una clase
# Las clases son contenedores de información
class Cliente(): 
    def _init_(self):
        self.email = "" # También se puede usar el None
        self.nombre = None
        self.direccion = None

# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = "jose@empresa.com"
cliente1.nombre = "Jose"
cliente1.direccion = "La calle de Jose"

# El uso de objetos no es obligatorio pero es de gran ayuda.
# Hace que el código sea limpio y legible


