# Clase que representa una tarea dentro del sistema
class Tarea:
    
    # Constructor de la clase
    def __init__(self, descripcion):
        # Guarda la descripción de la tarea
        self.descripcion = descripcion
        
        # Estado de la tarea (False = pendiente, True = completada)
        self.completada = False

    # Método para marcar la tarea como completada
    def marcar_completada(self):
        self.completada = True

    # Método especial para representar la tarea como texto
    def __str__(self):
        # Se muestra un símbolo dependiendo del estado
        estado = "✔" if self.completada else "✘"
        
        # Retorna el estado junto con la descripción
        return f"{estado} {self.descripcion}"