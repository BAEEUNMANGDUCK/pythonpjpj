from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# label 
my_label = Label(text="I Am a Label",font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.config(text="new Text")
my_label.grid(column=0, row=0)



# Buttion 

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())
    


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
input.grid(column=2, row=2)



window.mainloop()