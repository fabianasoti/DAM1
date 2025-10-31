class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail
        
clientes = []

clientes.append(Cliente("Fabiana", "info@fabiana.com"))
clientes.append(Cliente("Victoria", "info@victoria.com"))

print(clientes)
