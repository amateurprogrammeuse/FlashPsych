# Importing modules
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


# Shows whether you have successfully signed up or not
def message():
    if len(var1.get()) != 0:
        if len(var2.get()) != 0:
            if len(var3.get()) != 0:
                if len(var4.get()) != 0:
                    showinfo("Message", f"You have successfully signed up!")
                else:
                    showinfo("Message", f"Please fill all fields")
            else:
                showinfo("Message", f"Please fill all fields")
        else:
            showinfo("Message", f"Please fill all fields")
    else:
        showinfo("Message", f"Please fill all fields")


window = Tk()

# Setting the size of the window
window.geometry('350x300')
window.title("FlashPsych")

# First Name
lb1 = Label(window, text="First Name", font=("Arial Bold", 15))
lb1.place(x=50, y=50)

var1 = StringVar()
txt1 = Entry(window, width=20, textvariable=var1)
txt1.place(x=170, y=57)

# Surname
lb2 = Label(window, text="Surname", font=("Arial Bold", 15))
lb2.place(x=50, y=100)

var2 = StringVar()
txt2 = Entry(window, width=20, textvariable=var2)
txt2.place(x=170, y=100)

# Username
lb3 = Label(window, text="Username", font=("Arial Bold", 15))
lb3.place(x=50, y=150)

var3 = StringVar()
txt3 = Entry(window, width=20, textvariable=var3)
txt3.place(x=170, y=150)

# Password
lb4 = Label(window, text="Password", font=("Arial Bold", 15))
lb4.place(x=50, y=200)

var4 = StringVar()
txt4 = Entry(window, width=20, textvariable=var4)
txt4.place(x=170, y=200)

btn = ttk.Button(window, text="Sign Up", width=20, command=message)
btn.place(x=100, y=250)


window.mainloop()
