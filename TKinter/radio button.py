from tkinter import *

root = Tk()

# $ Ejemplo 1:

# x = StringVar()


# def mostrarValor():
#     Label(root, text=f"usted selecciono {x.get()}").pack()


# texto = Label(root, text="Selecciona una opcion: ").pack()

# encabezado = Label(root, text="¿Tiene animales?: ").pack()

# opcion1 = Radiobutton(
#     root, text="Si tengo", value=1, variable=x, command=mostrarValor
# ).pack()
# opcion2 = Radiobutton(
#     root, text="No tengo", value=2, variable=x, command=mostrarValor
# ).pack()


# $ Variable por defecto 1:

textValue = StringVar()  # Variable compartida

textValue.set("valor 1")


def actualizarValor(textValue):
    Label(root, text=textValue).pack()


Radiobutton(
    root,
    text="opcion 1",
    variable=textValue,
    value="valor 1",
).pack()
Radiobutton(
    root,
    text="opcion 2",
    variable=textValue,
    value="valor 2",
).pack()

Button(root, text="ENVIAR", command=lambda: actualizarValor(textValue.get())).pack()

root.mainloop()
