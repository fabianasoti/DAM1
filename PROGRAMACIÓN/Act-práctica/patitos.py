#1 Patitos producidos en el año 2023
patitos_contados = 0
patitos_2023 = 0

for mes in range(1, 13):  # Recorremos los meses del año (1 al 12)
    for dia in range(1, 32):  # Recorremos los días del mes (1 al 31)
        patitos_contados += 5  # Suponemos que producen 5 patitos por día
print("Los patitos producidos en 2023, son", patitos_2023) # Se muestra lo que se ha producido en 2023


#2 Patitos producidos desde 1978 a 2024
patitos_contados = 0
patitos_2023 = 0
for anio in range(1978, 2024):  # Recorremos los años desde 1978 hasta 2023
    for mes in range(1, 13):  # Recorremos los meses del año (1 al 12)
        for dia in range(1, 32):  # Recorremos los días del mes (1 al 31)
            patitos_contados += 5  # Suponemos que producen 5 patitos por día
            print("Hoy es el día", dia, "del mes", mes, "del año", anio, "y se han producido", patitos_contados, "patitos") # Se muestra todo lo que se ha producido en patitos en total desde 1978 hasta 2023
            if anio == 2023:
                patitos_2023 +=1
print("Los patitos producidos en 2023, son", patitos_2023) # Se muestra lo que se ha producido en 2023
 









