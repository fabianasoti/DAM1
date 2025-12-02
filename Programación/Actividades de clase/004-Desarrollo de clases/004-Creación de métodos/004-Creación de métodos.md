```
''' 
Gestión de clientes y cuentas bancarias
2025 Fabiana Victoria Sotillo
Programa que gestiona una Cuenta Bancaria
'''
```

---

La programación orientada a objetos (POO) organiza el código mediante clases y objetos, lo que facilita su reutilización y mantenimiento. Una clase define las propiedades y comportamientos de un objeto, mientras que los atributos privados y los métodos setter y getter garantizan el encapsulamiento y la protección de datos. En este ejercicio se aplica la POO para simular la gestión de un cliente y su cuenta bancaria, utilizando una variable global que controla los ingresos excesivos, como parte de una práctica de validación y seguridad en sistemas simples.

En el código se implementan dos clases principales: Cliente y CuentaBancaria.
La clase Cliente gestiona la información personal del usuario, mientras que CuentaBancaria controla el saldo y las validaciones de ingreso. Además, se emplea una variable global (limitediferenciasaldo) que restringe movimientos demasiado grandes para simular un control por parte del banco.

---
Explicación paso a paso:

- Se define una variable global que establece un límite de diferencia máxima entre el saldo actual y el nuevo saldo permitido.
```
limitediferenciasaldo = 1000
```

- Se crea la clase Cliente con dos atributos privados: ```__nombrecompleto``` y ```__email```. El método constructor ```__init__``` inicializa los atributos vacíos.
```
class Cliente():
    def __init__(self):
        self.__nombrecompleto = ""
        self.__email = ""
```

- Se establecen los métodos setter y getter que permiten modificar y acceder a los atributos privados, aplicando el encapsulamiento correctamente.
```
    def setNombreCompleto(self, nombre):
        self.__nombrecompleto = nombre

    def getNombreCompleto(self):
        return self.__nombrecompleto

    def setEmail(self, correo):
        self.__email = correo

    def getEmail(self):
        return self.__email
```

- Se define la clase CuentaBancaria, la cual contiene dos atributos privados: donde ```__saldo``` almacena el saldo del cliente, y ```__cliente``` referencia al objeto Cliente asociado a la cuenta.
```
class CuentaBancaria():
    def __init__(self):
        self.__saldo = 0
        self.__cliente = None
```

- Se crea el método setSaldo, el cual valida el ingreso utilizando la variable global limitediferenciasaldo. Y dentro de un blque if se establece que si el nuevo saldo excede el límite, muestra una advertencia; de lo contrario, actualiza el saldo.
```
    def setSaldo(self, nuevosaldo):
        if nuevosaldo > self.__saldo + limitediferenciasaldo:
            print("Voy a avisar a la entidad de un ingreso muy grande")
        else:
            self.__saldo = nuevosaldo
```

- Se establece el getSaldo que devuelve el saldo actual almacenado en la cuenta.
```
    def getSaldo(self):
        return self.__saldo
```

- Se establecen métodos que relacionan un objeto Cliente con la cuenta bancaria, lo que permite asociar los datos personales con el saldo del cliente.
```
    def setCliente(self, cliente):
        self.__cliente = cliente

    def getCliente(self):
        return self.__cliente
```

- Se crea un objeto Cliente y se inicializan sus atributos con los métodos setter.
```
cliente1 = Cliente()
cliente1.setNombreCompleto("Fabiana Sotillo")
cliente1.setEmail("fabiana@email.com")
```

- Se crea un objeto CuentaBancaria vinculado al cliente anterior. El intento de asignar un saldo demasiado alto activa la alerta de seguridad.
```
cuentacliente1 = CuentaBancaria()
cuentacliente1.setCliente(cliente1)
cuentacliente1.setSaldo(10000000000)
```

- Se muestran los datos del cliente y el saldo actual de su cuenta, verificando el correcto funcionamiento del programa.
```
print("Cliente:", cuentacliente1.getCliente().getNombreCompleto())
print("Saldo actual:", cuentacliente1.getSaldo())
```

---
A continuación se ilustra el código funcional completo:
```
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
```

---
Este ejercicio consolida los conocimientos sobre clases, métodos, encapsulamiento y variables globales, aplicados en un contexto realista de gestión bancaria.

Esta práctica permite comprender cómo los setters y getters permiten un control seguro sobre los datos, evitando accesos indebidos a los atributos privados. Además, la inclusión de una variable global de control refuerza la validación de condiciones lógicas en el código, fomentando buenas prácticas de seguridad y estructura en el desarrollo de un programa.