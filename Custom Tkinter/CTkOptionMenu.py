from customtkinter import *

app = CTk()


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


optionmenu = CTkOptionMenu(
    app, values=["option 1", "option 2"], command=optionmenu_callback
)
optionmenu.set("option 2")
optionmenu.pack()


app.mainloop()
