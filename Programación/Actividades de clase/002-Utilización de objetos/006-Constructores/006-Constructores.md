```
'''
Uso del módulo datetime
2025 Fabiana Victoria Sotillo
Programa que obtiene y muestra la fecha actual, 
incluyendo el día de la semana y el mes en curso,
utilizando métodos y atributos de la clase datetime.date.
'''
```

---
El manejo de fechas es una parte fundamental de la programación, ya que permite registrar, organizar y mostrar información temporal de manera precisa. En Python, el módulo datetime proporciona clases y métodos que facilitan el trabajo con fechas y horas. En este ejercicio se emplean los métodos date.today() y strftime() para obtener la fecha actual, identificar el mes y el día de la semana, y mostrar la información en un formato legible, reforzando así el uso de objetos y sus atributos en la práctica.

El ejercicio se basa en el uso de la clase date del módulo datetime, la cual permite trabajar directamente con fechas.

---
Para construir este código se han realizado los siguientes pasos:

- Se importa datetime, que es el módulo necesario para trabajar con fechas.
```
import datetime 
```

- Se crea una variable fecha_hoy que almacena la fecha actual mediante datetime.date.today().
```
fecha_hoy = datetime.date.today()
```

- Luego, se accede al atributo month de ese objeto para obtener el número correspondiente al mes actual.
```
mes_actual = fecha_hoy.month
```

- Se utiliza el método strftime('%A') para convertir la fecha en una cadena que contiene el nombre completo del día de la semana.
```
dia_semana = fecha_hoy.strftime('%A')
```

- Y finalmente se muestra un mensaje con el día y el mes actual.
```
print("Hoy es", dia_semana, "y estamos en el mes número", mes_actual)
```

---
A continuación se ilustra el código funcional completo:

```
'''
Uso del módulo datetime
2025 Fabiana Victoria Sotillo
Programa que obtiene y muestra la fecha actual, 
incluyendo el día de la semana y el mes en curso,
utilizando métodos y atributos de la clase datetime.date.
'''

# Importar el módulo datetime
import datetime

# Obtener la fecha actual
fecha_hoy = datetime.date.today()

# Imprimir la fecha actual
print("La fecha de hoy es:", fecha_hoy)

# Obtener el número del mes actual
mes_actual = fecha_hoy.month

# Obtener el nombre del día de la semana
dia_semana = fecha_hoy.strftime('%A')

# Mostrar un mensaje con el día y el mes actual
print("Hoy es", dia_semana, "y estamos en el mes número", mes_actual)
```

---
Este ejercicio permite comprender cómo utilizar objetos predefinidos del módulo datetime para manejar información relacionada con fechas. Se aplicaron los métodos today() y strftime() junto con el atributo month, fortaleciendo el uso de propiedades y métodos dentro de una clase. Además, este conocimiento resulta esencial para desarrollar programas que gestionen registros temporales.