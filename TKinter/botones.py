from tkinter import *

root = Tk()

# boton = Button(root, text="Hello World",bg="blue",padx=2 ,pady=3)
# boton = Button(root, text="Hello World",bg="blue",padx=2 ,pady=3, state=DISABLED)

# $ Ejemplo 2:


# def aparecerTexto():
#     Label(text="soy un texto :)").pack()


# botton = Button(
#     root,
#     text="presioname para aparecer textos: ",
#     bg="blue",
#     padx=3,
#     pady=6,
#     command=aparecerTexto,
# )

# botton.pack()

# $ Ejemplo 2.1:


# def aparecerTexto():
#     Label(text="soy un texto :)").grid(row=1, column=0)


# botton = Button(
#     root,
#     text="presioname para aparecer textos: ",
#     bg="blue",
#     padx=3,
#     pady=6,
#     command=aparecerTexto,
# )

# botton.grid(row=0, column=0)

# $ Ejemplo 2.2:


# def aparecerTexto():
#     Label(text="soy un texto :)").pack()
#     print("asd")


# botton = Button(
#     root,
#     text="presioname para aparecer textos: ",
#     bg="blue",
#     padx=3,
#     pady=6,
#     command=aparecerTexto,
# )

# botton.pack()


# $ Ejemplo 3:
# def change_color():
#     bg = root['bg']
#     if bg == 'white':
#         root.config(bg='lightgreen')
#     else:
#         root.config(bg='white')

# boton = Button(root, text="Change Color", command=change_color)

# boton.pack()


root.mainloop()
