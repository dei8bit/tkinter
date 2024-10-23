from tkinter import *

root = Tk()
root.title("Ventana de tkinter")
root.geometry("600x300")  # Tamaño inicial de la ventana
root.minsize(400, 400)  # Tamaño mínimo de la ventana
root.maxsize(800, 500)  # Tamaño máximo de la ventana
root.configure(bg="coral", pady=6, padx=6)  # atributos de la ventana

# root.resizable(0, 1)

root.mainloop()
