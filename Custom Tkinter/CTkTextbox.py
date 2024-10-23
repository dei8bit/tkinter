from customtkinter import *

app = CTk()

textbox = CTkTextbox(app)

textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
textbox.delete("0.0", "end")  # delete all text
textbox.configure(state="normal")  # configure textbox to be read-only
textbox.pack()

app.mainloop()
