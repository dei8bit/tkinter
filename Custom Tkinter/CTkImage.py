from customtkinter import *

app = CTk()

from PIL import Image

my_image = CTkImage(
    light_image=Image.open("Custom Tkinter/one.png"),
    dark_image=Image.open("Custom Tkinter/one.png"),
    size=(150, 150),
)

image_label = CTkButton(
    app,
    fg_color="transparent",
    image=my_image,
    text="Texto:) ",
).pack()  # display image with a CTkLabel

app.mainloop()
