Este programa 
```
'''
    Calculadora de Impuestos
    (c) 2025 Fabiana Sotillo
    Introduce una base imponible y se calcula IVA y total
'''

# Se crean variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Se solicita entrada al usuario
print("Introduce una base y te calculo el IVA y el total")
base_imponible = float(input("Introduce la base imponible de la factura: "))

# Se realizan cálculos
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

# Por último expreso una salida
print("El IVA de la factura es: ", total_iva)
print("El total de la factura es: ", total_factura)
```
