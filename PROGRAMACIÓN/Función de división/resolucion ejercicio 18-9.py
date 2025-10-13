def raizCuadrada (radicando):
    #para poder operar raices hay que importar sqrt de math
    from math import sqrt
    
    if isinstance(radicando, (int, float)):
        if radicando >= 0:
            resultado = sqrt(radicando)
            return resultado
            
        else:
            return 0
    else:
        try:
            radicando = float(radicando)
            resultado = sqrt(radicando)
            return resultado
            
        except:
            return 0
            
    
