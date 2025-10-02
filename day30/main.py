#PASSWORD MANAGER APP
from tkinter import *
from tkinter import messagebox
from turtle import title
from random import choice, randint, shuffle
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data:
                data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND SAVED PASSWORDS ------------------------------- #
#Search
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
 
    except Exception as e:
        print(f"An error occurred: {e}")
    
    else:
        if website in data:
            get_email = data[website]["email"]
            get_password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {get_email} \nPassword: {get_password} ")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()

email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "sime@gmail.com")

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

#buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save_login_details)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()