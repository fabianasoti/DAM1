# pip3 install ttkbootstrap
# pip3 install --user --upgrade Pillow --break-system-packages

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as tb
import mysql.connector

# Conexión a la BD
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()

# Ventana con tema moderno
ventana = tb.Window(themename="superhero")  # Puedes probar: minty, litera, journal...
ventana.title("Gestión de Clientes")

# Frame Formulario
frame_form = tb.LabelFrame(ventana, text="Nuevo Cliente", bootstyle="primary")
frame_form.pack(side=tk.LEFT, padx=20, pady=20)

# Campos
labels = ["DNI/NIE:", "Nombre:", "Apellidos:", "Email:"]
entries = []
for i, texto in enumerate(labels):
    tk.Label(frame_form, text=texto).grid(row=i, column=0, sticky="w", padx=5, pady=8)
    entry = tb.Entry(frame_form)
    entry.grid(row=i, column=1, pady=8, padx=5)
    entries.append(entry)

dninie, nombre, apellidos, email = entries

# Frame Tabla
frame_tabla = tb.LabelFrame(ventana, text="Listado de Clientes", bootstyle="success")
frame_tabla.pack(side=tk.RIGHT, padx=20, pady=20)

# Scrollbar
scroll = ttk.Scrollbar(frame_tabla)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Treeview
arbol = ttk.Treeview(
    frame_tabla,
    columns=("dninie", "nombre", "apellidos", "email"),
    show="headings",
    yscrollcommand=scroll.set,
    height=15
)

for col, text in zip(("dninie", "nombre", "apellidos", "email"), labels):
    arbol.heading(col, text=text)

arbol.pack(padx=5, pady=5)
scroll.config(command=arbol.yview)


def cargar_tabla():
    arbol.delete(*arbol.get_children())
    cursor.execute("SELECT * FROM clientes")
    for fila in cursor.fetchall():
        arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))


def insertar():
    try:
        consulta = """
        INSERT INTO clientes (dninie, nombre, apellidos, email)
        VALUES (%s, %s, %s, %s)
        """
        datos = (dninie.get(), nombre.get(), apellidos.get(), email.get())

        if not all(datos):
            messagebox.showwarning("Aviso", "Rellena todos los campos")
            return

        cursor.execute(consulta, datos)
        conexion.commit()

        cargar_tabla()
        messagebox.showinfo("Éxito", "Cliente añadido correctamente")

        for entry in entries:
            entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo insertar el cliente: {e}")


# Botón insert
boton_insertar = tb.Button(
    frame_form,
    text="Insertar Cliente",
    bootstyle="success-outline",
    command=insertar
)
boton_insertar.grid(row=5, columnspan=2, pady=15)


cargar_tabla()

ventana.mainloop()

cursor.close()
conexion.close()


