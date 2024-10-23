from customtkinter import *

app = CTk()

scrollable_frame = CTkScrollableFrame(app, width=200, height=200)
scrollable_frame.pack()

CTkLabel(scrollable_frame, text="...text...").pack()
CTkLabel(scrollable_frame, text="...text...").pack()
CTkLabel(scrollable_frame, text="...text...").pack()
CTkLabel(scrollable_frame, text="...text...").pack()
CTkLabel(scrollable_frame, text="...text...").pack()
CTkLabel(scrollable_frame, text="...text...").pack()
CTkLabel(scrollable_frame, text="...text...").pack()
CTkLabel(scrollable_frame, text="...text...").pack()
CTkLabel(scrollable_frame, text="...text...").pack()


app.mainloop()
