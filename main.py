from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()

    if website and login and password: 
        is_ok = messagebox.askokcancel(
            title=website, 
            message=f"These are the details entered:\nEmail: {login}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as f: 
                f.write(f"{website} / {login} / {password}\n")
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
generate_button = Button(text="Generate password")
generate_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)









window.mainloop() 