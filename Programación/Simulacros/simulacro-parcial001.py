'''
Generador de facturas
v0.1 2025 Fabiana Victoria Sotillo
Se genera un ticket calculando posibles descuentos e IVA
'''
###### Se establecen variables
cliente_nombre = input("Introduce tu nombre: ")
# Entrada edad convertida a entero
edad = int(input("Introduce tu edad: ")) # Convierto edad a entero

# Reglas de negocio 
if edad <= 0:
	print("Edad invalida")
elif edad < 18: # Si edad < 18: no emitir factura
    print("Es menor de 18 años, no se puede emitir factura.")
    exit()
else:    # Si es mayor de 18, es adulto: se emite factura
    print("Tiene la edad apta para generar su factura.")

# Entrada base convertida en decimal
base_imponible = float(input("Introduce la base imponible de tu factura: "))

if base_imponible <= 0: # Me aseguro de que es un número positivo
    print("Error: Base imponible inválida")

# Declaro constantes
IVA = 0.21 # Es el 21%
    
    
# Definición del descuento
porcentaje_descuento = 0
descuento = 0
# Descuento según base_imponible
if base_imponible < 100: # < 100 €: 0%
    porcentaje_descuento = 0
    descuento = 0
    
elif base_imponible <= 100 and base_imponible >= 199.99: # 100–199.99 €: 5%
    porcentaje_descuento = 5
    descuento = 0.05
    
else:   # ≥ 200 €: 10%
    porcentaje_descuento = 10
    descuento = 0.1

# Desglose: base, % descuento, € descuento, base tras descuento, IVA, TOTAL

# Cálculos requeridos
importe_descuento = base_imponible * descuento # Lo que se descuenta en euros
base_tras_descuento = base_imponible - importe_descuento # A pagar sin iva
importe_iva = base_tras_descuento * IVA # el porcentaje que corresponde de IVA según base
total_factura = base_tras_descuento + importe_iva
    
    
# Ticket

print("______________________________________________")
print("|           Generador de facturas            |")
print("|          Fabiana Victoria Sotillo          |")
print("|                 v0.1 2025                  |")
print("|____________________________________________|")
print("Nombre: ", cliente_nombre)
print("Edad: ", edad)
print("----------------------------------------------")
print("Base imponible:",base_imponible, "€")
print("Porcentaje de descuento:", porcentaje_descuento, "%")
print("Importe descuento:", importe_descuento, "€")
print("Base tras descuento:", base_tras_descuento, "€")
print("IVA (21%):", importe_iva, "€")
print("                              ----------------")
print("Total:", total_factura, "€")
print("______________________________________________")



