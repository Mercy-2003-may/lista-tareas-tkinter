# Importa el modelo Tarea
from modelos.tarea import Tarea

# Clase que maneja la lógica de negocio del sistema
class TareaServicio:

    # Constructor del servicio
    def __init__(self):
        # Lista donde se almacenan las tareas
        self.tareas = []

    # Método para agregar una nueva tarea
    def agregar_tarea(self, descripcion):
        # Verifica que la descripción no esté vacía
        if descripcion.strip() != "":
            # Crea una nueva tarea y la añade a la lista
            self.tareas.append(Tarea(descripcion))

    # Método para obtener todas las tareas
    def obtener_tareas(self):
        return self.tareas

    # Método para marcar una tarea como completada
    def completar_tarea(self, index):
        # Verifica que el índice sea válido
        if 0 <= index < len(self.tareas):
            # Llama al método del modelo
            self.tareas[index].marcar_completada()

    # Método para eliminar una tarea
    def eliminar_tarea(self, index):
        # Verifica que el índice sea válido
        if 0 <= index < len(self.tareas):
            # Elimina la tarea de la lista
            self.tareas.pop(index)