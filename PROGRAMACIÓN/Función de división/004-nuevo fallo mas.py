def hazDivision(dividendo,divisor):
    #comprobamos si son números
    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    #Comprobamos que el divisor no es 0
        if divisor !=0:
            resultado = dividendo/divisor
        else:
            resultado = 0
        return resultado
    else:
        return 0

print(hazDivision(4,'3'))


