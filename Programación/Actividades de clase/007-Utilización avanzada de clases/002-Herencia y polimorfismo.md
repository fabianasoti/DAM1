En este ejercicio se trabaja el concepto de herencia y polimorfismo en Python a través de un contexto práctico: la organización de un taller de programación para personas interesadas en actividades creativas como el crocheting o el arte latte. La herencia permite crear nuevas clases a partir de una clase base, reutilizando sus atributos y métodos, mientras que el polimorfismo permite que un mismo método se comporte de forma diferente según la clase que lo implemente. En este caso, se define una clase base llamada Persona y dos subclases llamadas Profesor y Alumno, que heredan sus propiedades básicas y redefinen el método dameDatos() para mostrar información personalizada. El objetivo del ejercicio es comprender cómo aplicar estos conceptos para modelar distintos tipos de personas dentro de un sistema.

Para resolver el ejercicio se ha definido una clase base Persona que contiene los atributos comunes nombre y apellidos, así como un método dameDatos() que devuelve una cadena con dichos datos. A partir de esta clase se crean dos subclases: Profesor y Alumno.

La herencia se implementa mediante el uso de super(), que permite reutilizar el constructor de la clase Persona sin duplicar código. El polimorfismo se aplica redefiniendo el método dameDatos() en cada subclase, de forma que cada una devuelve un mensaje diferente aunque el nombre del método sea el mismo.

De este modo, se consigue que un profesor y un alumno puedan ser tratados como personas, pero con un comportamiento específico al mostrar sus datos, integrándolos en el contexto del taller creativo de programación.

---

Se define la clase Persona con un constructor que inicializa el nombre y los apellidos.

Se define el método dameDatos() que devuelve una cadena con los datos de la persona.

Las clases Profesor y Alumno heredan de Persona usando super().

Ambas subclases redefinen el método dameDatos() aplicando polimorfismo.

Se crean dos objetos, uno de tipo Alumno y otro de tipo Profesor.

Se imprimen sus datos para comprobar el funcionamiento correcto.

A continuación se muestra el código completo y funcional:

```
''' 
Herencia y polimorfismo en un taller creativo
2025 Fabiana Victoria Sotillo
Programa que define una clase Persona y dos subclases (Profesor y Alumno),
aplicando herencia y polimorfismo para mostrar los datos de los participantes
de un taller de programación con hobbies creativos.
'''

class Persona():
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def dameDatos(self):
        return self.nombre + " " + self.apellidos


class Profesor(Persona):
    def __init__(self, nombre, apellidos):
        super().__init__(nombre, apellidos)

    def dameDatos(self):
        return "Profesor: " + self.nombre + " " + self.apellidos


class Alumno(Persona):
    def __init__(self, nombre, apellidos):
        super().__init__(nombre, apellidos)

    def dameDatos(self):
        return "Alumno: " + self.nombre + " " + self.apellidos


# Creación de objetos
alumno1 = Alumno("Jose Vicente", "Carratala")
profesor1 = Profesor("Juan", "Garcia")

# Mostrar datos
print(alumno1.dameDatos())
print(profesor1.dameDatos())
```

---
En este ejercicio se han aplicado los conceptos de herencia y polimorfismo para modelar un sistema sencillo de gestión de personas dentro de un taller de programación con intereses creativos como el crocheting o el arte latte. La herencia permite reutilizar código común en la clase Persona, mientras que el polimorfismo permite personalizar el comportamiento del método dameDatos() según el tipo de objeto. Estos conceptos son fundamentales en la programación orientada a objetos y pueden aplicarse en sistemas reales como plataformas educativas, sistemas de gestión escolar o aplicaciones laborales, donde distintos tipos de usuarios comparten características comunes pero requieren comportamientos específicos. Su correcta aplicación facilita la organización del código, mejora su reutilización y permite crear programas más estructurados y escalables.
