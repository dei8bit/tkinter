from tkinter import *

root = Tk()


# etiqueta = Label(root, text="Que onda desde TKINTERR").pack()
cuadro1 = Frame()
cuadro2 = Frame()
cuadro3 = Frame()
cuadro4 = Frame()

cuadro1.pack()
cuadro2.pack()
cuadro3.pack()
cuadro4.pack()

cuadro1.config(width=50, height=50, bg="green")
cuadro2.config(width=50, height=50, bg="red")
cuadro3.config(width=50, height=50, bg="blue")
cuadro4.config(width=50, height=50, bg="yellow")


root.mainloop()
