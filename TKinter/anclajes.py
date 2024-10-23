from tkinter import *

root = Tk()


# Función para crear una etiqueta con un ancla específica



root.title("Anclajes en Tkinter")

Label(root,text="NORTE").pack(anchor=N)
Label(root,text="ESTE").pack(anchor=E)
Label(root,text="OESTE").pack(anchor=W)
Label(root,text="Nor oeste").pack(anchor=NW)
Label(root,text="Nor este").pack(anchor=NE)
Label(root,text="CENTRO").pack(anchor=CENTER)
Label(root,text="Sur oeste").pack(anchor=SW)
Label(root,text="SUR este").pack(anchor=SE)
Label(root,text="SUR").pack(anchor=S)

root.mainloop()
