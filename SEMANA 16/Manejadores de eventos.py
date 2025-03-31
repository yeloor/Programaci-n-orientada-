import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)  # Agregar tarea a la lista
        listbox.itemconfig(tk.END, {'fg': 'black'})  # Color para tarea pendiente
        entry.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Error de Entrada", "Por favor ingrese una tarea.")

# Función para eliminar la tarea seleccionada
def delete_task(event=None):
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Error de Selección", "Por favor seleccione una tarea para eliminar.")

# Función para marcar una tarea como completada
def mark_completed(event=None):
    try:
        task_index = listbox.curselection()[0]
        task = listbox.get(task_index)

        if not task.startswith("✅"):
            listbox.delete(task_index)
            listbox.insert(task_index, f"✅ {task}")
            listbox.itemconfig(task_index, {'fg': 'gray'})  # Color gris para tarea completada
        else:
            messagebox.showinfo("Información", "Esta tarea ya está completada.")
    except IndexError:
        messagebox.showwarning("Error de Selección", "Por favor seleccione una tarea para marcar como completada.")

# Función para configurar atajos de teclado
def bind_shortcuts():
    root.bind("<Control-n>", add_task)  # Ctrl + N -> Añadir tarea
    root.bind("<Control-d>", delete_task)  # Ctrl + D -> Eliminar tarea
    root.bind("<Control-c>", mark_completed)  # Ctrl + C -> Marcar como completada

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Lista de tareas
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
listbox.pack(pady=10)

# Campo de entrada para añadir tareas
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Botón para añadir nueva tarea
add_button = tk.Button(root, text="➕ Añadir Tarea", width=20, command=add_task)
add_button.pack()

# Botón para eliminar tarea seleccionada
delete_button = tk.Button(root, text="❌ Eliminar Tarea", width=20, command=delete_task)
delete_button.pack(pady=5)

# Botón para marcar tarea como completada
mark_button = tk.Button(root, text="✔️ Marcar como Completada", width=20, command=mark_completed)
mark_button.pack(pady=5)

# Configurar atajos de teclado
bind_shortcuts()

# Ejecutar la aplicación
root.mainloop()
