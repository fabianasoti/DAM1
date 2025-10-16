# Las listas se mueven, son modificables
cliente1 = "Juan"
cliente2 = "Jorge"

clientes = ["Juan", "Jorge", "Jaime", "José"]

print (clientes)

# Añadir un cliente

clientes.append("Julia")

print(clientes)

# Quito elementos de la lista
# Los que acabo de agregar con .append se van

clientes.pop()

print(clientes)
