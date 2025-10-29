# Establezco variables
taza_ml = input("Dime cuantos mililitros caben en tu taza: ")
taza_ml = int(taza_ml)
# Se realiza la clasificación del tamaño de tazas usando if, elif y else
if taza_ml <= 200: # Y se muestra en pantalla el tamaño del café en cada caso
    print("Tu café es pequeño")
elif taza_ml <= 350:
    print("Tu café es mediano")
elif taza_ml <= 500:
    print("Tu café es grande")
