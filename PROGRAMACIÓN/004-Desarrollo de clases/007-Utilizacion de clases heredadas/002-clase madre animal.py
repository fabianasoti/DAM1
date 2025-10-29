class Animal():
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.raza = ""

class Gato(Animal):
    def __init__(self):
        super().__init__()  # Llamada a un método
        
class Perro(Animal):
    def __init__(self):
        super().__init__()
       
gato1 = Gato()
print(gato1.edad)
