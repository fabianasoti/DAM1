# Se define la variable de la edad del jugador
edad_jugador = input("Dime tu edad: ")
edad_jugador = int(edad_jugador)

#Se realiza la clasificación de categoría por edad usando if, elif, else
# Si la edad es menor a 10 años, imprime "Eres un niño".
if edad_jugador < 10 :
    print("Eres un niño")
# Si la edad está entre 10 y 20 años (inclusive), imprime "Eres un adolescente".
elif edad_jugador >= 10 and edad_jugador <= 20:
    print("Eres un adolescente")
# Si la edad está entre 20 y 30 años (inclusive), imprime "Eres un joven".
elif edad_jugador >= 20 and edad_jugador <= 30:
    print("Eres un joven")
# Para cualquier otra edad, imprime "Ya no eres un joven".
else:
    print("Ya no eres un joven")

