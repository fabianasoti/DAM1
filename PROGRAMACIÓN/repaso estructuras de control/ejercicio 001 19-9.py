#Entrenamiento y duelo de dragones, utilizando estructuras de control combinadas y las buenas pràcticas.
#pide por consola el nombre y la edad de cada dragón: Dragón A y Dragón B

#en este bloque tomo los datos del usuario ###################
nombre_dragon_A = input('Dime el nombre del dragón A: ')
edad_dragon_A = input('Dime la edad del dragón A: ')
clasificacion_dragon_a = ''
fuerza_dragon_a = 0
resistencia_dragon_a = 0

print('El nombre del dragón A es: ', nombre_dragon_A)
print('La edad del dragón A es: ', edad_dragon_A)

nombre_dragon_B = input('Dime el nombre del dragón B: ')
edad_dragon_B = input('Dime la edad del dragón B: ')
clasificacion_dragon_b = ''
fuerza_dragon_b = 0
resistencia_dragon_b = 0

print('El nombre del dragón B es: ', nombre_dragon_B)
print('La edad del dragón B es: ', edad_dragon_B)

#aqui me aseguro de que la edad es un numero entero ###############
try:
    edad_dragon_a = int(edad_dragon_a)
    print('he convertido la edad A correctamente')
except: 
    edad_dragon_a = 100
    print('No he convertido la edad A correctamente, asigno 100')
    
try:
    edad_dragon_b = int(edad_dragon_b)
    print('he convertido la edad B correctamente')
except: 
    edad_dragon_b = 100
    print('No he convertido la edad B correctamente, asigno 100')
    
    
#en este bloque clasifico a los dragones según su edad ############

if edad_dragon_a < 50:
    clasificacion_dragon_a = 'Joven'
elif edad_dragon_a >=50 and edad_dragon_a <= 199:
    clasificacion_dragon_a = 'Adulto'
elif edad_dragon_a >=200:
    clasificacion_dragon_a = 'Anciano'
print('El dragón A es: ', clasificacion_dragon_a)
    
if edad_dragon_b < 50:
    clasificacion_dragon_b = 'Joven'
elif edad_dragon_b >=50 and edad_dragon_b <= 199:
    clasificacion_dragon_b = 'Adulto'
elif edad_dragon_b >=200:
    clasificacion_dragon_b = 'Anciano'
print('El dragón B es: ', clasificacion_dragon_b)

# Ahora los vamos a entrenar ###################################

for dia in range (1,4):
  # Como entrenar a tu dragon A
  if clasificacion_dragon_a == "Joven":
    fuerza_dragon_a += 2
    resistencia_dragon_a += 2
  elif clasificacion_dragon_a == "Adulto":
    fuerza_dragon_a += 1
    resistencia_dragon_a += 1
  elif clasificacion_dragon_a == "Anciano":
    fuerza_dragon_a += 1
    resistencia_dragon_a += 1
  print("Final del dia",dia)
  print("El dragon A ahora tiene ",fuerza_dragon_a,"de fuerza y ",resistencia_dragon_a,"de resistencia")
  # Como entrenar a tu dragon B
  if clasificacion_dragon_b == "Joven":
    fuerza_dragon_b += 2
    resistencia_dragon_b += 2
  elif clasificacion_dragon_b == "Adulto":
    fuerza_dragon_b += 1
    resistencia_dragon_b += 1
  elif clasificacion_dragon_b == "Anciano":
    fuerza_dragon_b += 1
    resistencia_dragon_b += 1
  print("Final del dia",dia)
  print("El dragon B ahora tiene ",fuerza_dragon_b,"de fuerza y ",resistencia_dragon_b,"de resistencia")
