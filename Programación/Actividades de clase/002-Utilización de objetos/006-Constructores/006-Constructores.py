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