import tkinter
import pandas as pd
from tkinter import messagebox
import passwordgen
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def genpassword():
    random_password = passwordgen.generatepassword()
    password_input.insert(0, random_password)
    pyperclip.copy(random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    if len(website_input.get()) == 0 or len(username_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(
            title="Warning", message="Dont leave the inputfield empty")
    else:
        password = {"website": [website_input.get()], "email": [username_input.get()],
                    "password": [password_input.get()]}
        isok = messagebox.askokcancel(title=website_input.get(
        ), message=f"Verify the details to be saved\n website:{website_input.get()}\n email:{username_input.get()}\n password:{password_input.get()}")
        if isok:
            df = pd.DataFrame.from_dict(password)
            df.to_csv("day 29\\password.csv", mode="a")
            website_input.delete(0, 'end')
            username_input.delete(0, 'end')
            password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
img = tkinter.PhotoImage(file=r"day 29\logo.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
# Labels
website_label = tkinter.Label(text="Website")
website_label.grid(row=1, column=0)
username_label = tkinter.Label(text="Email/Username")
username_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password")
password_label.grid(row=3, column=0)
# Input
website_input = tkinter.Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)
username_input = tkinter.Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
password_input = tkinter.Entry(width=23)
password_input.grid(row=3, column=1)
# buttons
generate_button = tkinter.Button(text="GenPasswrd", command=genpassword)
generate_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
