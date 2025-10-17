import sqlite3
import os

# ==============================
# ANSI COLOR CODES
# ==============================
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"

# ==============================
# DATABASE SETUP
# ==============================
conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT NOT NULL
);
""")

# ==============================
# HELPER FUNCTIONS
# ==============================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(f"{BOLD}{MAGENTA}==============================")
    print(f"     AGENDA SQLite v1.1")
    print(f"     By Fabiana Victoria Sotillo")
    print(f"=============================={RESET}\n")

def show_menu():
    print(f"{CYAN}Escoge una opción:{RESET}")
    print(f"{YELLOW}1.{RESET} Crear cliente")
    print(f"{YELLOW}2.{RESET} Listar clientes")
    print(f"{YELLOW}3.{RESET} Actualizar cliente")
    print(f"{YELLOW}4.{RESET} Eliminar cliente")
    print(f"{YELLOW}5.{RESET} Salir del programa")
    print(f"{YELLOW}6.{RESET} Buscar cliente\n")

def pause():
    input(f"\n{CYAN}Presiona Enter para continuar...{RESET}")

def mostrar_clientes(filas=None):
    """Muestra la tabla de clientes con formato."""
    if filas is None:
        cursor.execute("SELECT * FROM clientes;")
        filas = cursor.fetchall()

    if not filas:
        print(f"{YELLOW}No hay clientes registrados.{RESET}")
    else:
        print(f"\n{BOLD}{MAGENTA}{'ID':<5}{'NOMBRE':<20}{'APELLIDOS':<25}{'EMAIL'}{RESET}")
        print("-" * 70)
        for fila in filas:
            print(f"{fila[0]:<5}{fila[1]:<20}{fila[2]:<25}{fila[3]}")

# ==============================
# MAIN LOOP
# ==============================
while True:
    print_header()
    show_menu()

    try:
        opcion = int(input(f"{BOLD}Selecciona una opción: {RESET}"))
    except ValueError:
        print(f"{RED}Por favor, introduce un número válido.{RESET}")
        pause()
        continue

    if opcion == 1:
        print(f"\n{BOLD}{CYAN}=== Crear nuevo cliente ==={RESET}")
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        email = input("Email: ").strip()

        if not (nombre and apellidos and email):
            print(f"{RED}Error: Todos los campos son obligatorios.{RESET}")
        else:
            cursor.execute(
                "INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)",
                (nombre, apellidos, email)
            )
            conexion.commit()
            print(f"{GREEN}Cliente agregado correctamente.{RESET}")

        pause()

    elif opcion == 2:
        print(f"\n{BOLD}{CYAN}=== Lista de clientes ==={RESET}")
        mostrar_clientes()
        pause()

    elif opcion == 3:
        print(f"\n{BOLD}{CYAN}=== Actualizar cliente ==={RESET}")
        mostrar_clientes()

        identificador = input("\nIntroduce el Identificador del cliente a actualizar: ")
        cursor.execute("SELECT * FROM clientes WHERE Identificador = ?", (identificador,))
        cliente = cursor.fetchone()

        if cliente:
            print(f"\nCliente actual: {cliente[1]} {cliente[2]} ({cliente[3]})")
            nombre = input("Nuevo nombre (deja vacío para no cambiar): ").strip() or cliente[1]
            apellidos = input("Nuevos apellidos (deja vacío para no cambiar): ").strip() or cliente[2]
            email = input("Nuevo email (deja vacío para no cambiar): ").strip() or cliente[3]

            cursor.execute("""
                UPDATE clientes
                SET nombre = ?, apellidos = ?, email = ?
                WHERE Identificador = ?
            """, (nombre, apellidos, email, identificador))
            conexion.commit()
            print(f"{GREEN}Cliente actualizado correctamente.{RESET}")
        else:
            print(f"{RED}No se encontró un cliente con ese Identificador.{RESET}")
        pause()

    elif opcion == 4:
        print(f"\n{BOLD}{CYAN}=== Eliminar cliente ==={RESET}")
        mostrar_clientes()

        identificador = input("\nIntroduce el Identificador del cliente a eliminar: ")

        cursor.execute("SELECT * FROM clientes WHERE Identificador = ?", (identificador,))
        cliente = cursor.fetchone()

        if cliente:
            print(f"{YELLOW}¿Seguro que deseas eliminar a {cliente[1]} {cliente[2]}? (s/n){RESET}")
            confirm = input("> ").lower()
            if confirm == "s":
                cursor.execute("DELETE FROM clientes WHERE Identificador = ?", (identificador,))
                conexion.commit()
                print(f"{GREEN}Cliente eliminado correctamente.{RESET}")
            else:
                print(f"{CYAN}Operación cancelada.{RESET}")
        else:
            print(f"{RED}No se encontró un cliente con ese Identificador.{RESET}")
        pause()

    elif opcion == 5:
        print(f"{GREEN}Bye bye 👋{RESET}")
        break

    elif opcion == 6:
        print(f"\n{BOLD}{CYAN}=== Buscar cliente ==={RESET}")
        criterio = input("Introduce nombre, email o ID a buscar: ").strip()

        if not criterio:
            print(f"{RED}Debes introducir algo para buscar.{RESET}")
        else:
            # Try to interpret as ID first
            if criterio.isdigit():
                cursor.execute("SELECT * FROM clientes WHERE Identificador = ?", (criterio,))
                filas = cursor.fetchall()
            else:
                like_pattern = f"%{criterio}%"
                cursor.execute("""
                    SELECT * FROM clientes
                    WHERE nombre LIKE ? OR apellidos LIKE ? OR email LIKE ?
                """, (like_pattern, like_pattern, like_pattern))
                filas = cursor.fetchall()

            if filas:
                print(f"{GREEN}\nResultados de la búsqueda:{RESET}")
                mostrar_clientes(filas)
            else:
                print(f"{YELLOW}No se encontraron resultados para '{criterio}'.{RESET}")

        pause()

    else:
        print(f"{RED}Opción no válida.{RESET}")
        pause()

conexion.close()


