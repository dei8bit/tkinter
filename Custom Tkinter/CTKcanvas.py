import tkinter as tk
import customtkinter as ctk


def main():
    root = ctk.CTk()
    root.geometry("800x600")
    root.title("Ejemplo de Canvas en customtkinter")

    # Crear un Canvas
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(padx=20, pady=20)

    # Dibujar un rectángulo
    canvas.create_rectangle(50, 50, 200, 200, fill="blue", outline="black")

    # Dibujar un círculo (óvalo)
    canvas.create_oval(250, 50, 350, 150, fill="red", outline="black")

    # Dibujar una línea
    canvas.create_line(0, 0, 400, 400, fill="green", width=3)

    # Añadir texto
    canvas.create_text(200, 300, text="¡Hola, Canvas!", font=("Arial", 20))

    root.mainloop()


if __name__ == "__main__":
    main()
