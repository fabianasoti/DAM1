'''
Factura con IVA y descuento
v0.1 2025 Fabiana Sotillo
Programa que genera facturas calculando posibles descuentos e IVA 
'''

# Se crean variables
nombre_cliente = ""
precio = 0
precio_bruto = float(precio)

# Se crean constantes
IVA = 0.21
DESCUENTO = 10.0

# Entrada de información
nombre_cliente = input("Introduce nombre del cliente: ")
precio_bruto = float(input("Introduce el precio bruto del producto: "))

# Se realizan cálculos
descuento_aplicado = 0
iva_aplicado = precio_bruto * IVA
subtotal_con_iva = precio_bruto + iva_aplicado
total = subtotal_con_iva - descuento_aplicado


# Condiciones del descuento
if precio_bruto >= 50:
    descuento_aplicado = float(subtotal_con_iva - DESCUENTO)
else:
    descuento_aplicado = 0
    
# Salida de información
print("_________________________________")
print("              Factura            ")
print("    v0.1 2025 Fabiana Sotillo    ")
print("_________________________________")
print("---------------------------------")
print("Nombre cliente:", nombre_cliente)
print("---------------------------------")
print("Precio bruto:", precio_bruto, "€")
print("IVA aplicado 21%:", iva_aplicado, "€")
print("Descuento aplicado:", descuento_aplicado, "€")
print("---------------------------------")
print("TOTAL:", total, "€")
print("_________________________________")

