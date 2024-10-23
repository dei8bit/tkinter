from customtkinter import *

app = CTk()

#$ ejemplo 1:

button = CTkButton(app, font=CTkFont(family="", size=16, underline=True))

button.cget("font").configure(size=16)  # configure font afterwards

#$ ejemplo 2: reutilizando la fuente creada.

my_font = CTkFont(family="", size=18, )

button_1 = CTkButton(app, font=my_font).pack()
button_2 = CTkButton(app, font=my_font).pack()

my_font.configure(family="new name")  # changes apply to button_1 and button_2

app.mainloop()
