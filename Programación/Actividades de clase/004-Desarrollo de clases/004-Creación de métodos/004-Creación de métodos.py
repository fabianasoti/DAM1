''' 
Gestión de clientes y cuentas bancarias
2025 Fabiana Victoria Sotillo
Programa que gestiona una Cuenta Bancaria
'''
limitediferenciasaldo = 1000

class Cliente():
    def __init__(self):
        self.__nombrecompleto = ""
        self.__email = ""
    
    def setNombreCompleto(self, nombre):
        self.__nombrecompleto = nombre

    def getNombreCompleto(self):
        return self.__nombrecompleto

    def setEmail(self, correo):
        self.__email = correo

    def getEmail(self):
        return self.__email

class CuentaBancaria():
    def __init__(self):
        self.__saldo = 0
        self.__cliente = None
    
    def setSaldo(self, nuevosaldo):
        if nuevosaldo > self.__saldo + limitediferenciasaldo:
            print("Voy a avisar a la entidad de un ingreso muy grande")
        else:
            self.__saldo = nuevosaldo
      
    def getSaldo(self):
        return self.__saldo

    def setCliente(self, cliente):
        self.__cliente = cliente

    def getCliente(self):
        return self.__cliente

cliente1 = Cliente()
cliente1.setNombreCompleto("Fabiana Sotillo")
cliente1.setEmail("fabiana@email.com")

cuentacliente1 = CuentaBancaria()
cuentacliente1.setCliente(cliente1)
cuentacliente1.setSaldo(10000000000)

print("Cliente:", cuentacliente1.getCliente().getNombreCompleto())
print("Saldo actual:", cuentacliente1.getSaldo())