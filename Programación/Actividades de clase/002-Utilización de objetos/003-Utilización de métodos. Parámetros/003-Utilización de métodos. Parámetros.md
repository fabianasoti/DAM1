```
'''
Redondeo al alza con math.ceil
2025 Fabiana Victoria Sotillo
Este programa importa la librería math para redondear al alza una variable
'''
```

---
La programación combina lógica y precisión para resolver problemas de manera eficiente. En este ejercicio se trabaja con métodos predefinidos del lenguaje Python, específicamente con el módulo math, que ofrece funciones matemáticas útiles como ceil().

El método math.ceil() redondea un número decimal hacia arriba al entero más próximo, facilitando cálculos que requieren exactitud. A través de este ejercicio se busca aplicar dicho método para redondear valores, almacenarlos e imprimir el resultado, fortaleciendo la comprensión del uso de bibliotecas estándar en Python.

- Para resolver este ejercicio, primero se debe importar la biblioteca math, que proporciona acceso al método ceil(). 
```
import math
```

- A continuación, se crea una variable numero_cafe con el valor decimal 7.2. 
```
numero_cafe = 7.2
```

- Este valor será redondeado hacia arriba usando math.ceil(numero_cafe), cuyo resultado se almacenará en una nueva variable llamada redondeo_cafe. 
```
redondeo_cafe = math.ceil(numero_cafe)
```

- Finalmente, se imprimirá el resultado mediante la función print().
```
print(redondeo_cafe)
```

---
A continuación se ilustra el código funcional completo:

```
'''
Redondeo al alza con math.ceil
2025 Fabiana Victoria Sotillo
Este programa importa la librería math para redondear al alza una variable
'''

# Importamos la biblioteca math
import math

# Definimos un número decimal representando la medida de café
numero_cafe = 7.2

# Aplicamos el método ceil() para redondear hacia arriba
redondeo_cafe = math.ceil(numero_cafe)

# Mostramos el resultado
print("El redondeo al alza de 7.2 es =", redondeo_cafe)
```

---
Este ejercicio permite poner en práctica el uso de métodos predefinidos en Python, en particular el método math.ceil(), que redondea valores decimales hacia arriba. Su correcta aplicación demuestra cómo aprovechar las bibliotecas estándar del lenguaje para simplificar cálculos y mantener un código limpio y eficiente.

Además, aprender a utilizar funciones como ceil() sienta las bases para abordar operaciones más complejas en ámbitos como el diseño de sistemas de cálculo, estadísticas o simulaciones, fortaleciendo el pensamiento lógico y la precisión en la resolución de problemas de programación.