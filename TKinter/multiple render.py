from tkinter import *

root = Tk()


Label(root, text="Renderizado multiple").pack()

texto = ["boton1", "boton2", "boton3", "boton4"]

for texto in texto:
    Button(root, text=texto).pack()


root.geometry("600x300")
root.mainloop()
