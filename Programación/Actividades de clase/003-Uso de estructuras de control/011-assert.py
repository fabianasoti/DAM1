'''
Programa de aserciones
v0.1 Fabiana Victoria Sotillo
Este programa verifica que un dato en el código sea correcto
'''

edad = 47
try:
    assert edad == 48
except:
    print('no es correcto')