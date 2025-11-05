''' 
Aplicación de gestión de clientes
2025 Fabiana Victoria Sotillo
Esta aplicación gestiona clientes
'''

# Definición de la clase Cliente
class Cliente:
    def __init__(self):
        # Inicialización de atributos con valores vacíos o nulos
        self.nombre = ""
        self.edad = 0
        self.telefonos = []  # lista para almacenar múltiples números de teléfono

# Creación de una instancia del objeto Cliente
cliente1 = Cliente()

# Asignación de valores a las propiedades
cliente1.nombre = "Fabiana Sotillo"
cliente1.edad = 23
cliente1.telefonos = ["663966930", "667077890"]

# Mostrar los valores asignados
print("Nombre del cliente:", cliente1.nombre)
print("Edad:", cliente1.edad)
print("Teléfonos:", cliente1.telefonos)