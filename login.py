# Importing modules
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


# Shows whether you have logged in or not
def message():
    if len(var1.get()) != 0 and len(var2.get()) != 0:
        showinfo("Message", f"You are successfully login!")
    else:
        showinfo("Message", f"Please Enter the correct username and password")


window = Tk()

# Setting the size of the window
window.geometry('350x300')
window.title("FlashPsych")

# Username
lb1 = Label(window, text="Username", font=("Arial Bold", 15))
lb1.place(x=50, y=50)

var1 = StringVar()
txt1 = Entry(window, width=20, textvariable=var1)
txt1.place(x=170, y=57)

# Password
lb2 = Label(window, text="Password", font=("Arial Bold", 15))
lb2.place(x=50, y=100)

var2 = StringVar()
txt2 = Entry(window, width=20, textvariable=var2)
txt2.place(x=170, y=100)

btn = ttk.Button(window, text="Login", width=20, command=message)
btn.place(x=100, y=150)


window.mainloop()
