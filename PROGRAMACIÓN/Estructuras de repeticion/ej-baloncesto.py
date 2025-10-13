#docstring
'''
programa clasificador de baloncesto 
v.01 jose
'''
#importaciones
#este programa no requiere importaciones

#declaracion de variables globales
#inicializamos las variables con valores vacíos
edad=0
categoria=''

#funciones/clases 
#en este programa no hay funciones o clases

Las estructuras de control de señección nos permiten ejecutar diferentes bloques de codigo condicional, es decir, la ejecucion de esos bloques esta supeditada a la validacion de una expresion.
Nos sirve para elegir que partes de un programa se activan y cuales permanecen sin ejecutarse

## 2. desarrolllo detallado y preciso
Cuando introducimos una o


#funcion principal
edad= input('Introduce tu edad')
edad = int(edad) #Convierto la edad en un entero
if edad < 8:
 categoría = 'pre-mini'
elif edad >= 8 and edad < 11:
 categoria = 'mini'
elif edad >= 12 and edad <= 15:
 categoria = 'infantil'
elif edad >= 16 and edad <= 17:
 categoria = 'cadete'
elif edad >= 18 and edad <= 20:
 categoria = 'junior'
else:
 categoria = senior

print('Tu edad es de', edad, 'años, y tu categoria es: ', categoria)
if edad > 40:
 ('Veterano con experiencia en la cancha')
 
 #elif: else+if. Si no pasa esto y pasa esto, pasa esto.
 #if: si pasa la condiciòn pasa x. siempre se pregunta
 #else: si no pasa nada de lo de arriba pasa y.
 #elif: solo se pregunta si las condiciones anteriores no se cumplen
