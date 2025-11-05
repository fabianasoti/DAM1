''' 
Constructores en clases de Python
2025 Fabiana Victoria Sotillo
Programa que define una clase Persona con un constructor y método
'''

# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, apellidos, edad, hobby):
        # Constructor que inicializa los atributos de la persona
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.hobby = hobby

    def mostrar_hobby(self):
        # Método que devuelve el hobby de la persona
        return "El hobby de "+self.nombre+" es "+self.hobby

# Creación de una instancia de la clase Persona con los datos de Ana
ana = Persona("Ana", "Gómez Pérez", 22, "crochet")

# Mostrar el hobby de Ana
print(ana.mostrar_hobby())

