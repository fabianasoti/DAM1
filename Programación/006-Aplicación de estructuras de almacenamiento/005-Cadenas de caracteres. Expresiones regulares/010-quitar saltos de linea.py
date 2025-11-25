# Esta cadena tiene algo que no quiero (\n)
linea_con_salto = "Esto es una prueba \n"
# Lo que quiero es QUITAR algo
# Reemplazo \n con "nada"

limpiado = linea_con_salto.replace("\n","")

print(linea_con_salto)
print(limpiado)
print(limpiado)
