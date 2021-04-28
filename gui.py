from tkinter import *
import managePass as o
import time
from tkinter import messagebox
def clearFrame():
    for widget in container.winfo_children():
        widget.destroy()

def showpass_window(a, b):
    clearFrame()
    root.title("Passwords - "+ a)
    frame = Frame(container)
    frame.pack()
    dict = o.pass_list[a]
    list = []
    btnlst = []
    delbtnlst = []
    updatebtnlst = []
    labellst = []
    for key in dict.keys():
        list.append(key)
    def showpass(usr,key, ind):
        # clearFrame()
        # showpass_window(a, b)
        for i in range(len(btnlst)):
            if i != ind:
                labellst[i].config(text="***********")
                labellst[i].grid(row=i, column=1)
            else:
                labellst[i].config(text=o.decrypter(o.pass_list[usr][key]))
                labellst[i].grid(row=ind, column=1)
    
    def delpass(usr, key, ind):
        print(f'{key} deleted')
        o.del_pass(usr, key)
        btnlst.pop(ind)
        delbtnlst.pop(ind)
        labellst.pop(ind)
        showpass_window(a, b)
    if o.pass_list[a]:
        for i in range(len(list)):
            x = f'{i+1}. {list[i]}'
            btnlst.append(Button(frame, text = x, width=10, command=lambda c=i: showpass(a,btnlst[c].cget("text")[3:], (int)(btnlst[c].cget("text")[0])-1)))
            btnlst[i].grid(row=i, column=0, padx=10, pady=10)
            labellst.append(Label(frame, text="***********", width=20, bg="yellow"))
            labellst[i].grid(row=i, column=1, padx=10, pady=10)
            delbtnlst.append(Button(frame, text="Delete", command=lambda c=i: delpass(a, btnlst[c].cget("text")[3:], (int)(btnlst[c].cget("text")[0])-1)))
            delbtnlst[i].grid(row=i, column=3, padx=10, pady=10)
            updatebtnlst.append(Button(frame, text="Update", command =lambda c=i:updatepass_window(a, btnlst[c].cget("text")[3:], b)))
            updatebtnlst[i].grid(row=i, column=4, padx=10, pady=10)
    else:
        Label(frame, text="No passwords saved!").pack()

    btn_frame = Frame(container)
    if btnlst:
        hide_btn = Button(btn_frame, text="Hide", command=lambda: showpass_window(a, b),borderwidth=0, width=10, bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white")
        hide_btn.grid(row=0, column=0, padx=10, pady=10)
    back_btn = Button(btn_frame, text="Back", command= lambda: logged_in(a, b),borderwidth=0, width=10, bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white")
    back_btn.grid(row=0, column=1, padx=10, pady=10)
    btn_frame.pack(pady=10)
    

def updatepass_window(usr, key, pwd):
    clearFrame()
    root.title("Update Password "+key)
    frame = Frame(container)
    oldpass_label = Label(frame, text="Enter the Account password", font=('Arial',12))
    oldpass_entry = Entry(frame, show='*', borderwidth = 0, font=('Arial',12))
    newpass_label = Label(frame, text="Enter the new Password", font=('Arial',12))
    newpass_entry = Entry(frame, show="*", borderwidth=0, font=('Arial',12))
    conf_label = Label(frame, text="Confirm new password", font=('Arial',12))
    conf_entry = Entry(frame, show="*", borderwidth=0, font=('Arial',12))

    def updatepass():
        if(oldpass_entry.get().strip() == pwd):
            if(newpass_entry.get().strip() == conf_entry.get().strip()):
                o.pass_list[usr][key] = o.encrypter(newpass_entry.get().strip())
                o.update_record()
                clearFrame()
                logged_in(usr, pwd)
                Label(container, text=f'Key {key} updated succesfully', fg='green').grid(row=6, column=0)

            else:
                Label(frame, text="Passwords don't match! Re-enter", fg="red").grid(row=4, column=0)
        else:
            Label(frame, text="Account password incorrect!", fg="red").grid(row=4, column=0)

    btn = Button(container,text="Update", command= updatepass)
    frame.pack()
    oldpass_label.grid(row=0, column=0,padx=5, pady=10)
    oldpass_entry.grid(row=0, column=1,padx=5, pady=10)
    newpass_label.grid(row=1, column=0,padx=5, pady=10)
    newpass_entry.grid(row=1, column=1,padx=5, pady=10)
    conf_label.grid(row=2, column=0,padx=5, pady=10)
    conf_entry.grid(row=2, column=1,padx=5, pady=10)
    btn.pack()
    back_btn = Button(container, text="Back", command= lambda: logged_in(usr, pwd),borderwidth=0, width=10, bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white")
    back_btn.pack(pady=10)

def addpass_window(a, b):
    root.title("Add password")
    key_frame=Frame(container)
    key_label = Label(key_frame, text="Key:",font=("Arial", 12), width=20)
    key_entry = Entry(key_frame, borderwidth=0)
    key_label.grid(row=0, column=0, padx=20, pady=10)
    key_entry.grid(row=0,column=1, padx=20, pady=10)
    pass_frame = Frame(container)
    pass_label = Label(pass_frame, text="Password: ",font=("Arial", 12), width=20)
    pass_entry = Entry(pass_frame, show="*", borderwidth=0)
    pass_label.grid(row=0, column=0, padx=20, pady=10)
    pass_entry.grid(row=0,column=1, padx=20, pady=10)
    passconfirm_label = Label(pass_frame, text="Confirm Password:",font=("Arial", 12), width=20).grid(row=1, column=0, padx=20, pady=10)
    passconfirm_entry = Entry(pass_frame, show="*", borderwidth=0)
    passconfirm_entry.grid(row=1, column=1, padx=20, pady=10)
    key_frame.pack()
    pass_frame.pack()

    def addpass():
        key = key_entry.get().strip()
        pwd = pass_entry.get().strip()
        conf = passconfirm_entry.get().strip()
        if (pwd == conf):
            if key in list(o.pass_list[a]):
                Label(container, text=f'The key {key} already exists.\nClick on the following button to update the password or chose a new key').pack()
                Button(container, text="Update", command=lambda: updatepass_window(a, key, pwd)).pack()
            else:
                o.add_pass(a, key, pwd)
                logged_in(a, b)
                Label(container, text=f'Key {key} added succesfully', fg='green').grid(row=6, column=0)
        else:
            passconfirm_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')
            Label(container, text="Password does not match. Please reenter.", fg='red').grid(row=4, column=0).pack()
            

    add_new_btn = Button(container, text="Add", command = addpass, borderwidth=0,width=10, bg="#35d132", activebackground="#2fb82c", fg="white", activeforeground="white")
    add_new_btn.pack()
    back_btn = Button(container, text="Back", command= lambda: logged_in(a, b),borderwidth=0, width=10, bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white")
    back_btn.pack(pady=10)

def updateaccpass_window(usr, pwd):
    clearFrame()
    root.title("Update Account Password - "+usr)
    frame = Frame(container)
    oldpass_label = Label(frame, text="Enter the account password", font=('Arial',12))
    oldpass_entry = Entry(frame, show='*', borderwidth = 0, font=('Arial',12))
    newpass_label = Label(frame, text="Enter the new Password", font=('Arial',12))
    newpass_entry = Entry(frame, show="*", borderwidth=0, font=('Arial',12))
    conf_label = Label(frame, text="Confirm new password", font=('Arial',12))
    conf_entry = Entry(frame, show="*", borderwidth=0, font=('Arial',12))

    def updateaccpass():
        if(oldpass_entry.get().strip() == pwd):
            if(newpass_entry.get().strip() == conf_entry.get().strip()):
                o.usr_list[usr] = o.convert_to_hash(newpass_entry.get().strip())
                o.update_record()
                clearFrame()
                login_window()
                Label(container, text=f'Password updated succesfully', fg='green').grid(row=6, column=0)
            else:
                Label(frame, text="Passwords don't match! Re-enter", fg="red").grid(row=4, column=0)
        else:
            Label(frame, text="Account password incorrect!", fg="red").grid(row=4, column=0)

    btn = Button(container,text="Update", command= updateaccpass)
    frame.pack()
    oldpass_label.grid(row=0, column=0,padx=5, pady=10)
    oldpass_entry.grid(row=0, column=1,padx=5, pady=10)
    newpass_label.grid(row=1, column=0,padx=5, pady=10)
    newpass_entry.grid(row=1, column=1,padx=5, pady=10)
    conf_label.grid(row=2, column=0,padx=5, pady=10)
    conf_entry.grid(row=2, column=1,padx=5, pady=10)
    btn.pack()

    back_btn = Button(container, text="Back", command= lambda: logged_in(usr, pwd),borderwidth=0, width=10, bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white")
    back_btn.pack(pady=10)

def delacc_window(usr, pwd):
    clearFrame()
    root.title("Delete Account - "+usr)
    def delacc_confirm():
        clearFrame()
        root.title("Delete Account - "+usr)
        frame = Frame(container)
        pass_label = Label(frame, text="Enter the account password", font=('Arial',12)).grid(row=0, column=0, padx=10, pady=10)
        pass_entry = Entry(frame, show='*', borderwidth = 0, font=('Arial',12))
        pass_entry.grid(row=0, column=1, padx=10, pady=10)
        
        def delacc():
            if pass_entry.get() == pwd:
                o.del_acc(usr)
                clearFrame()
                Label(container, text="Account deleted successfully", fg="green").grid(row=4, column=0)
                login_window()
            else:
                Label(container, text="Enter the correct password", fg="red").grid(row=4, column=0)
                pass_entry.delete(0, 'end')
        Button(frame, text="Delete!", command=delacc).grid(row=1, column=0, padx=10, pady=10)
        frame.pack()

    Label(container, text="Are you sure you want to delete the account - "+usr+"?").pack()
    btn_frame = Frame(container)
    Button(btn_frame, text="Yes I want to delete this account.", command=delacc_confirm).grid(row=0, column=0, padx=10, pady=10)
    Button(btn_frame, text="No, I changed my mind, don't delete.", command= lambda: logged_in(usr, pwd)).grid(row=0, column=1, padx=10, pady=10)
    btn_frame.pack(pady=10)


def logged_in(a, b):
    clearFrame()
    root.title("Account - "+a)
    logout_btn = Button(container, text="Logout", command = lambda: [clearFrame(), login_window()], width=20)
    addpass_btn = Button(container, text="Add password",command = lambda: [clearFrame(),addpass_window(a, b)], width=20)
    showpass_btn = Button(container, text="Show Passwords", command=lambda: [clearFrame(), showpass_window(a, b)], width=20)
    updateaccpass_btn = Button(container, text="Update Account Password",command=lambda: updateaccpass_window(a,b), width=20)
    delacc_btn = Button(container, text="Delete Account",command =lambda: delacc_window(a, b) , width=20)

    logout_btn.grid(row=1,column=0,padx=5,pady=10)
    addpass_btn.grid(row=2,column=0,padx=5,pady=10)
    showpass_btn.grid(row=3,column=0,padx=5,pady=10)
    updateaccpass_btn.grid(row=4, column=0, pady=10)
    delacc_btn.grid(row=5, column=0, pady=10)



def login(a, b):
    if not a:
        Label(container, text="Please Enter the Username", fg='red', width=20).grid(row=4, column=0)
    elif not b:
        Label(container, text="Please Enter the password", fg='red', width=20).grid(row=4, column=0)
    else:
        if not o.check_avl(a):
            Label(container, text="Account not found.\nTry signing up.", fg='red', width=20).grid(row=4, column=0)
            login_window()
        else:
            if not o.log_in(a, b):
                Label(container, text="Wrong Password!", fg='red', width=20).grid(row=4, column=0)
            else:
                logged_in(a, b)

def signup(a, b):
    if not a:
        Label(container, text="Please Enter the Username", fg='red', width=20).grid(row=4, column=0)
    elif not b:
        Label(container, text="Please Enter the password", fg='red', width=20).grid(row=4, column=0)
    else:
        if o.check_avl(a):
            messagebox.showwarning('Warning!','Username already registered! Try a new one')
            signup_window()
        else:
            o.sign_up(a, b)
            clearFrame()
            Label(container, text="Signup successfull!\nEnter credentials to log in", fg='green', width=30).grid(row=5, column=0)
            login_window()
            
def signup_window():
    clearFrame()
    root.title("Password Manager|SignUp")
    usr_frame=Frame(container)
    usr_label = Label(usr_frame, text="Username:",font=("Arial", 12))
    usr_entry = Entry(usr_frame, borderwidth=0)
    usr_label.grid(row=0, column=0)
    usr_entry.grid(row=0,column=1, padx=20, pady=10)
    pass_frame = Frame(container)
    pass_label = Label(pass_frame, text="Password: ",font=("Arial", 12))
    pass_entry = Entry(pass_frame, show="*", borderwidth=0)
    pass_label.grid(row=0, column=0)
    pass_entry.grid(row=0,column=1, padx=20, pady=10)
    usr_frame.grid(row=0, column=0)
    pass_frame.grid(row=1, column=0)
    signup_btn = Button(container, text="SIGNUP",bg="#ff7575", activebackground="#ff3b3b", fg="white", command=lambda: signup(usr_entry.get().strip(), pass_entry.get().strip()),borderwidth=0, width=15)
    signup_btn.grid(row=3,column=0, pady=10)
    back_btn = Button(container, text="Back", command=lambda: [clearFrame(), login_window()],bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white", borderwidth=0, width=15)
    back_btn.grid(row=4, column=0, pady=10)

def login_window():
    # clearFrame()
    root.title("Password Manager|Login")
    usr_frame=Frame(container)
    usr_label = Label(usr_frame, text="Username:",font=("Arial", 12))
    usr_entry = Entry(usr_frame, borderwidth=0)
    usr_label.grid(row=0, column=0)
    usr_entry.grid(row=0,column=1, padx=20, pady=10)
    pass_frame = Frame(container)
    pass_label = Label(pass_frame, text="Password: ",font=("Arial", 12))
    pass_entry = Entry(pass_frame, show="*", borderwidth=0)
    pass_label.grid(row=0, column=0)
    pass_entry.grid(row=0,column=1, padx=20, pady=10)
    usr_frame.grid(row=0, column=0)
    pass_frame.grid(row=1, column=0)
    login_btn = Button(container, text="LOGIN", bg="#35d132", activebackground="#2fb82c", fg="white", activeforeground="white", command=lambda: login(usr_entry.get().strip(), pass_entry.get().strip()),borderwidth=0, width=15)
    login_btn.grid(row=2, column=0)
    signup_btn = Button(container, text="SIGNUP",bg="#ff7575", activebackground="#ff3b3b", fg="white", activeforeground="white", command=signup_window,borderwidth=0, width=15)
    signup_btn.grid(row=3,column=0, pady=10)

root = Tk()
root.geometry('500x350')
root.resizable(0,0)
# root.config(bg="red")
container = Frame(root, width=500, height=350)
container.pack()
alert=Label(container, text="Welcome User!", fg="red")
alert.grid(row=4, column=0)

login_window()
root.mainloop()