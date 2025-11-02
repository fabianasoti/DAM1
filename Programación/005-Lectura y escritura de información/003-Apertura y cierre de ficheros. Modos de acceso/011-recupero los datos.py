import pickle

class Cliente():
  def __init__(self,nuevonombre,nuevoemail):
    self.nombre = nuevonombre
    self.email = nuevoemail

archivo = open("clientes.bn","rb")
clientes = pickle.load(archivo)
archivo.close()

print(clientes)
