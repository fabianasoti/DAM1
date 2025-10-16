#pedir edad
edad_mago = input('Introduce la edad del mago: ')
#convertir a entero
try:
    edad_mago = int(edad_mago)
#si falla, pon 100
except:
    edad_mago = 100
    
#clasifica por edad
clasificacion_mago: ''
#menor que 30 es aprendiz
if edad_mago < 30:
    clasificacion_edad = 'Aprendiz'
#de 30 a 99 es hechicero
elif edad_mago >= 30 and edad_mago <100:
    clasificacion_edad = 'Hechicero'
#màs de 100 es archimago
elif edad_mago >= 100:
    clasificacion_edad = 'Archimago'


#funcion poderBase, recibe edad, devuelve entero
def poderBase(edad_mago)

#si es aprendiz, devuelve 5
#si es hechicero, devuelve 8
#si es archimago, devuelve 10

#empezamos bucle
#escudo empieza con 15 puntos
#recorre dos turnos con for
#turno 1 fuego daño: poderBase//2
#turno 2 hechizo rayo = daño = poderBase //3
#resta el daño al escudo
#si energia escudo baja de cero, ajusta a cero

#tras cada daño, print de daño y mayor que cero
#tras ajuste de energia, print y energia es mayor que cero

#salida: edad, rango, poder base, energia del escudo.
#energia es cero, mago rompe escudo
#energia mayor que cero; escudo resiste duelo.
