from tkinter import *
import managePass as o
import time
from tkinter import messagebox
def clearFrame():
    for widget in container.winfo_children():
        widget.destroy()

def showpass_window(a, b):
    root.title("Passwords - "+ a)
    back_btn = Button(container, text="Back", command= lambda: logged_in(a, b))
    back_btn.pack()

    frame = Frame(container, width=490, height=250)
    frame.pack()
    dict = o.pass_list[a]
    list = []
    for key in dict.keys():
        list.append(key)
    
    for i in range(len(list)):
        print(i)
        Button(container, text = list[i]).grid(row=i, column=0)

def updatepass_window(usr, key, pwd):
    clearFrame()
    root.title("Update Password "+key)
    oldpass_label = Label(container, text="Enter the old password")
    oldpass_entry = Entry(container, show='*', borderwidth = 0)
    newpass_label = Label(container, text="Enter the new Password")
    newpass_entry = Entry(container, show="*", borderwidth=0)
    conf_label = Label(container, text="Confirm new password")
    conf_entry = Entry(container, show="*", borderwidth=0)

    def updatepass():
        if(oldpass_entry.get().strip() == pwd):
            if(newpass_entry.get().strip() == conf_entry.get().strip()):
                o.pass_list[usr][key] = o.encrypter(newpass_entry.get().strip())
                o.update_record()
                logged_in(usr, pwd)
            else:
                Label(container, text="Passwords don't match! Re-enter", fg="red").grid(row=4, column=0)
        else:
            Label(container, text="Old password incorrect!", fg="red").grid(row=4, column=0)

    btn = Button(container,text="Update", command= updatepass)

    oldpass_label.grid(row=0, column=0)
    oldpass_entry.grid(row=0, column=1)
    newpass_label.grid(row=1, column=0)
    newpass_entry.grid(row=1, column=1)
    conf_label.grid(row=2, column=0)
    conf_entry.grid(row=2, column=1)
    btn.grid(row=3, column=0)


def addpass_window(a, b):
    root.title("Add password")
    web_frame=Frame(container)
    web_label = Label(web_frame, text="Website:",font=("Arial", 12))
    web_entry = Entry(web_frame, borderwidth=0)
    web_label.grid(row=0, column=0)
    web_entry.grid(row=0,column=1, padx=20, pady=10)
    pass_frame = Frame(container)
    pass_label = Label(pass_frame, text="Password: ",font=("Arial", 12))
    pass_entry = Entry(pass_frame, show="*", borderwidth=0)
    pass_label.grid(row=0, column=0)
    pass_entry.grid(row=0,column=1, padx=20, pady=10)
    passconfirm_label = Label(pass_frame, text="Confirm Password:",font=("Arial", 12)).grid(row=1, column=0)
    passconfirm_entry = Entry(pass_frame, show="*", borderwidth=0)
    passconfirm_entry.grid(row=1, column=1, padx=20, pady=10)
    web_frame.pack()
    pass_frame.pack()

    def addpass():
        web = web_entry.get().strip()
        pwd = pass_entry.get().strip()
        conf = passconfirm_entry.get().strip()
        if (pwd == conf):
            if web in list(o.pass_list[a]):
                Label(container, text=f'The key {web} already exists.\nClick on the following button to update the password or chose a new key').pack()
                Button(container, text="Update", command=lambda: updatepass_window(a, web, pwd)).pack()
            else:
                o.add_pass(a, web, pwd)
                logged_in(a, b)
                Label(container, text=f'Key {web} added succesfully', fg='green').grid(row=6, column=0)
        else:
            passconfirm_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')
            Label(container, text="Password does not match. Please reenter.", fg='red').grid(row=4, column=0).pack()
            

    add_new_btn = Button(container, text="Add", command = addpass)
    add_new_btn.pack()

def logged_in(a, b):
    clearFrame()
    root.title("Account - "+a)
    logout_btn = Button(container, text="Logout", command = lambda: [clearFrame(), login_window(container)])
    addpass_btn = Button(container, text="Add password",command = lambda: [clearFrame(),addpass_window(a, b)])
    showpass_btn = Button(container, text="Show Passwords", command=lambda: [clearFrame(), showpass_window(a, b)])
    updateaccpass_btn = Button(container, text="Update Account Password")
    delacc_btn = Button(container, text="Delete Account")
    
    logout_btn.grid(row=1,column=0,padx=5,pady=10)
    addpass_btn.grid(row=2,column=0,padx=5,pady=10)
    showpass_btn.grid(row=3,column=0,padx=5,pady=10)
    updateaccpass_btn.grid(row=4, column=0, pady=10)
    delacc_btn.grid(row=5, column=0, pady=10)



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
        if o.check_avl(a):
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
    signup_btn = Button(master, text="SIGNUP",bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white", command=lambda: signup(usr_entry.get().strip(), pass_entry.get().strip()),borderwidth=0, width=15)
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
    login_btn = Button(master, text="LOGIN", bg="#35d132", activebackground="#2fb82c", fg="white", activeforeground="white", command=lambda: login(usr_entry.get().strip(), pass_entry.get().strip()),borderwidth=0, width=15)
    login_btn.grid(row=2, column=0)
    signup_btn = Button(master, text="SIGNUP",bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white", command=lambda: signup_window(master),borderwidth=0, width=15)
    signup_btn.grid(row=3,column=0, pady=10)

root = Tk()
root.geometry('500x350')
root.resizable(0,0)
root.config(bg="red")
container = Frame(root, width=500, height=350, bg="yellow")
container.pack()
alert=Label(container, text="Welcome User!", fg="red")
alert.grid(row=4, column=0)

login_window(container)
root.mainloop()