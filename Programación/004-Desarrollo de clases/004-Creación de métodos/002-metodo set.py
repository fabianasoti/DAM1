class Gato():
    def __init__(self):
        self.color = "" # Esto es una propiedad. Estática. Sustantivo.
        
    def maulla(self):   # Esto es un método (es una acción). Verbo.
        return "miau"
        
        
gato1 = Gato()
gato1.color = "naranja" # Aquí seteamos una propiedad.
print(gato1.maulla())   # Aquí llamamos a un método.
