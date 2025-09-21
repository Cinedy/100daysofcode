#Mile to km converter

from tkinter import *


def calculate():
    miles = miles_input.get()
    km = round(float(miles) * 1.609, 2) 
    result_label.config(text=km) 


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=120)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=2, row=0)

equal_to = Label(text="is equal to", font=("Arial", 11))
equal_to.grid(column=0, row=1)

result_label = Label(text="0", font=("Arial", 11))
result_label.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 11))
miles_label.grid(column=3, row=0)

km_label = Label(text="Km", font=("Arial", 11))
km_label.grid(column=3, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=2,row=3)



window.mainloop()