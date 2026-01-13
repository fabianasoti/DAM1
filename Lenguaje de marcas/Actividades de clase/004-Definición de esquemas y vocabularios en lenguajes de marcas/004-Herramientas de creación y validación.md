```
'''
Curriculum Vitae formato XML
2026 Fabiana Sotillo
Herramientas de creación y validación XML y  XSD
'''
```

---
XML (eXtensible Markup Language) es un lenguaje de marcado orientado al almacenamiento y transporte de información estructurada. Su principal característica es la posibilidad de definir etiquetas personalizadas, lo que permite adaptar la estructura de los documentos a cualquier tipo de información, como en este caso un currículum vitae.

Para garantizar que un documento XML sea válido, debe cumplir las siguientes normas fundamentales:
- Debe existir una única etiqueta raíz.
- Todas las etiquetas deben abrirse y cerrarse correctamente.
- Las etiquetas deben respetar la jerarquía y el anidamiento.
- El documento debe ser sensible a mayúsculas y minúsculas (case sensitive).
- Puede validarse mediante un esquema XSD que define su estructura.

En esta actividad se ha creado un currículum en formato XML siguiendo una estructura predefinida y posteriormente se ha generado un esquema XSD para validar que el documento cumple correctamente con dicha estructura.

Se trabaja la creación de un currículum vitae en formato XML, aplicando los conceptos fundamentales del lenguaje de marcado estructurado para la organización y validación de datos. 

XML permite definir etiquetas personalizadas y estructurar la información de forma jerárquica, lo que facilita su intercambio entre sistemas. 

---
A continuación, se muestra el currículum XML desarrollado.
```
<?xml version="1.0" encoding="UTF-8"?>
<curriculum>
	<datospersonales>
		<nombre>Fabiana Victoria</nombre>
		<apellidos>Sotillo</apellidos>
		<telefono>+34 663966940</telefono>
	</datospersonales>
	<competencias>
		<tecnicas>
			<tecnica>MySQL</tecnica>
			<tecnica>Python</tecnica>
			<tecnica>HTML y CSS</tecnica>
			<tecnica>Microsoft office</tecnica>
			<tecnica>Warehouse Management OS</tecnica>
		</tecnicas>
		<personales>
			<personal>Empatía y comunicación efectiva</personal>
			<personal>Organización y gestión eficiente de tareas y prioridades</personal>
			<personal>Puntualidad y responsabilidad en la entrega de resultados</personal>
			<personal>Capacidad resolutiva y adaptable</personal>
			<personal>Colaboración y trabajo en equipo</personal>
		</personales>
		<idiomas>
			<idioma>Inglés - Avanzado</idioma>
			<idioma>Español - Nativo</idioma>
		</idiomas>
	</competencias>
	<sobremi>
		<p>Profesional proactiva con experiencia en atención al cliente y análisis de existencias. En formación en Desarrollo de Aplicaciones Multiplataforma (DAM), con interés en el sector tecnológico. Destaco por mi adaptabilidad, comunicación y trabajo en equipo. Comprometida con el aprendizaje continuo y la mejora de procesos.</p>
	</sobremi>
</curriculum>
```

--- 
Con ayuda de chatGPT, tal y como dice en lel enunciado del ejercicio, se ha podido comprobar que: 
Este documento cumple con los requisitos básicos de XML: presenta una única etiqueta raíz <curriculum>, utiliza etiquetas correctamente anidadas y mantiene una estructura jerárquica clara. Y además se procede a generar el esquema XSD.

#### Generación del esquema XSD
A partir del documento XML se ha generado un esquema XSD que define la estructura del currículum y permite validar su contenido. El esquema establece los tipos de datos, los elementos obligatorios y el orden correcto de cada bloque.
```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <xsd:element name="curriculum">
    <xsd:complexType>
      <xsd:sequence>

        <xsd:element name="datospersonales">
          <xsd:complexType>
            <xsd:sequence>
              <xsd:element name="nombre" type="xsd:string"/>
              <xsd:element name="apellidos" type="xsd:string"/>
              <xsd:element name="telefono" type="xsd:string"/>
            </xsd:sequence>
          </xsd:complexType>
        </xsd:element>

        <xsd:element name="competencias">
          <xsd:complexType>
            <xsd:sequence>

              <xsd:element name="tecnicas">
                <xsd:complexType>
                  <xsd:sequence>
                    <xsd:element name="tecnica" type="xsd:string" maxOccurs="unbounded"/>
                  </xsd:sequence>
                </xsd:complexType>
              </xsd:element>

              <xsd:element name="personales">
                <xsd:complexType>
                  <xsd:sequence>
                    <xsd:element name="personal" type="xsd:string" maxOccurs="unbounded"/>
                  </xsd:sequence>
                </xsd:complexType>
              </xsd:element>

              <xsd:element name="idiomas">
                <xsd:complexType>
                  <xsd:sequence>
                    <xsd:element name="idioma" type="xsd:string" maxOccurs="unbounded"/>
                  </xsd:sequence>
                </xsd:complexType>
              </xsd:element>

            </xsd:sequence>
          </xsd:complexType>
        </xsd:element>

        <xsd:element name="sobremi">
          <xsd:complexType>
            <xsd:sequence>
              <xsd:element name="p" type="xsd:string"/>
            </xsd:sequence>
          </xsd:complexType>
        </xsd:element>

      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>

</xsd:schema>
```

---
A través de este ejercicio se ha aprendido a estructurar un currículum vitae en formato XML, aplicando correctamente el uso de etiquetas personalizadas, jerarquía de elementos y una única etiqueta raíz.
Además, se ha generado un esquema XSD que permite validar la estructura del documento y garantizar que cumple con los requisitos establecidos. 
Esta práctica refuerza la comprensión del uso de XML como herramienta fundamental para el intercambio de información estructurada entre sistemas y como base para el trabajo con tecnologías más avanzadas de validación y transformación de datos.
