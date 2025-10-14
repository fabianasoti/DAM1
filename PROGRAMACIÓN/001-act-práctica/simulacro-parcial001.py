###### Se establecen variables
cliente_nombre = input("Introduce tu nombre: ")

edad = input("Introduce tu edad: ") 
edad_entero = int(edad) # Convierto edad a entero

#   Reglas de negocio
if edad_entero < 18:   # Si edad < 18: no emitir factura
    print("Es menor de 18 años, no se puede emitir factura.")
    exit()
else:    # Si es mayor de 18, es adulto: se emite factura
    print("Tiene la edad apta para generar su factura.")

base_imponible = (input("Introduce la base imponible de tu factura: ")) 
base_decimal = float(base_imponible)    # Convierto base en decimal


# Declaro constantes
IVA = 0.21 # Es el 21%
    
    
# Cálculos requeridos y reglas de negocio

importe_descuento = 0
descuento_decimal = float(importe_descuento)     # Convierto descuento en decimal
# Descuento según base_imponible
if base_decimal < 100: # < 100 €: 0%
    descuento_decimal = 0
    base_tras_descuento = base_decimal - descuento_decimal
    print("Descuento %", descuento_decimal)
    print("Descuento en euros:", descuento_decimal)
    
elif base_decimal <= 100 and base_imponible >= 199.99: # 100–199.99 €: 5%
    descuento_decimal = 0.5
    base_tras_descuento = base_decimal - descuento_decimal
    print("Descuento %", descuento_decimal)
    print("Descuento en euros:", descuento_decimal)
else:   # ≥ 200 €: 10%
    descuento_decimal = 0.10
    base_tras_descuento = base_decimal - descuento_decimal
    print("Descuento %", descuento_decimal)
    print("Descuento en euros:", descuento_decimal)

# Desglose: base, % descuento, € descuento, base tras descuento, IVA, TOTAL

base_tras_descuento = base_decimal - descuento_decimal
print("Tu base con el descuento es:", base_tras_descuento)

importe_iva = base_tras_descuento * IVA
print("Importe IVA 21%:", importe_iva)

total_factura = base_tras_descuento + importe_iva
print("Total:", total_factura)
    
    
# Ticket

print("______________________________________________")
print("  Factura con descuento y calculadora de IVA  ")
print("______________________________________________")




