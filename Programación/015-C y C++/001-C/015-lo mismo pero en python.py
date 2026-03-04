import time

inicio = time.time()

numero = 1.0000000432
for contador in range(235324544):  # range llega hasta n-1
    numero = numero * 1.00000000645

fin = time.time()

tiempo = fin - inicio

print(f"El resultado es: {numero}")
print(f"Tiempo de ejecución: {tiempo} segundos")
