import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Conexión a la BD
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()

ventana = tk.Tk()
ventana.title("Gestión de Clientes")

# Frame de formulario
frame_form = tk.LabelFrame(ventana, text="Insertar Cliente", padx=10, pady=10)
frame_form.pack(side=tk.LEFT, padx=20, pady=20)

# DNI NIE
tk.Label(frame_form, text="DNI/NIE:").grid(row=0, column=0, sticky="w")
dninie = tk.Entry(frame_form)
dninie.grid(row=0, column=1, pady=5)

# Nombre
tk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w")
nombre = tk.Entry(frame_form)
nombre.grid(row=1, column=1, pady=5)

# Apellidos
tk.Label(frame_form, text="Apellidos:").grid(row=2, column=0, sticky="w")
apellidos = tk.Entry(frame_form)
apellidos.grid(row=2, column=1, pady=5)

# Email
tk.Label(frame_form, text="Email:").grid(row=3, column=0, sticky="w")
email = tk.Entry(frame_form)
email.grid(row=3, column=1, pady=5)


def cargar_tabla():
    arbol.delete(*arbol.get_children())  # Limpiar tabla
    cursor.execute("SELECT * FROM clientes")
    filas = cursor.fetchall()
    for fila in filas:
        arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))


def insertar():
    try:
        consulta = """
        INSERT INTO clientes (dninie, nombre, apellidos, email)
        VALUES (%s, %s, %s, %s)
        """
        datos = (dninie.get(), nombre.get(), apellidos.get(), email.get())
        cursor.execute(consulta, datos)
        conexion.commit()

        cargar_tabla()

        messagebox.showinfo("Éxito", "Cliente insertado correctamente")

        dninie.delete(0, tk.END)
        nombre.delete(0, tk.END)
        apellidos.delete(0, tk.END)
        email.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo insertar: {e}")


tk.Button(frame_form, text="Insertar", command=insertar).grid(row=4, columnspan=2, pady=10)

# Frame tabla
frame_tabla = tk.LabelFrame(ventana, text="Listado de Clientes", padx=10, pady=10)
frame_tabla.pack(side=tk.RIGHT, padx=20, pady=20)

arbol = ttk.Treeview(frame_tabla, columns=("dninie", "nombre", "apellidos", "email"), show="headings")
arbol.heading("dninie", text="DNI/NIE")
arbol.heading("nombre", text="Nombre")
arbol.heading("apellidos", text="Apellidos")
arbol.heading("email", text="Email")

arbol.pack()

cargar_tabla()

ventana.mainloop()

cursor.close()
conexion.close()

