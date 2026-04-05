# 📝 Lista de Tareas - Aplicación GUI con Tkinter

## 📌 Descripción

Este proyecto consiste en el desarrollo de una aplicación de escritorio para la gestión de tareas diarias, implementada en Python utilizando la biblioteca Tkinter.

El sistema permite registrar, completar y eliminar tareas mediante una interfaz gráfica amigable, incorporando además atajos de teclado para optimizar la interacción del usuario.

La aplicación mantiene una arquitectura modular por capas, garantizando una correcta separación de responsabilidades entre la lógica del negocio y la interfaz gráfica.

---

## 🎯 Objetivo

Desarrollar una aplicación GUI que permita gestionar tareas de forma eficiente, incorporando interacción mediante teclado y respetando una arquitectura modular bien definida.

---

## 🧩 Arquitectura del Sistema

El sistema está organizado en capas de la siguiente manera:

```
lista_tareas_app/
│
├── main.py
├── modelos/
│   └── tarea.py
├── servicios/
│   └── tarea_servicio.py
└── ui/
    └── app_tkinter.py
```

### 🔹 Descripción de componentes

* **modelos/**: Define la estructura de los datos (clase `Tarea`)
* **servicios/**: Contiene la lógica del sistema (gestión de tareas)
* **ui/**: Implementa la interfaz gráfica con Tkinter
* **main.py**: Punto de entrada del sistema

---

## ⚙️ Funcionalidades

* ✅ Registro de nuevas tareas
* ✅ Marcado de tareas como completadas
* ✅ Eliminación de tareas con confirmación
* ✅ Limpieza del campo de entrada
* ✅ Visualización en tabla (Treeview)
* ✅ Diferenciación visual de estados (pendiente/completada)
* ✅ Selección de tareas para edición
* ✅ Uso de atajos de teclado

---

## ⌨️ Atajos de Teclado

| Acción            | Tecla  |
| ----------------- | ------ |
| Agregar tarea     | Enter  |
| Completar tarea   | C      |
| Eliminar tarea    | Delete |
| Cerrar aplicación | Esc    |

---

## 🖥️ Tecnologías Utilizadas

* Python 3
* Tkinter
* ttk (Treeview)

---

## 🚀 Ejecución del Proyecto

1. Clonar el repositorio:

```
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
```

2. Acceder al proyecto:

```
cd lista_tareas_app
```

3. Ejecutar la aplicación:

```
python main.py
```

---

## 🧠 Mejoras Implementadas

* Uso de eventos de teclado mediante `.bind()`
* Implementación de `Treeview` para visualización estructurada
* Uso de `Frame` para organización de la interfaz
* Confirmación antes de eliminar tareas
* Aplicación de estilos visuales para mejorar la experiencia de usuario
* Implementación de arquitectura por capas

---

## 📷 Evidencia del Sistema

Agrega aquí una captura del funcionamiento de la aplicación:

```
![Captura del sistema](captura.png)
```

---

## Autor

* Nombre: Mercy Katherine Amaya
* Semana: 16

---

## 📌 Conclusión

El desarrollo de esta aplicación permitió aplicar conceptos de programación orientada a objetos, diseño de interfaces gráficas y arquitectura por capas. La incorporación de atajos de teclado mejoró significativamente la usabilidad del sistema, logrando una solución más eficiente y estructurada.
