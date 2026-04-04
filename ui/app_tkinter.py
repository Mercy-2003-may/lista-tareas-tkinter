# Importación de librerías necesarias
import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio

# Clase principal de la interfaz gráfica
class AppTkinter:

    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas - Sistema CRUD")
        self.root.geometry("600x450")

        # Instancia del servicio (lógica)
        self.servicio = TareaServicio()

        # ---------------------------
        # FRAME FORMULARIO
        # ---------------------------
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10, padx=10, fill="x")

        # Label + campo de entrada
        tk.Label(frame_form, text="Tarea:").grid(row=0, column=0, padx=5, pady=5)

        self.entry = tk.Entry(frame_form, width=40)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        # Botón limpiar
        self.btn_limpiar = tk.Button(
            frame_form,
            text="Limpiar",
            command=self.limpiar_campo
        )
        self.btn_limpiar.grid(row=0, column=2, padx=5)

        # Texto informativo de atajos
        tk.Label(
            frame_form,
            text="Enter = agregar | C = completar | Delete = eliminar | Esc = salir",
            fg="gray"
        ).grid(row=1, column=0, columnspan=3, pady=5)

        # ---------------------------
        # FRAME BOTONES
        # ---------------------------
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)

        self.btn_agregar = tk.Button(
            frame_botones,
            text="Agregar",
            bg="#4CAF50",
            fg="white",
            width=12,
            command=self.agregar_tarea
        )
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(
            frame_botones,
            text="Completar",
            bg="#2196F3",
            fg="white",
            width=12,
            command=self.completar_tarea
        )
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            bg="#f44336",
            fg="white",
            width=12,
            command=self.eliminar_tarea
        )
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # ---------------------------
        # TABLA (TREEVIEW)
        # ---------------------------
        frame_tabla = tk.Frame(root)
        frame_tabla.pack(pady=10)

        # Definición de columnas
        self.tree = ttk.Treeview(
            frame_tabla,
            columns=("Estado", "Descripción"),
            show="headings",
            height=12
        )

        # Encabezados
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Descripción", text="Descripción")

        # Tamaño columnas
        self.tree.column("Estado", width=100, anchor="center")
        self.tree.column("Descripción", width=350)

        self.tree.pack()

        # ---------------------------
        # ATAJOS DE TECLADO
        # ---------------------------
        self.root.bind("<Return>", lambda event: self.agregar_tarea())
        self.root.bind("<c>", lambda event: self.completar_tarea())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda event: self.root.quit())

        # Foco inicial
        self.entry.focus()

    # ---------------------------
    # FUNCIONES
    # ---------------------------

    # Agregar tarea
    def agregar_tarea(self):
        texto = self.entry.get()
        self.servicio.agregar_tarea(texto)
        self.entry.delete(0, tk.END)
        self.actualizar_tabla()

    # Completar tarea
    def completar_tarea(self):
        seleccion = self.tree.selection()
        if seleccion:
            index = self.tree.index(seleccion[0])
            self.servicio.completar_tarea(index)
            self.actualizar_tabla()

    # Eliminar tarea
    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if seleccion:
            index = self.tree.index(seleccion[0])
            self.servicio.eliminar_tarea(index)
            self.actualizar_tabla()

    # Limpiar campo
    def limpiar_campo(self):
        self.entry.delete(0, tk.END)

    # Actualizar tabla
    def actualizar_tabla(self):
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos
        for tarea in self.servicio.obtener_tareas():
            estado = "✔ Completada" if tarea.completada else "✘ Pendiente"
            self.tree.insert("", tk.END, values=(estado, tarea.descripcion))