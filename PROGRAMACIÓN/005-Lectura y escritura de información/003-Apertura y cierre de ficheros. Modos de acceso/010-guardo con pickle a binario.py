import pickle

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
clientes = []

clientes.append(Cliente("Fabiana", "info@fabiana.com"))
clientes.append(Cliente("Victoria", "info@victoria.com"))

archivo = open("clientes.bn","wb")
pickle.dump(clientes,archivo)
archivo.close()
