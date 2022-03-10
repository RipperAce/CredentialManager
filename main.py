from tkinter import *
from tkinter import messagebox
import PasswordGenerator
import pyperclip

BIEGE = "#F3EFCC"
FONT = "Optima"

def add_creds_to_file():
    website = website_text.get()
    username = username_text.get()
    password = password_text.get()

    if len(website) == 0 or len(password) == 0 or len(username) == 10:
        messagebox.showwarning(title="Incorrect info", message="Missing Data!")
    
    else:
        is_true = messagebox.askokcancel(title=website, message=f"Entered details are: \nUsername: {username}\nPassword: {password}\nDo you want to continue?")

        if is_true:
            with open("credentials.txt", "a") as creds_file:
                add_data = f"{website} | {username} | {password} \n"
                separator = "-" * len(add_data) + "\n"

                creds_file.write(add_data)
                creds_file.write(separator)

            website_text.delete(0, END)
            username_text.delete(0, END)
            username_text.insert(END, "@gmail.com")
            password_text.delete(0, END)


def password_generator():
    password = PasswordGenerator.generate()
    password_text.insert(0, password)
    pyperclip.copy(password)

#------------------------------------------------------------------------------------------

screen = Tk()
screen.title("Credential Manager")
screen.config(padx=20, pady=20, bg=BIEGE)

canvas = Canvas(width=300, height=300, bg=BIEGE, highlightthickness=0)
image = PhotoImage(file="credential_logo.png")
canvas.create_image(150, 150, image=image)
canvas.grid(column=1, row=0, pady=(0, 20))

website_label = Label(text="Website: ", bg=BIEGE, font=(FONT, 10, "italic"))
website_label.grid(column=0, row=1, sticky="w")

username_label = Label(text="Email/Username: ", bg=BIEGE, font=(FONT, 10, "italic"))
username_label.grid(column=0, row=2, sticky="w")

password_label = Label(text="Password: ", bg=BIEGE, font=(FONT, 10, "italic"))
password_label.grid(column=0, row=3, sticky="w")

website_text = Entry(width=35)
website_text.focus()
website_text.grid(column=1, row=1, columnspan=2, sticky="we")

username_text = Entry(width=35)
username_text.insert(END, "@gmail.com")
username_text.grid(column=1, row=2, columnspan=2, sticky="we")

password_text = Entry(width=21)
password_text.grid(column=1, row=3, sticky="ew")

generate_password_button = Button(text="Generate", font=(FONT, 10, "italic"), highlightthickness=0, command=password_generator)
generate_password_button.grid(column=2, row=3,sticky="we", padx=(5, 0))

add_button = Button(text="Add", font=(FONT, 10, "italic"), highlightthickness=0, width=36, command=add_creds_to_file)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

screen.mainloop()