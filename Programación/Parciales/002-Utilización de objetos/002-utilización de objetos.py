''' 
    Calculadora de cuadras
    v0.1 Fabiana Victoria Sotillo
    Programa que calcula número de cuadras a partir de los caballos
'''

import math as matematicas
import datetime as fechas

# Datos de inicio
caballos = 0
cuadras = 0
caballos_por_cuadra = 0

# Entrada de información
try:
    dia = int(input("Introduce qué día es hoy en formato de fecha 'DD': "))
    mes = int(input("Introduce qué mes es hoy en formato de fecha 'MM': "))
    anio = int(input("Introduce qué año es hoy en formato 'YYYY': "))

    if dia <= 0 or mes <= 0 or anio <= 0:
        print("Error: los valores de la fecha deben ser enteros positivos.")
        exit()

    # Creación de fecha
    hoy = fechas.date(anio, mes, dia)
    print("Hoy es:", hoy)
    
except:
    print("Error: formato de fecha incorrecto o valores no válidos.")
    exit()

# Datos de cálculo y entrada de información
try:
    caballos_por_cuadra = int(input("Introduce el número de caballos por cuadra: "))
    caballos = int(input("Introduce el número de caballos que tienes hoy: "))

    if caballos_por_cuadra <= 0 or caballos <= 0:
        print("Error: los valores deben ser enteros positivos.")
        exit()
        
except:
    print("Error: debes introducir solo números enteros positivos.")
    exit()

# Obtención del día de la semana
diadelasemana = hoy      
diadelasemana_week = hoy.weekday() # Lunes = 0, Domingo = 6
print("weekday:", diadelasemana_week)
diadelasemana_iso = hoy.isoweekday()   # Lunes = 1, Domingo = 7
print("isoweekday:", diadelasemana_iso)

# Realización de cálculos
cuadras = caballos / caballos_por_cuadra
redondeoalza = matematicas.ceil(cuadras)  # Redondeo hacia arriba

# Salida de resultados
print("Hoy", hoy, "año", anio, "del mes", mes, "del día", dia,)
print("que es el día de la semana weekday:", diadelasemana_week,) 
print("y día de la semana isoweekday:", diadelasemana_iso)
print("Tienes", caballos, "caballos.")
print("Y si te caben", caballos_por_cuadra, "caballos por cuadra,")
print("en ese caso necesitas", redondeoalza, "cuadras.")
