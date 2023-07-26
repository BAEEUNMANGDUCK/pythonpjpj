from tkinter import * 


window = Tk()
window.minsize(width=200, height=100)
window.title(string="Mile to Km Converter")
window.config(padx=20, pady=20)


def mile_to_km_convert():
    miles = entry.get()
    km_converter = int(float(miles) * 1.6)
    to_km_label.config(text=f"{km_converter}")

# Entry
entry = Entry(width=15)
entry.grid(row=0, column=1)

# Miles label

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

# is equal to label

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

# to kilometer label

to_km_label = Label(text="0")
to_km_label.grid(row=1, column=1)


# km label

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# calculate Button 



cal_button = Button(text="Calculate", command=mile_to_km_convert)
cal_button.grid(row=2, column=1)








window.mainloop()