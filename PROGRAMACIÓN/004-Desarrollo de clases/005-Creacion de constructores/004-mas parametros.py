class Gato():
    def __init__(self): # El constructor se ejecuta sí o sí
        self.edad = 0
        
    def maulla(self):   #El resto de métodos sólo se ejecutan si los llamas
        return "El gayo está maullando"
        
gato1 = Gato(5)

