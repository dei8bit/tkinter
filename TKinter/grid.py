from tkinter import *

ventana = Tk()


cuadro1 = Frame()
cuadro2 = Frame()
cuadro3 = Frame()
cuadro4 = Frame()
cuadro5 = Frame()

cuadro1.grid(row=0, column=0)
cuadro2.grid(row=0, column=1)
cuadro3.grid(row=1, column=0)
cuadro4.grid(row=1, column=1)
cuadro5.grid(row=1, column=1)

cuadro1.config(width=100, height=100, bg="orange")
cuadro2.config(width=100, height=100, bg="black")
cuadro3.config(width=100, height=100, bg="blue")
cuadro4.config(width=100, height=100, bg="yellow")
cuadro5.config(width=60, height=60, bg="brown")

ventana.mainloop()
