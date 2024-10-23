from tkinter import *

root = Tk()
root.title("label frames")
root.geometry("400x400")


etiqueta = LabelFrame(root, text="etiqueta", padx=20, pady=20)
etiqueta.grid(row=0, column=0, padx=5, pady=5)

Entry(etiqueta).pack()
Button(etiqueta, text="enviar").pack()


mainloop()
