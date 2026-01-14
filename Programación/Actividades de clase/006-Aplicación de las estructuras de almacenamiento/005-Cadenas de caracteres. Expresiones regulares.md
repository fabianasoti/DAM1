```
'''
Validación de direcciones postales con expresiones regulares
2026 Fabiana Sotillo
Programa que utiliza el módulo re para validar una dirección postal española
mediante una expresión regular.
'''
```

---
En la vida cotidiana es habitual trabajar con cadenas de texto que deben cumplir un formato específico, como ocurre con las direcciones postales al rellenar formularios en línea. Para garantizar que estos datos sean correctos, es necesario aplicar mecanismos de validación que permitan comprobar su estructura antes de ser almacenados o procesados. En este ejercicio se utiliza el lenguaje Python junto con el módulo re para validar una dirección postal española mediante expresiones regulares. El objetivo principal es comprender cómo funcionan las expresiones regulares y cómo pueden utilizarse para verificar patrones de texto de forma precisa y eficiente.

---
El programa se basa en el uso del módulo re, que permite trabajar con expresiones regulares en Python. Una expresión regular es una cadena que define un patrón que debe cumplir un texto determinado.

En este ejercicio se define una variable llamada patron que contiene una expresión regular diseñada para validar direcciones postales españolas con el siguiente formato:

Nombre de la calle + número + letra opcional + código postal
```
patron = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
```

Ejemplo válido:
Calle Mayor 10 B 46001

El patrón permite:
- Letras mayúsculas y minúsculas.
- Letras acentuadas y la letra ñ.
- Espacios entre los distintos componentes.
- Un número de portal formado por uno o más dígitos.
- Una letra opcional junto al número.
- Un código postal de exactamente cinco cifras.

Posteriormente, se utilizan dos cadenas de prueba, una incorrecta y otra correcta, y se valida cada una con la función re.match(), que comprueba si la cadena cumple el patrón desde el inicio hasta el final.

---
A continuación se muestra el código funcional completo:
```
'''
Validación de direcciones postales con expresiones regulares
2026 Fabiana Sotillo
Programa que utiliza el módulo re para validar una dirección postal española
mediante una expresión regular.
'''

import re

patron = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'

direccion_mal = "Calle Mayor"
direccion_bien = "Calle Mayor 10 46001"

print(re.match(patron, direccion_mal))
print(re.match(patron, direccion_bien))
```
El programa mostrará None para la dirección incorrecta, indicando que no cumple el patrón, y mostrará un objeto de tipo match para la dirección correcta, lo que confirma que el formato es válido según la expresión regular definida.

---
Este ejercicio permite aplicar de forma práctica el uso de expresiones regulares para la validación de cadenas de texto en Python.

A través del ejemplo de una dirección postal española, se refuerza la importancia de comprobar que los datos introducidos por el usuario cumplen un formato correcto antes de ser utilizados en una aplicación. 

El uso del módulo ```re``` facilita la detección de errores en los datos y mejora la fiabilidad de los programas que trabajan con formularios y sistemas de registro. Este conocimiento resulta fundamental para el desarrollo de aplicaciones reales que requieren validación de información de manera automática y segura.
