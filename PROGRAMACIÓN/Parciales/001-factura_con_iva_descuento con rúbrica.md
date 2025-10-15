'''
Factura con IVA y descuento
v0.1 2025 Fabiana Sotillo
Programa que genera facturas calculando posibles descuentos e IVA 
'''

---
Con este programa se permite aplicar los conocimientos adquiridos en la primera unidad de la asignatura de programación: variables, constantes, tipos de datos, entradas y salidas de información, cálculos aritméticos y operaciones booleanas.
Este contenido, aunque básico, es sumamente necesario para la introducción a la programación.

- Las variables se usan para determinar la información y los tipos de datos con los que se trabaja en el programa. Los tipos de datos pueden ser, por ejemplo, literales de cadenas (""), enteros (int) o decimales (float), estos dos últimos son necesarios para poder realizar operaciones aritméticas.
- Además se crean constantes, que serán datos de variables que reutilizaremos en operaciones constantemente, con un valor fijo que no cambia.
- Para solicitar entrada de información al usuario se usa el "input()", y para mostrar la información en pantalla se usa el "print()".
- Finalmente, también se hace uso del if para poner condiciones al programa para ejecutar de cierta u otra manera los datos, y por ende se utilizan operaciones booleanas para hacer las comparaciones dentro de las condiciones aplicables.

---

Para desarrollar este programa:

- Se crean variables:
```
nombre_cliente = ""
precio = 0
precio_bruto = float(precio)
```

- Se crean constante:
```
IVA = 0.21
DESCUENTO = 10.0
```

- Se solicita entrada de información al usuario:
```
nombre_cliente = input("Introduce nombre del cliente: ")
precio_bruto = float(input("Introduce el precio bruto del producto: "))
```

- Se establecen las condiciones del descuento:
```
if precio_bruto >= 50:
    descuento_aplicado = float(subtotal_con_iva - DESCUENTO)
else:
    descuento_aplicado = 0
```
- Finalmente se muestra la información en pantalla.
```
print("TOTAL:", total, "€")
```

---

Se ilustrará el uso de todo lo anteriormente mencionado, en el siguiente bloque de código:

```
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
```
---

Para finalizar, con el código que se ha construido, se ha podido aplicar de manera práctica y utilizable en la vida cotidiana, todos los conocimientos adquiridos en la introducción a la asignatura de programación.
Al aplicar y definir bien los tipos de datos, se puede generar una factura calculando su IVA y posibles descuentos aplicables. Y se ha hecho usa de condicionales (if) y de operaciones booleanas (>=) para poder definir en qué casos era aplicable el descuento.
Solicitar (input()) y mostrar (print()) la información en pantalla es lo que nos permite interactuar con el usuario y mejorar su experiencia, lo que es un paso pequeño pero significativo en el proceso de crear una aplicación.
Se ha podido demostrar lo importante que es comprender los elementos básicos del código de un programa para así poder construir códigos más complejos en el futuro.
