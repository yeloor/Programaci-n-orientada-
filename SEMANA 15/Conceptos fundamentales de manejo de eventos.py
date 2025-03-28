import tkinter as tk
from tkinter import messagebox

# Función para agregar una tarea a la lista
def agregar_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea:  # Verifica que la tarea no esté vacía
        lista_tareas.insert(tk.END, tarea)  # Agrega la tarea al final de la lista
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

# Función para eliminar la tarea seleccionada de la lista
def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        lista_tareas.delete(indice)  # Elimina la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Función para marcar una tarea como completada
def marcar_completada(event=None):
    try:
        indice = lista_tareas.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        tarea = lista_tareas.get(indice)  # Obtiene el texto de la tarea seleccionada
        lista_tareas.delete(indice)  # Elimina la tarea original
        lista_tareas.insert(tk.END, f"✔ {tarea}")  # Vuelve a agregar la tarea con un check para indicar que está completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")  # Título de la ventana
root.geometry("400x400")  # Tamaño de la ventana

# Crear un frame para la entrada de tareas
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Campo de entrada para escribir nuevas tareas
entrada_tarea = tk.Entry(frame_entrada, width=40)
entrada_tarea.pack(side=tk.LEFT, padx=5)
entrada_tarea.bind("<Return>", agregar_tarea)  # Permite agregar tarea presionando Enter

# Botón para añadir una nueva tarea
boton_agregar = tk.Button(frame_entrada, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack(side=tk.RIGHT)

# Crear un frame para la lista de tareas
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Listbox para mostrar las tareas actuales
lista_tareas = tk.Listbox(frame_lista, width=50, height=15)
lista_tareas.pack()
lista_tareas.bind("<Double-Button-1>", marcar_completada)  # Permite marcar como completada con doble clic

# Crear un frame para los botones de acciones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para marcar una tarea como completada
boton_completar = tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(side=tk.LEFT, padx=5)

# Botón para eliminar una tarea seleccionada
boton_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(side=tk.RIGHT, padx=5)

# Iniciar la aplicación principal
root.mainloop()
