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
WHITE = "\033[97m"

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
    border = f"{MAGENTA}{'═'*50}{RESET}"
    print(border)
    print(f"{BOLD}{MAGENTA}║{'AGENDA SQLITE v1.2':^48}║{RESET}")
    print(f"{BOLD}{CYAN}║{'By Fabiana Victoria Sotillo':^48}║{RESET}")
    print(border + "\n")

def show_menu():
    border = f"{MAGENTA}{'─'*40}{RESET}"
    print(border)
    print(f"{BOLD}{CYAN}📋  MENÚ PRINCIPAL{RESET}")
    print(border)
    print(f"{YELLOW}1.{RESET} ➤ Crear cliente")
    print(f"{YELLOW}2.{RESET} ➤ Listar clientes")
    print(f"{YELLOW}3.{RESET} ➤ Actualizar cliente")
    print(f"{YELLOW}4.{RESET} ➤ Eliminar cliente")
    print(f"{YELLOW}5.{RESET} ➤ Salir del programa")
    print(f"{YELLOW}6.{RESET} ➤ Buscar cliente 🔍")
    print(border + "\n")

def pause():
    input(f"\n{CYAN}Presiona Enter para continuar...{RESET}")

def mostrar_clientes(filas=None):
    """Muestra la tabla de clientes con formato."""
    if filas is None:
        cursor.execute("SELECT * FROM clientes;")
        filas = cursor.fetchall()

    print(f"\n{BOLD}{MAGENTA}╔{'═'*70}╗{RESET}")
    print(f"{BOLD}{MAGENTA}║{RESET}{'ID':^5}{'|':^3}{'NOMBRE':^20}{'|':^3}{'APELLIDOS':^25}{'|':^3}{'EMAIL':^20}{BOLD}{MAGENTA}║{RESET}")
    print(f"{BOLD}{MAGENTA}╠{'═'*70}╣{RESET}")

    if not filas:
        print(f"{YELLOW}║{'No hay clientes registrados.':^70}║{RESET}")
    else:
        for fila in filas:
            print(f"{WHITE}║{RESET}{str(fila[0]):^5}{'|':^3}{fila[1][:18]:<20}{'|':^3}{fila[2][:23]:<25}{'|':^3}{fila[3][:18]:<20}{WHITE}║{RESET}")

    print(f"{BOLD}{MAGENTA}╚{'═'*70}╝{RESET}")

# ==============================
# MAIN LOOP
# ==============================
while True:
    print_header()
    show_menu()

    try:
        opcion = int(input(f"{BOLD}{WHITE}Selecciona una opción: {RESET}"))
    except ValueError:
        print(f"{RED}❌ Por favor, introduce un número válido.{RESET}")
        pause()
        continue

    if opcion == 1:
        print(f"\n{BOLD}{CYAN}╔════════════════════════════════════╗")
        print(f"║     🧾 CREAR NUEVO CLIENTE        ║")
        print(f"╚════════════════════════════════════╝{RESET}")
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        email = input("Email: ").strip()

        if not (nombre and apellidos and email):
            print(f"{RED}❌ Error: Todos los campos son obligatorios.{RESET}")
        else:
            cursor.execute(
                "INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)",
                (nombre, apellidos, email)
            )
            conexion.commit()
            print(f"{GREEN}✅ Cliente agregado correctamente.{RESET}")

        pause()

    elif opcion == 2:
        print(f"\n{BOLD}{CYAN}╔════════════════════════════════════╗")
        print(f"║     📋 LISTA DE CLIENTES          ║")
        print(f"╚════════════════════════════════════╝{RESET}")
        mostrar_clientes()
        pause()

    elif opcion == 3:
        print(f"\n{BOLD}{CYAN}╔════════════════════════════════════╗")
        print(f"║     ✏️  ACTUALIZAR CLIENTE        ║")
        print(f"╚════════════════════════════════════╝{RESET}")
        mostrar_clientes()

        identificador = input("\nIntroduce el ID del cliente a actualizar: ")
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
            print(f"{GREEN}✅ Cliente actualizado correctamente.{RESET}")
        else:
            print(f"{RED}❌ No se encontró un cliente con ese ID.{RESET}")
        pause()

    elif opcion == 4:
        print(f"\n{BOLD}{CYAN}╔════════════════════════════════════╗")
        print(f"║     🗑️  ELIMINAR CLIENTE          ║")
        print(f"╚════════════════════════════════════╝{RESET}")
        mostrar_clientes()

        identificador = input("\nIntroduce el ID del cliente a eliminar: ")

        cursor.execute("SELECT * FROM clientes WHERE Identificador = ?", (identificador,))
        cliente = cursor.fetchone()

        if cliente:
            print(f"{YELLOW}⚠️ ¿Seguro que deseas eliminar a {cliente[1]} {cliente[2]}? (s/n){RESET}")
            confirm = input("> ").lower()
            if confirm == "s":
                cursor.execute("DELETE FROM clientes WHERE Ident

