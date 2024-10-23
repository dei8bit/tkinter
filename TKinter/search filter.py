import tkinter as tk


def actualizar_filtro(event):
    filtro = entry_busqueda.get().lower()
    listbox_items.delete(0, tk.END)
    for item in elementos:
        if filtro in item.lower():
            listbox_items.insert(tk.END, item)


# Crear la ventana principal
root = tk.Tk()
root.geometry("400x300")
root.title("Ejemplo de Filtro de Búsqueda con Tkinter")

# Crear una entrada para búsqueda
entry_busqueda = tk.Entry(root, width=30)
entry_busqueda.pack(padx=20, pady=10)
entry_busqueda.bind("<KeyRelease>", actualizar_filtro)

# Datos de ejemplo
elementos = ["Manzana", "Banana", "Cereza", "Durazno", "Fresa", "Uva"]

# Crear un Listbox para mostrar los elementos filtrados
listbox_items = tk.Listbox(root)
for item in elementos:
    listbox_items.insert(tk.END, item)
listbox_items.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

root.mainloop()
