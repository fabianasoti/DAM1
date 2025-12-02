''' 
    Calculadora de cuadras
    v0.1 Fabiana Victoria Sotillo
    Programa que calcula número de cuadras a partir de los caballos
'''

---
En programación, un objeto es una entidad que combina datos (atributos) y comportamientos (métodos). Los objetos se utilizan para representar entidades del mundo real (como fechas, personas o cálculos) de una manera estructurada y reutilizable.  

A su vez, los métodos son funciones asociadas a esos objetos que permiten manipular o consultar su información. Por ejemplo, el objeto date del módulo datetime tiene métodos como .weekday() o .isoweekday(), que devuelven el día de la semana en formato numérico.

El objetivo de este ejercicio es aplicar el uso de objetos y módulos en Python para resolver un problema cotidiano: calcular el número de cuadras necesarias según la cantidad de caballos disponibles.

Los pasos principales del programa incluyen:

- Importación de módulos externos (math y datetime).
- Declaración de variables iniciales.
- Creación de la fecha con los datos de entrada utilizando el objeto datetime.
- Uso de métodos del objeto para obtener información del día de la semana.
- Solicitud de la cantidad de caballos y cálculo de cuadras necesarias.
- Redondeo al alza mediante un método matemático (ceil()).
- Muestra de resultados en pantalla.

Este ejercicio refuerza el uso de módulos estándar, el manejo de fechas y la aplicación de operaciones matemáticas con redondeo, elementos esenciales en la programación orientada a objetos y en la automatización de tareas diarias. Para desarrollar este programa se ha realizado lo siguiente:

Se importan dos módulos estándar de Python:
math para usar funciones matemáticas.
datetime para manejar fechas y extraer información del calendario.
```
import math as matematicas
import datetime as fechas
```

Se declaran variables con valor 0 para asegurar su existencia antes de ser utilizadas.
```
caballos = 0
cuadras = 0
caballos_por_cuadra = 0
```

Se solicita al usuario entrada de información: la fecha actual (día, mes y año) y luego crea un objeto date para almacenarla.
También se pide la cantidad de caballos disponibles ese día.
```
dia = int(input("Introduce qué día es hoy en formato de fecha 'DD': "))
mes = int(input("Introduce qué mes es hoy en formato de fecha 'MM': "))
anio = int(input("Introduce qué año es hoy en formato 'YYYY': "))
hoy = fechas.date(anio, mes, dia)
print("Hoy es:", hoy)

caballos_por_cuadra = int3
caballos = int(input("Introduce el número de caballos que tienes hoy: "))
```

Se hace uso de métodos del objeto date para obtener el día de la semana.
```
.weekday() → devuelve un número del 0 (lunes) al 6 (domingo).

.isoweekday() → devuelve un número del 1 (lunes) al 7 (domingo).

diadelasemana = hoy      
diadelasemana_week = hoy.weekday() # Lunes = 0, Domingo = 6
print("weekday:", diadelasemana_week)
diadelasemana_iso = hoy.isoweekday()   # Lunes = 1, Domingo = 7
print("isoweekday:", diadelasemana_iso)
```

Se realiza el cálculo de cuadras y redondeo al alza con math.ceil().
```
cuadras = caballos / caballos_por_cuadra
redondeoalza = matematicas.ceil(cuadras)
```

Se utiliza try-except para asegurar que los datos introducidos son correctos.
```
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
```

Finalmente, se muestra un resumen con todos los datos ingresados y calculados.
```
print("Hoy", hoy, "año", anio, "del mes", mes, "del día", dia,
      "que es el día de la semana", diadelasemana, "tienes", caballos, "caballos.")
print("Y si te caben", caballos_por_cuadra, "caballos por cuadra,")
print("en ese caso necesitas", redondeoalza, "cuadras.")
```

A continuación se ilustra el bloque de código completo:
```
'''' 
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
```

A través de este ejercicio se aplicaron conceptos fundamentales de programación en Python relacionados con la utilización de objetos y módulos externos. Se demostró cómo emplear la biblioteca datetime para trabajar con fechas y la biblioteca math para realizar operaciones matemáticas precisas, en este caso el redondeo hacia arriba del número de cuadras necesarias.

El uso de variables, entradas de usuario y operaciones aritméticas permitió estructurar un pequeño programa funcional y claro. Además, se evidenció la importancia de los objetos y sus métodos (.date(), .weekday(), .isoweekday()), que aportan exactitud al tratamiento de datos.

Este tipo de ejercicios contribuye a fortalecer la lógica de programación y el pensamiento lógico, sirviendo como base para desarrollar programas más complejos que involucren objetos personalizados, clases y manejo avanzado de datos.
