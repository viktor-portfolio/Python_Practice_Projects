import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

MY_EMAIL = "myemail@email.com"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_generated_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    return password

def generate_password_onclick():
    password_entry.delete(0,END)
    password_entry.insert(0,random_generated_password())
    pyperclip.copy(random_generated_password())

def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Missing Data File", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"email: {data[website]["email"]}\n "
                                                               f"password: {data[website]["password"]}")
        else:
            messagebox.showwarning(title="Details Not Found", message=f"Cant find the login details for {website}")

def save():
    website_name = website_entry.get()
    email_name = email_name_entry.get()
    password = password_entry.get()
    new_data = {website_name: {
                        "email": email_name,
                        "password": password
        }
    }

    if len(website_name) == 0 or len(email_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Missing details", message="You failed to fill in the entries\n Please go back and check")
    else:
        is_okay = messagebox.askokcancel(title=website_name, message=f"Email: {email_name}\n "
                                                                     f"Password: {password}\n "
                                                                     f"Want to save it?")

        if is_okay:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}

            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0,END)
            password_entry.delete(0,END)


# _______________________ UI _______________________ #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1, pady=2, sticky="W")

email_name_label = Label(text="Email/Username:")
email_name_label.grid(column=0,row=2)
email_name_entry = Entry(width=35)
email_name_entry.insert(0,MY_EMAIL)
email_name_entry.grid(column=1, row=2, columnspan=2, pady=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="W")

generate_password_button = Button(text="Generate Password", command=generate_password_onclick)
generate_password_button.grid(column=2,row=3, pady=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1,row=4, columnspan=2,pady=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2,row=1,sticky="EW")

window.mainloop()