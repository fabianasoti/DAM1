def hazDivision(dividendo,divisor):
    #comprobamos si son números
    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    #Comprobamos que el divisor no es 0
        if divisor !=0:
            resultado = dividendo/divisor
            return resultado
        else:
            resultado = 0     
    else:
        try:
            #Vamos a intentar convertirlo a números
            dividendo = float(dividendo)
            divisor = float(divisor)
            resultado = dividendo/divisor
            return resultado
        except:
            return 0

print(hazDivision(4,'3'))
