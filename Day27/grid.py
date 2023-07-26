from tkinter import *


window = Tk()
window.title("grid")
window.config(padx=20, pady=20)
#Label 

label = Label(text="Label")
label.grid(row=0, column=0)
label.config(padx=10, pady=10)
# new_button 

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

# button 

button = Button(text="Button")
button.grid(row=1, column=1)

# Entry

entry = Entry()
entry.grid(row=2, column=3)





window.mainloop()