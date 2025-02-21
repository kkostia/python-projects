from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
from json import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    # generating random letters, symbols, numbers from list
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list) # shuffling all the symbols

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()
    new_data = {
         website: {
                "email": login,
                "password":  password,
            } 
         }

    if website and login and password: 
            try:
                with open("data.json", "r") as f: 
                    data = load(f)
                    data.update(new_data)
            except FileNotFoundError:
                 data = {}
            with open("data.json", "w") as f: 
                dump(data, f, indent=4)

            password_input.delete(0, END)
            website_input.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Make sure to fill all the fields")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

##Logo setup
logo = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

## Lables
website_label = Label(text="Website:", font="Arial")
website_label.grid(row=1, column=0, padx=5, pady=5)

username_label = Label(text="Email/Username:", font="Arial")
username_label.grid(row=2, column=0, padx=5, pady=5)

password_label = Label(text="Password:", font="Arial")
password_label.grid(row=3, column=0, padx=5, pady=5)

## Inputs
webiste = website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, pady=5)
website_input.focus()

login = login_input = Entry(width=35)
login_input.grid(row=2, column=1, columnspan=2, pady=5)
login_input.insert(0, "kospanasenko2@gmail.com")

password = password_input = Entry(width=21)  # Adjusted width
password_input.grid(row=3, column=1, pady=5)

## Buttons
generate_button = Button(text="Generate password",command=generate_password)
generate_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)









window.mainloop() 