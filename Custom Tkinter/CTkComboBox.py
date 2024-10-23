import customtkinter as ctk

def opcion_seleccionada(event):
    seleccion = combobox.get()
    print(f"Opción seleccionada: {seleccion}")

# Crear la ventana principal
root = ctk.CTk()
root.geometry("400x200")
root.title("Ejemplo de CTkComboBox en customtkinter")

# Crear un CTkComboBox
opciones = ["Opción 1", "Opción 2", "Opción 3"]
combobox = ctk.CTkComboBox(root, values=opciones)
combobox.pack(pady=20)

# Asociar un evento para la selección
combobox.bind("<<ComboboxSelected>>", opcion_seleccionada)

# Ejecutar el loop principal de la ventana
root.mainloop()