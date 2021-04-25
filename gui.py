from tkinter import *
import managePass as o
import time
from tkinter import messagebox
def clearFrame():
    for widget in container.winfo_children():
        widget.destroy()
def logged_in(a, b):
    clearFrame()
    root.title("Account - "+a)
    logout_btn = Button(container, text="Logout", command = lambda: [clearFrame(), login_window(container)])
    addpass_btn = Button(container, text="Add password")
    delpass_btn = Button(container, text="Remove a Password")
    showpass_btn = Button(container, text="Show Passwords")
    logout_btn.grid(row=1,column=0,padx=5,pady=10)
    addpass_btn.grid(row=2,column=0,padx=5,pady=10)
    delpass_btn.grid(row=3,column=0,padx=5,pady=10)
    showpass_btn.grid(row=4,column=0,padx=5,pady=10)

def login(a, b):
    if not a:
        alert.config(text="Please Enter the Username")
    elif not b:
        alert.config(text="Please Enter the password")
    else:
        if not o.log_in(a, b):
            alert.config(text="Wrong password!")
        else:
            logged_in(a, b)

def signup(a, b):
    if not a:
        Label(container, text="Please Enter the Username", fg='red').grid(row=4, column=0)
    elif not b:
        Label(container, text="Please Enter the password", fg='red').grid(row=4, column=0)
    else:
        if a in o.usr_list:
            messagebox.showwarning('Warning!','Username already registered! Try a new one')
            signup_window(container)
        else:
            o.sign_up(a, b)
            clearFrame()
            Label(container, text="Signup successfull! Enter credentials to log in", fg='green').grid(row=5, column=0)
            login_window(container)
            
def signup_window(master):
    clearFrame()
    root.title("Password Manager|SignUp")
    usr_frame=Frame(master)
    usr_label = Label(usr_frame, text="Username:",font=("Arial", 12))
    usr_entry = Entry(usr_frame, borderwidth=0)
    usr_label.grid(row=0, column=0)
    usr_entry.grid(row=0,column=1, padx=20, pady=10)
    pass_frame = Frame(master)
    pass_label = Label(pass_frame, text="Password: ",font=("Arial", 12))
    pass_entry = Entry(pass_frame, show="*", borderwidth=0)
    pass_label.grid(row=0, column=0)
    pass_entry.grid(row=0,column=1, padx=20, pady=10)
    usr_frame.grid(row=0, column=0)
    pass_frame.grid(row=1, column=0)
    signup_btn = Button(master, text="SIGNUP",bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white", command=lambda: signup(usr_entry.get(), pass_entry.get()),borderwidth=0, width=15)
    signup_btn.grid(row=3,column=0, pady=10)


def login_window(master):
    # clearFrame()
    root.title("Password Manager|Login")
    usr_frame=Frame(master)
    usr_label = Label(usr_frame, text="Username:",font=("Arial", 12))
    usr_entry = Entry(usr_frame, borderwidth=0)
    usr_label.grid(row=0, column=0)
    usr_entry.grid(row=0,column=1, padx=20, pady=10)
    pass_frame = Frame(master)
    pass_label = Label(pass_frame, text="Password: ",font=("Arial", 12))
    pass_entry = Entry(pass_frame, show="*", borderwidth=0)
    pass_label.grid(row=0, column=0)
    pass_entry.grid(row=0,column=1, padx=20, pady=10)
    usr_frame.grid(row=0, column=0)
    pass_frame.grid(row=1, column=0)
    login_btn = Button(master, text="LOGIN", bg="#35d132", activebackground="#2fb82c", fg="white", activeforeground="white", command=lambda: login(usr_entry.get(), pass_entry.get()),borderwidth=0, width=15)
    login_btn.grid(row=2, column=0)
    signup_btn = Button(master, text="SIGNUP",bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white", command=lambda: signup_window(master),borderwidth=0, width=15)
    signup_btn.grid(row=3,column=0, pady=10)

root = Tk()
root.geometry('500x350')
root.resizable(0,0)
container = Frame(root, width=300, height=300)
container.pack()
alert=Label(container, text="Welcome User!", fg="red")
alert.grid(row=4, column=0)

login_window(container)
root.mainloop()