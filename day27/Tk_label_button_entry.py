from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)

second_button = Button(text="Click me", command=button_clicked)
second_button.grid(column=3,row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=4)

window.mainloop()