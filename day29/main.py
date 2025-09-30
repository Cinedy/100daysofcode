#PASSWORD MANAGER APP

from tkinter import *
from tkinter import messagebox
from turtle import title
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = (
    [choice(letters) for _ in range(randint(8, 10))] +
    [choice(numbers) for _ in range(randint(2, 4))] +
    [choice(symbols) for _ in range(randint(2, 4))]
    )

    shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_input.insert(0, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_login_details():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                                                            f"\n Password: {password} \n Is it ok to save?")
        if is_ok:
            with open("login_details", "a") as f:
                f.write(f"Website: {website} | Email: {email} | Password: {password} \n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#entries
website_input = Entry()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "sime@gmail.com")

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

#buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save_login_details)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()