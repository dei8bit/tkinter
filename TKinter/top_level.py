from tkinter import *

root = Tk()
root.title("top level")
root.geometry("500x200")
root.configure(bg="light cyan", padx=6, pady=6)


# $ Ejemplo 1:

# ventana_nueva = Toplevel()
# ventana_nueva.geometry("150x150")
# ventana_nueva.title("aloha")


# $ Ejemplo 2:
def crear_ventana():
    nombre = nombre_ventana.get()
    texto = contenido.get()
    ventana_nueva = Toplevel()
    ventana_nueva.geometry("300x200")
    ventana_nueva.title(f"{nombre}")
    Label(ventana_nueva, text=texto).pack()
    Button(ventana_nueva, text="cerrar ventana" ,command=ventana_nueva.destroy).pack()


nombre_ventana = StringVar(value="Nombre de la ventana")
contenido = StringVar(value="Contenido textual ")

Entry(
    root,
    width=20,
    bd=3,
    bg="pale green",
    justify="center",
    font=16,
    textvariable=nombre_ventana,
).pack(pady=10)
Entry(root, width=60, bd=3, bg="pale green", font=16, textvariable=contenido).pack(
    pady=10
)
Button(
    root,
    bg="steel blue",
    text="Crear Ventana",
    width=16,
    height=2,
    font=20,
    command=crear_ventana,
).pack()

root.mainloop()
