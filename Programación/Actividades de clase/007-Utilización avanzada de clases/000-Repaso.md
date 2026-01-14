```
'''
Simulación NPCs en movimiento con Flask
2026 Fabiana Sotillo
Programa que genera 50 personajes con movimiento aleatorio y los muestra
en una aplicación web mediante una API en Flask.
'''
```

---
En este ejercicio se desarrolla una aplicación interactiva que simula el movimiento de personajes en una pantalla web utilizando Python y Flask. A través del uso de programación orientada a objetos, trigonometría y generación de valores aleatorios, se representa el comportamiento de personajes que se desplazan de forma autónoma dentro de un escenario. El objetivo principal es comprender cómo se pueden crear objetos en movimiento, actualizar sus posiciones en tiempo real y exponer estos datos mediante una API para ser visualizados en una interfaz web.

El programa se basa en la creación de una clase llamada Npc, que representa a cada personaje del juego. 
- Cada objeto de esta clase contiene información sobre su posición, radio, dirección y velocidad. 
- Para simular el movimiento, se utiliza trigonometría mediante las funciones cos() y sin() del módulo math, que permiten calcular el desplazamiento en función del ángulo de dirección.
- Se generan 50 personajes con valores aleatorios para sus atributos iniciales.

Posteriormente, se configura un servidor Flask que ofrece dos rutas principales:
- Ruta principal ( / ): muestra una página HTML llamada juego.html donde se visualizan los personajes.
- Ruta API ( /api ): devuelve en formato JSON la posición actualizada de todos los personajes tras aplicar el movimiento.

Cada vez que se consulta la API, los personajes se mueven, modificando su dirección de forma aleatoria y rebotando contra los bordes de la pantalla, lo que crea un comportamiento dinámico y realista.

---
A continuación se muestra el código funcional completo:
```
'''
Simulación de personajes en movimiento con Flask
2026 Fabiana Sotillo
Programa que genera 50 personajes con movimiento aleatorio y los muestra
en una aplicación web mediante una API en Flask.
'''

import random
import json
from flask import Flask, render_template
import math  # Para poder hacer trigonometría


class Npc():
    def __init__(self, x, y, radio, direccion, velocidad): 
        self.posx = x
        self.posy = y
        self.radio = radio
        self.direccion = direccion 
        self.velocidad = velocidad 

    def to_dict(self):
        return {
            "posx": self.posx, 
            "posy": self.posy,
            "radio": self.radio,
            "direccion": self.direccion 
        }

    def mover(self):
        # Aplicamos variación de la dirección con el tiempo
        self.direccion += (random.random() - 0.5) * 0.2

        # Colisión con paredes
        if self.posx > 500 or self.posx < 0 or self.posy > 500 or self.posy < 0:
            self.direccion += math.pi  # El personaje se da la vuelta

        self.posx += math.cos(self.direccion) * self.velocidad
        self.posy += math.sin(self.direccion) * self.velocidad 


# Creamos los personajes
personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    xaleatoria = random.randint(0, 500)
    yaleatoria = random.randint(0, 500)
    radioaleatorio = random.randint(10, 30)
    direccionaleatoria = random.random() * math.pi * 2 
    velocidadaleatoria = random.random() * 5 

    personajes.append(
        Npc(
            xaleatoria, 
            yaleatoria,
            radioaleatorio,
            direccionaleatoria,
            velocidadaleatoria 
        ) 
    )


# Servidor Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("juego.html")

@app.route("/api")
def api():
    # Movemos todos los personajes
    for personaje in personajes:	
        personaje.mover()

    personajes_json = [p.to_dict() for p in personajes]
    return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
    app.run(debug=True)

```

---
Al ejecutar el servidor Flask y acceder desde el navegador, se mostrará una pantalla web donde se visualizan los 50 personajes moviéndose de forma aleatoria. Cada vez que se consulta la API, las posiciones se actualizan, simulando movimiento continuo.

Este ejercicio permite aplicar de forma práctica conceptos de trigonometría, programación orientada a objetos y desarrollo de APIs con Flask. 

A través de la simulación de personajes en movimiento, se refuerza la comprensión del uso de clases, métodos y estructuras de control, así como la integración de un backend con una interfaz web. 

El resultado final es una aplicación funcional que demuestra cómo se pueden manipular objetos en tiempo real dentro de un sistema interactivo, un concepto fundamental en el desarrollo de videojuegos, simulaciones y aplicaciones web dinámicas.
