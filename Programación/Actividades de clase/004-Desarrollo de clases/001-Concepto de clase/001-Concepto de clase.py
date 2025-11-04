class Café:
  def __init__(self, nombre, ubicación):
    self.nombre = nombre
    self.ubicación = ubicación
  
  def preparar_café(self):
    print("El café está siendo preparado en",self.nombre)

# Crear un objeto de la clase Café
mi_cafe = Café("Café DDL", "Av. San Vicente Martir")

# Llamar al método preparar_café
mi_cafe.preparar_café()