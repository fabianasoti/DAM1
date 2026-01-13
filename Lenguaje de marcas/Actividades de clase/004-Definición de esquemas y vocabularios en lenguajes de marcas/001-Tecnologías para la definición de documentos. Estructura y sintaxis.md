```
'''
XML
2026 Fabiana Sotillo
Almacenar y transportar datos de forma estructurada entre sistemas con XML
'''
```

---
XML es un lenguaje de marcado orientado al intercambio de datos, donde cada documento debe cumplir una serie de normas básicas para ser considerado válido:

- Debe existir una única etiqueta raíz.
- Todas las etiquetas deben abrirse y cerrarse correctamente.
- Las etiquetas son sensibles a mayúsculas y minúsculas.
- Los elementos pueden anidarse jerárquicamente.
- La estructura debe ser clara y coherente.

En este ejercicio se trabaja el lenguaje de marcado XML (eXtensible Markup Language), utilizado para almacenar y transportar datos de forma estructurada entre sistemas. A diferencia de HTML, XML permite definir etiquetas personalizadas y organizar la información mediante elementos anidados, manteniendo una estructura jerárquica clara y ordenada. El objetivo es crear documentos XML correctamente formados, aplicando el uso de etiquetas raíz, elementos anidados y respetando la norma de sensibilidad a mayúsculas y minúsculas (case sensitive).

Se han creado varios documentos XML para aplicar estos conceptos, trabajando con etiquetas personalizadas, estructuras anidadas y múltiples elementos dentro de un mismo documento.

---
Aplicación práctica:

#### 1.- persona.xml
Se crea un documento XML con una etiqueta raíz ```<persona>``` y tres elementos hijos: nombre, apellidos y teléfono. 
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
  <telefono>12345567</telefono>
</persona>
```

#### 2.- varios-telefonos.xml
Se crea un documento con una estructura anidada, incluyendo un contenedor ```<telefonos>``` con varias subetiquetas ```<telefono>```.
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
  </telefonos>
</persona>
```
Este ejercicio permite comprender cómo se organizan datos relacionados dentro de una estructura jerárquica.

#### 3.- subetiquetas.xml
Documento con etiqueta raíz y subetiquetas internas correctamente estructuradas.
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
</persona>
```

#### 4.- debe-haber-una-etiqueta-raiz.xml
Documento que cumple la norma fundamental de XML: una única etiqueta raíz.
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
</persona>
```

---
A través de estos ejercicios se ha aprendido a estructurar y sintetizar información utilizando XML, creando documentos correctamente formados mediante etiquetas personalizadas y estructuras jerárquicas. 

Se ha aplicado el uso de elementos anidados y la norma case sensitive, fundamentales para garantizar la validez de los documentos. 

Esta práctica refuerza la comprensión del lenguaje XML como herramienta esencial para el intercambio de datos entre sistemas y como base para el trabajo de desarrollo.
