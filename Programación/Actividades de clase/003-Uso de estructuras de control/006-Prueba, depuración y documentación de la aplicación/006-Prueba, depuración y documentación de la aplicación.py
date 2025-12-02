'''
Si el numero es un valor numérico (int o float) y es mayor o igual a 0, devuelve su raíz cuadrada.
Si numero es una cadena, intenta convertirla a float y devuelve su raíz cuadrada
Si la conversión falla, o si el número es negativo, la función devuelve 0.
'''
import math

def raizSegura(numero):
    try:
        # Si es string intentamos convertirlo
        if isinstance(numero, str):
            numero = float(numero)

        # Comprobación de número negativo
        if numero < 0:
            return 0

        # Aserciones (comprobaciones internas)
        assert isinstance(numero, (int, float)), "El valor debe ser numérico"
        assert numero >= 0, "El número debe ser mayor o igual a 0"

        return math.sqrt(numero)

    except:
        # Si ocurre cualquier error devolvemos 0
        return 0

print(raizSegura(4))     
print(raizSegura("9")) 
print(raizSegura("-1"))  
print(raizSegura("abc")) 
print(raizSegura(-5))    
print(raizSegura(None)) 
