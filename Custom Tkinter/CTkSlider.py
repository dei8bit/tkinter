from customtkinter import *

app = CTk()


slider = CTkSlider(app, from_=0, to=100, command=lambda v: print(v)).pack()

app.mainloop()
