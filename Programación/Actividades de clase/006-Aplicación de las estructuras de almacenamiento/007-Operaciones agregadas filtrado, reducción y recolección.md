```
'''
Sudoku 
2026 Fabiana Sotillo
Programa que genera un tablero de Sudoku 
en una interfaz web con matrices bidimensionales.
'''
```

---
En este ejercicio se trabajan matrices bidimensionales y generación de datos aleatorios aplicados a un contexto lúdico y práctico. Inspirado en el entrenamiento mental para torneos de League of Legends (LOL), se desarrolla un programa que genera tableros de Sudoku de 9x9 y permite eliminar números de forma aleatoria para convertirlo en un juego interactivo. 

El objetivo principal es aplicar el uso de matrices bidimensionales, funciones y estructuras de control para crear una aplicación funcional que combine lógica, estrategia y programación.

---
1. El programa se basa en la creación de una matriz bidimensional de 9x9 que representa un tablero de Sudoku. 
```
def es_valido(grid, fila, col, num):
    # Comprueba si el número puede colocarse en la posición indicada

    if num in grid[fila]:
        return False

    for f in range(9):
        if grid[f][col] == num:
            return False

    bloque_fila = (fila // 3) * 3
    bloque_col = (col // 3) * 3
    for f in range(bloque_fila, bloque_fila + 3):
        for c in range(bloque_col, bloque_col + 3):
            if grid[f][c] == num:
                return False

    return True
```

2. Para ello se utiliza un algoritmo de backtracking que rellena la matriz respetando las reglas del juego: cada fila, columna y bloque 3x3 debe contener los números del 1 al 9 sin repetir.
```
def resolver_sudoku(grid):
    # Algoritmo de backtracking para resolver el Sudoku

    for fila in range(9):
        for col in range(9):
            if grid[fila][col] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)

                for num in numeros:
                    if es_valido(grid, fila, col, num):
                        grid[fila][col] = num
                        if resolver_sudoku(grid):
                            return True
                        grid[fila][col] = 0
                return False
    return True
```

3. Una vez generado el tablero completo, se añade una función que elimina un número aleatorio de cada fila, asegurando que no se repite la eliminación en la misma posición.

```
def eliminar_numero(tablero):
		# Elimina un número aleatorio de cada fila

		for fila in range(9):
				columna = random.randint(0, 8)
				tablero[fila][columna] = 0
```

4. Posteriormente, se utiliza Flask para crear una interfaz web que muestra el tablero al usuario.
```
@app.route("/")
def inicio():
    sudoku = generar_tablero_sudoku()
    eliminar_numero(sudoku)
    datos = sudoku_a_bloques(sudoku)
    return render_template("index2.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)
```

La aplicación permite visualizar el Sudoku generado y practicar eliminando números, simulando un juego de entrenamiento mental que combina estrategia, memoria y concentración, habilidades muy útiles en videojuegos.

---
A continuación se muestra el código funcional completo:
```
'''
Generación de tableros de Sudoku con matrices bidimensionales
2026 Fabiana Sotillo
Programa que genera un tablero de Sudoku válido y lo muestra en una interfaz web
para practicar memoria y estrategia.
'''

import random
from flask import Flask, render_template

app = Flask(__name__)


def es_valido(grid, fila, col, num):
    # Comprueba si el número puede colocarse en la posición indicada

    if num in grid[fila]:
        return False

    for f in range(9):
        if grid[f][col] == num:
            return False

    bloque_fila = (fila // 3) * 3
    bloque_col = (col // 3) * 3
    for f in range(bloque_fila, bloque_fila + 3):
        for c in range(bloque_col, bloque_col + 3):
            if grid[f][c] == num:
                return False

    return True


def resolver_sudoku(grid):
    # Algoritmo de backtracking para resolver el Sudoku

    for fila in range(9):
        for col in range(9):
            if grid[fila][col] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)

                for num in numeros:
                    if es_valido(grid, fila, col, num):
                        grid[fila][col] = num
                        if resolver_sudoku(grid):
                            return True
                        grid[fila][col] = 0
                return False
    return True


def generar_tablero_sudoku():
    # Genera un tablero completo de Sudoku válido

    tablero = [[0 for _ in range(9)] for _ in range(9)]
    resolver_sudoku(tablero)
    return tablero


def eliminar_numero(tablero):
    # Elimina un número aleatorio de cada fila

    for fila in range(9):
        columna = random.randint(0, 8)
        tablero[fila][columna] = 0


def sudoku_a_bloques(sudoku):
    # Convierte la matriz 9x9 en bloques 3x3

    bloques = []
    for br in range(3):
        for bc in range(3):
            bloque = []
            for r in range(br * 3, br * 3 + 3):
                for c in range(bc * 3, bc * 3 + 3):
                    bloque.append(sudoku[r][c])
            bloques.append(bloque)
    return bloques


@app.route("/")
def inicio():
    sudoku = generar_tablero_sudoku()
    eliminar_numero(sudoku)
    datos = sudoku_a_bloques(sudoku)
    return render_template("index.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)
```

---
El programa genera un tablero de Sudoku completo y válido utilizando una matriz bidimensional. Posteriormente, elimina un número aleatorio de cada fila y muestra el tablero en una interfaz web. Cada vez que se recarga la página, se genera un nuevo tablero con números eliminados, permitiendo al usuario entrenar su memoria y estrategia.

Este ejercicio permite aplicar de forma práctica los conceptos aprendidos sobre matrices bidimensionales, funciones y estructuras de control en Python. 

A través de la generación de tableros de Sudoku, se refuerza la lógica algorítmica y el pensamiento estratégico, habilidades muy útiles tanto en videojuegos como League of Legends como en actividades creativas y técnicas relacionadas con el arte latte. 

Además, la integración con Flask es sumamente útil en el desarrollo de aplicaciones interactivas, demostrando cómo la programación puede utilizarse para crear juegos y herramientas de entrenamiento mental y lúdicos.
