class Cliente():
    def __init__(self, email, nombre, direccion):
        self.email = email
        self.nombre = nombre
        self.direccion = direccion


print("_________________________")
print("Gestión de clientes v0.1")
print("Fabiana Victoria Sotillo")
print("_________________________")

clientes = []

while True:
    print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Actualizar un cliente")
    print("4.-Eliminar un cliente")
    opcion = int(input("Escoge una opción: "))

    if opcion == 1:
        email = input("Introduce el email: ")
        nombre = input("Introduce el nombre: ")
        direccion = input("Introduce la dirección: ")
        clientes.append(Cliente(email, nombre, direccion))

    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("Este es el cliente con ID:", identificador)
            print(cliente.email, cliente.nombre, cliente.direccion)
            identificador += 1

    elif opcion == 3:
        identificador = int(input("Introduce el id para modificar: "))
        email = input("Introduce el email: ")
        nombre = input("Introduce el nombre: ")
        direccion = input("Introduce la dirección: ")
        clientes[identificador].email = email
        clientes[identificador].nombre = nombre
        clientes[identificador].direccion = direccion

    elif opcion == 4:
        identificador = int(input("Introduce el ID para eliminar: "))
        confirmacion = input("¿Estás seguro? (S/N): ").lower()
        if confirmacion == "s":
            clientes.pop(identificador)
        elif confirmacion == "n":
            print("Cancelado")
        else:
            print("Opción no válida")