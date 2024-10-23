import customtkinter as ctk
from PIL import Image, ImageTk


# Función para cargar la imagen de fondo
def cargar_imagen_de_fondo():
    # Cargar la imagen y convertirla a un formato compatible con tkinter
    imagen = Image.open("Custom Tkinter/one.png")  # Reemplaza con la ruta de tu imagen
    imagen_de_fondo = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen de fondo
    label_fondo = ctk.CTkLabel(root, image=imagen_de_fondo)
    label_fondo.image = imagen_de_fondo  # Guardar una referencia para evitar que Python la elimine de la memoria
    label_fondo.place(
        x=0, y=0, relwidth=1, relheight=1
    )  # Ajustar para que ocupe toda la ventana


# Crear la ventana principal
root = ctk.CTk()
root.title("App con Imagen de Fondo")
root.geometry("800x600")

# Llamar a la función para cargar la imagen de fondo
cargar_imagen_de_fondo()


def button_event():
    print("button pressed")


button = ctk.CTkButton(root, text="CTkButton", width=140, height=28)
button.place(x=10, y=10)

# Agregar otros widgets y funcionalidades según sea necesario

root.mainloop()
