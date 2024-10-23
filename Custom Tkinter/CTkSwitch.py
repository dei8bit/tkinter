from customtkinter import *

app = CTk()


def switch_event():
    print("switch toggled, current value:", switch_var.get())


switch_var = StringVar(value="on")
switch = CTkSwitch(
    app,
    text="CTkSwitch",
    command=switch_event,
    variable=switch_var,
    onvalue="on",
    offvalue="off",
).pack()


app.mainloop()
