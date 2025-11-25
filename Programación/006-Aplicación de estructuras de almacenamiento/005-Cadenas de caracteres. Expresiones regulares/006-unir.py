datos = "uno,dos,tres,cuatro,cinco,seis"

# Primero imprimo la cadena
print(datos)
# Ahora la parto
partido = datos.split(",")
# Ahora imprimo el partido
print(partido)
# Ahora quiero unirlo todo de nuevo
nueva_cadena = "|".join(partido) # Se puede usar cualquier caracter para separarlo
print(nueva_cadena)
