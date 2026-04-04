# Importa Tkinter
import tkinter as tk

# Importa la interfaz gráfica
from ui.app_tkinter import AppTkinter

# Punto de entrada del sistema
if __name__ == "__main__":
    
    # Crea la ventana principal
    root = tk.Tk()
    
    # Inicializa la aplicación
    app = AppTkinter(root)
    
    # Ejecuta el bucle principal de la interfaz
    root.mainloop()