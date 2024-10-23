from tkinter import *

root = Tk()

texto = StringVar()
numero = IntVar()
booleano = BooleanVar()
flotante = DoubleVar()

Label(root, text="variable textual: ").pack()
campo_textual = Entry(root, textvariable=texto).pack()

Label(root, text="variable numerica: ").pack()
campo_numerico = Entry(root, textvariable=numero).pack()

Label(root, text="variable booleana: ").pack()
campo_booleano = Entry(root, textvariable=booleano).pack()

Label(root, text="variable flotante: ").pack()
campo_flotante = Entry(root, textvariable=flotante).pack()


def imprimirNumero():
    print(texto.get())


def imprimirTexto():
    print(numero.get())


def imprimirBooleano():
    print(booleano.get())


def imprimirFlotante():
    print(flotante.get())


Button(root, text="Imprimir texto", command=imprimirNumero).pack()

Button(root, text="Imprimir numero", command=imprimirTexto).pack()

Button(root, text="Imprimir booleano", command=imprimirBooleano).pack()

Button(root, text="Imprimir flotante", command=imprimirFlotante).pack()

root.mainloop()
