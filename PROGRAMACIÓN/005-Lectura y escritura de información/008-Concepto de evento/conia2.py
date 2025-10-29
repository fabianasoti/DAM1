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

# Ventana con tema pastel elegante
ventana = tb.Window(themename="lumen")
ventana.title("Gestión de Clientes 🌸")
ventana.geometry("900x500")

# Frame Formulario
frame_form = tb.LabelFrame(
    ventana,
    text="Nuevo Cliente",
    bootstyle="info",
    padding=10
)
frame_form.pack(side=tk.LEFT, padx=25, pady=25)

# Campos
labels = ["DNI/NIE:", "Nombre:", "Apellidos:", "Email:"]
entries = []
for i, texto in enumerate(labels):
    etiqueta = tb.Label(frame_form, text=texto, font=("Segoe UI", 11))
    etiqueta.grid(row=i, column=0, sticky="w", padx=5, pady=8)
    entry = tb.Entry(frame_form, width=25)
    entry.grid(row=i, column=1, pady=8, padx=5)
    entries.append(entry)

dninie, nombre, apellidos, email = entries

# Frame Tabla
frame_tabla = tb.LabelFrame(
    ventana,
    text="Listado de Clientes",
    bootstyle="secondary",
    padding=10
)
frame_tabla.pack(side=tk.RIGHT, padx=25, pady=25)

# Scrollbar
scroll = ttk.Scrollbar(frame_tabla)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Tabla
arbol = ttk.Treeview(
    frame_tabla,
    columns=("dninie", "nombre", "apellidos", "email"),
    show="headings",
    yscrollcommand=scroll.set,
    height=18
)

for col, text in zip(("dninie", "nombre", "apellidos", "email"), labels):
    arbol.heading(col, text=text)
    arbol.column(col, anchor="center", width=140)

arbol.pack(padx=5, pady=5)
scroll.config(command=arbol.yview)


def cargar_tabla():
    arbol.delete(*arbol.get_children())
    cursor.execute("SELECT * FROM clientes")
    for fila in cursor.fetchall():
        arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))


def insertar():
    try:
        datos = (dninie.get(), nombre.get(), apellidos.get(), email.get())

        if not all(datos):
            messagebox.showwarning("Aviso ✨", "Completa todos los campos, porfi.")
            return

        cursor.execute(
            "INSERT INTO clientes (dninie, nombre, apellidos, email) VALUES (%s, %s, %s, %s)",
            datos
        )
        conexion.commit()

        cargar_tabla()
        messagebox.showinfo("Éxito 🎀", "Cliente añadido con éxito.")

        for entry in entries:
            entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error 💔", f"No se pudo insertar: {e}")


# Botón Insertar con toquecito pastel cute
boton_insertar = tb.Button(
    frame_form,
    text="Añadir Cliente 🌸",
    bootstyle="danger-outline",
    command=inserta
    width=22
)
boton_insertar.grid(row=5, columnspan=2, pady=20)

cargar_tabla()
ventana.mainloop()

cursor.close()
conexion.close()

