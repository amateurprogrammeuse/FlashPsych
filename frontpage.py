# Importing modules
from tkinter import *
from tkinter import ttk
import login
import signup


window = Tk()


# Functions to open login and signup programs
# At the moment the programs loop before the button is even pressed
def login_btn():
    login.mainloop()


def signup_btn():
    signup.mainloop()


# Setting the size of the window
window.geometry('350x300')
window.title("FlashPsych")

# Welcome message
lbl = Label(window, text="Welcome to FlashPsych", font=("Arial Bold", 20))
lbl.pack()

# Buttons to login and sign up pages
btn1 = ttk.Button(window, text="Login", width=20, command=login_btn)
btn1.place(x=100, y=100)

btn2 = ttk.Button(window, text="Sign Up", width=20, command=signup_btn)
btn2.place(x=100, y=150)


window.mainloop()
