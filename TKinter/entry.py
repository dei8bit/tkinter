from tkinter import *

root = Tk()

# entrada = Entry(root, fg="green")
# entrada.pack()


# $ Ejemplo:

# entrada = Entry(root, width=60)
# entrada.grid(row=0, column=0)


# def mostrar():
#     Label(text=f"texto {entrada.get()}").grid(row=3, column=0)


# boton = Button(root, bg="red", text="presiona ", command=mostrar)
# boton.grid(row=1, column=0)

# $ Ejemplo 2:


# entrada = Entry(root, width=60, show="☺")
# entrada.grid(row=0, column=0)


# def mostrar():
#     Label(text=f"texto {entrada.get()}").grid(row=3, column=0)


# boton = Button(root, bg="red", text="presiona ", command=mostrar)
# boton.grid(row=1, column=0)


# $ Ejemplo3:

# def remove_placeholder(event):
#     entrada.delete(0, END)

# entrada = Entry(root, width=60)
# entrada.insert(0, "Placeholder")  # Inserta el texto del placeholder
# entrada.bind('<FocusIn>', remove_placeholder)  # Elimina el placeholder cuando el widget recibe el foco

# entrada.grid(row=0, column=0)


# def mostrar():
#     Label(text=f"texto {entrada.get()}").grid(row=3, column=0)


# boton = Button(root, bg="red", text="presiona ", command=mostrar)
# boton.grid(row=1, column=0)


root.mainloop()
