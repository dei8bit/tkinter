import tkinter as tk
import customtkinter as ctk


def abrirVentana():
    pass


# Crear la ventana principal
root = ctk.CTk()
root.geometry("800x600")
root.title("Ejemplo de Widgets Responsivos con Wrap Dinámico")

# Crear un PanedWindow horizontal
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=1)

# Crear el frame izquierdo
left_frame = ctk.CTkFrame(pw)
pw.add(left_frame)

# Crear el frame derecho
right_frame = ctk.CTkFrame(pw)
pw.add(right_frame)

# Añadir widgets al frame izquierdo
entry = ctk.CTkEntry(left_frame, width=250, placeholder_text="Busque un coro...")
entry.pack(padx=10, pady=10, fill=tk.X)

button = ctk.CTkButton(left_frame, text="Agregar coro", command=abrirVentana)
button.pack(padx=10, pady=10, fill=tk.X)

# Añadir un Label con wrap dinámico al frame derecho
text = "Aquí podría haber más contenido, y este texto es lo suficientemente largo como para demostrar el wrapping dinámico."
label = ctk.CTkLabel(right_frame, text=text)
label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Configurar weight de columnas y filas para hacerlas responsivas
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


# Ejemplo de agregar un evento de redimensionamiento
def resize(event):
    # Ajustar wraplength del label para que envuelva dinámicamente
    label.configure(
        wraplength=right_frame.winfo_width() - 20
    )  # Ajustar con un pequeño margen


root.bind("<Configure>", resize)

# Iniciar el loop principal de la interfaz
root.mainloop()
