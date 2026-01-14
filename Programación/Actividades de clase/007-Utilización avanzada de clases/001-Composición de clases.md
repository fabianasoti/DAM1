```
'''
Uso de herencia y clases en una escuela virtual
2026 Fabiana Sotillo
Programa que representa alumnos y profesores mediante herencia
e incorpora hobbies como propiedad adicional.
'''
```

---
En esta unidad se ha trabajado el concepto de herencia en programación orientada a objetos, una técnica fundamental que permite organizar el código de forma eficiente, reutilizando estructuras comunes y especializándolas según las necesidades del programa. A través del ejemplo de una escuela virtual con alumnos y profesores, se representa una situación real en la que distintas personas comparten características comunes, pero también poseen comportamientos específicos. 

El objetivo principal de este ejercicio es comprender cómo crear una superclase, generar subclases a partir de ella y añadir propiedades adicionales, como hobbies, para personalizar los objetos.

---
1. El programa empieza con la creación de una superclase llamada Persona, que contiene los atributos básicos de cualquier usuario de la escuela: nombre, apellidos, email y dirección. Esta clase incluye además un método llamado dameDatos, que devuelve el nombre completo de la persona.
```
class Persona():
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        self.hobby = hobby

    def dameDatos(self):
        return self.nombre + " " + self.apellidos
```
1.1. Se incorpora una propiedad adicional llamada hobby, junto con un método que permite mostrar dicho hobby, integrando así los intereses personales dentro del modelo de clases.        
```
    def mostrarHobby(self):
        return "Mi hobby es: " + self.hobby
```
       
2. A partir de esta superclase se crean dos subclases principales: Profesor y Alumno, que heredan todos los atributos y métodos de Persona. 
```
class Profesor(Persona):
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        super().__init__(nombre, apellidos, email, direccion, hobby)

    def mostrarProfesor(self):
        return "Profesor: " + self.dameDatos()


class Alumno(Persona):
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        super().__init__(nombre, apellidos, email, direccion, hobby)

    def mostrarAlumno(self):
        return "Alumno: " + self.dameDatos()
```
        
3. Posteriormente, se definen dos tipos de alumnos: AlumnoOnline y AlumnoPresencial, que heredan de la clase Alumno, permitiendo representar los distintos métodos de asistencia.
```
class AlumnoOnline(Alumno):
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        super().__init__(nombre, apellidos, email, direccion, hobby)


class AlumnoPresencial(Alumno):
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        super().__init__(nombre, apellidos, email, direccion, hobby)
```     
Esta estructura jerárquica facilita la reutilización del código y permite representar de forma clara las relaciones entre los distintos tipos de personas dentro de la escuela virtual.

---
A continuación se muestra el código completo:
```
'''
Uso de herencia y clases en una escuela virtual
2026 Fabiana Sotillo
Programa que representa alumnos y profesores mediante herencia
e incorpora hobbies como propiedad adicional.
'''

class Persona():
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        self.hobby = hobby

    def dameDatos(self):
        return self.nombre + " " + self.apellidos

    def mostrarHobby(self):
        return "Mi hobby es: " + self.hobby


class Profesor(Persona):
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        super().__init__(nombre, apellidos, email, direccion, hobby)

    def mostrarProfesor(self):
        return "Profesor: " + self.dameDatos()


class Alumno(Persona):
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        super().__init__(nombre, apellidos, email, direccion, hobby)

    def mostrarAlumno(self):
        return "Alumno: " + self.dameDatos()


class AlumnoOnline(Alumno):
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        super().__init__(nombre, apellidos, email, direccion, hobby)


class AlumnoPresencial(Alumno):
    def __init__(self, nombre, apellidos, email, direccion, hobby):
        super().__init__(nombre, apellidos, email, direccion, hobby)


alumno1 = AlumnoOnline("Jose Vicente", "Carratala", "info@jocarsa.com", "Direccion", "Bailar")
print(alumno1.mostrarAlumno())
print(alumno1.mostrarHobby())

profesor1 = Profesor("Juan", "Garcia", "juan@jocarsa.com", "Direccion", "Cantar")
print(profesor1.mostrarProfesor())
print(profesor1.mostrarHobby())
```

---
El programa crea correctamente objetos de tipo AlumnoOnline y Profesor, mostrando por pantalla sus datos personales y su hobby. De este modo se comprueba el correcto funcionamiento de la herencia y el uso de métodos propios de cada clase.

Este ejercicio permite aplicar de forma práctica el uso de herencia y programación orientada a objetos en Python. A través del ejemplo de una escuela virtual con profesores y alumnos, se refuerza la comprensión de cómo organizar el código mediante una superclase y varias subclases, reutilizando atributos y métodos comunes.

Además, la incorporación de hobbies demuestra cómo se pueden personalizar los objetos para adaptarlos a distintos contextos. 

Estos conceptos son fundamentales para el desarrollo de aplicaciones más complejas y resultan especialmente útiles en proyectos donde sea necesario modelar estructuras jerárquicas y relaciones entre distintos tipos de usuarios.
