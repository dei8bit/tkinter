import tkinter as tk
from tkinter import ttk, messagebox

def on_button_click():
    messagebox.showinfo("Información", "¡Botón clicado!")

def show_selection():
    selected = radio_var.get()
    messagebox.showinfo("Selección", f"Has seleccionado la opción {selected}")

def update_progress():
    progress['value'] += 10
    if progress['value'] >= 100:
        progress['value'] = 0

def on_combobox_select(event):
    selected_value = combo.get()
    messagebox.showinfo("Seleccionado", f"Has seleccionado: {selected_value}")

def add_to_listbox():
    listbox.insert(tk.END, entry.get())

def create_notebook():
    notebook_tab1 = ttk.Frame(notebook)
    notebook.add(notebook_tab1, text="Pestaña 1")
    ttk.Label(notebook_tab1, text="Contenido de la Pestaña 1").pack()

    notebook_tab2 = ttk.Frame(notebook)
    notebook.add(notebook_tab2, text="Pestaña 2")
    ttk.Label(notebook_tab2, text="Contenido de la Pestaña 2").pack()

root = tk.Tk()
root.title("Ejemplo de Widgets en Tkinter")

# Label
label = tk.Label(root, text="Etiqueta")
label.pack()

# Button
button = tk.Button(root, text="Botón", command=on_button_click)
button.pack()

# Entry
entry = tk.Entry(root)
entry.pack()

# Listbox
listbox = tk.Listbox(root)
listbox.pack()
add_button = tk.Button(root, text="Añadir a Listbox", command=add_to_listbox)
add_button.pack()

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack()
canvas.create_line(0, 0, 200, 100)
canvas.create_rectangle(50, 25, 150, 75, fill="blue")

# Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Checkbutton", variable=check_var)
checkbutton.pack()

# Radiobutton
radio_var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="Opción 1", variable=radio_var, value=1)
radiobutton2 = tk.Radiobutton(root, text="Opción 2", variable=radio_var, value=2)
radiobutton1.pack()
radiobutton2.pack()
select_button = tk.Button(root, text="Mostrar Selección", command=show_selection)
select_button.pack()

# Menu
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nueva Ventana", command=root.quit)
file_menu.add_command(label="Salir", command=root.quit)

# ProgressBar
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack()
progress_button = tk.Button(root, text="Actualizar Progreso", command=update_progress)
progress_button.pack()

# Treeview
tree = ttk.Treeview(root)
tree.pack()
tree["columns"] = ("one", "two")
tree.heading("one", text="Columna 1")
tree.heading("two", text="Columna 2")
tree.insert("", "end", text="Elemento 1", values=("Valor 1", "Valor 2"))

# Combobox
combo = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3"])
combo.pack()
combo.bind("<<ComboboxSelected>>", on_combobox_select)

# Notebook
notebook = ttk.Notebook(root)
notebook.pack()
create_notebook()

# Mensaje de prueba
messagebox.showinfo("Bienvenida", "¡Bienvenido a la prueba de Widgets!")

root.mainloop()