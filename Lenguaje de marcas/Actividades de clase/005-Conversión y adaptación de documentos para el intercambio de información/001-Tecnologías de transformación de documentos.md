```
'''
Tecnologías de transformación de documentos
2026 Fabiana Sotillo
Conversión y adaptación de documentos mediante el uso de 
Python y librerías especializadas para la generación de archivos
'''
```

---
En esta actividad se trabaja la conversión y adaptación de documentos mediante el uso de Python y librerías especializadas para la generación de archivos PDF a partir de distintos formatos de origen, como texto Markdown y tablas de datos. El objetivo principal es comprender cómo transformar información estructurada en documentos portables utilizando herramientas de automatización, aplicando conceptos de procesamiento de datos, generación de archivos y manipulación de formatos.

La conversión de documentos es una tarea fundamental en entornos informáticos donde se requiere adaptar información entre distintos formatos para su almacenamiento, distribución o presentación. Python ofrece múltiples bibliotecas que facilitan estas tareas, permitiendo automatizar procesos de conversión de texto, tablas y documentos estructurados.

En esta actividad se utilizan principalmente las siguientes librerías:
- markdown: para trabajar con documentos en formato Markdown.
- fpdf: para generar documentos PDF desde Python.
- pandas: para manipular datos tabulares y convertirlos en estructuras como DataFrames.
- odfpy: para facilitar la exportación de datos a formatos de hoja de cálculo.

El proceso general consiste en:
1.- Leer el contenido de un documento.
2.- Procesar la información con Python.
3.- Generar un archivo PDF con la estructura adecuada.
4.- Guardar el archivo en el sistema de archivos.
De esta forma, se logra una conversión eficiente y automatizada entre distintos formatos de documentos.

---
Aplicación práctica:

#### Conversión de texto Markdown a PDF
Para la conversión de un documento Markdown a PDF se ha utilizado la biblioteca fpdf, que permite generar archivos PDF línea por línea.

- Instalación de la librería:
```
pip3 install fpdf --break-system-packages
```
- Función de conversión de texto a PDF:
```
from fpdf import FPDF

def texto_a_pdf(text, filename="salida.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.cell(0, 10, txt=line, ln=True)

    pdf.output(filename)
```
Esta función recibe un texto en formato Markdown (o texto plano) y genera un archivo salida.pdf con el contenido formateado en líneas.

#### Conversión de tabla a Excel y posteriormente a PDF
En este ejercicio se ha trabajado con un conjunto de datos representados mediante un diccionario de Python, que posteriormente se transforma en una tabla Excel y finalmente en un documento PDF.

- Instalación de librerías necesarias:
```
pip3 install pandas --break-system-packages
pip3 install odfpy --break-system-packages
```
- Creación del archivo Excel a partir de un diccionario:
```
import pandas as pd

diccionario = [
    {
        "titular": "Noticia 1",
        "fecha": "2025-12-09",
        "contenido": "Este es el contenido de la noticia 1"
    },
    {
        "titular": "Noticia 2",
        "fecha": "2025-12-10",
        "contenido": "Este es el contenido de la noticia 2"
    },
    {
        "titular": "Noticia 3",
        "fecha": "2025-12-11",
        "contenido": "Este es el contenido de la noticia 3"
    }
]

# Convertir a DataFrame
df = pd.DataFrame(diccionario)

# Exportar a Excel
df.to_excel("noticias.xlsx", index=False)
```
Este código crea un archivo noticias.xlsx a partir de los datos proporcionados.

#### Conversión de la tabla a PDF
Una vez generado el archivo Excel, se utiliza nuevamente la librería fpdf para convertir la tabla a un documento PDF.
```
from fpdf import FPDF
import pandas as pd

diccionario = [
    {
        "titular": "Noticia 1",
        "fecha": "2025-12-09",
        "contenido": "Este es el contenido de la noticia 1"
    },
    {
        "titular": "Noticia 2",
        "fecha": "2025-12-10",
        "contenido": "Este es el contenido de la noticia 2"
    },
    {
        "titular": "Noticia 3",
        "fecha": "2025-12-11",
        "contenido": "Este es el contenido de la noticia 3"
    }
]

# Convertir a DataFrame
df = pd.DataFrame(diccionario)

# Exportar a Excel
df.to_excel("noticias.xlsx", index=False)

# Convertir a PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

for i, row in df.iterrows():
    for j, value in enumerate(row):
        pdf.cell(0, 10, txt=str(value), ln=True, border=1)
    pdf.ln()

pdf.output("noticias.pdf")
```
Este script genera correctamente el archivo noticias.pdf, que contiene la tabla exportada desde el DataFrame.

---
A través de esta actividad se ha aprendido a convertir y adaptar documentos utilizando Python y bibliotecas especializadas como fpdf y pandas. Se ha trabajado la transformación de texto Markdown a PDF, así como la conversión de datos tabulares a Excel y posteriormente a PDF, aplicando procesos de automatización y generación de documentos. 

Esta práctica refuerza el uso de Python como herramienta versátil para la gestión de información y la creación de documentos portables, fundamentales en entornos profesionales donde se requiere interoperabilidad entre distintos formatos.
