import json
filename = 'user_list.json' #put the .json file in the same folder:)

with open(filename) as usrs:
        data = json.load(usrs)
usr_list=data["users"]
pass_list=data["passwords"]

def log_in(a,b):
        if usr_list[a] == b:
            print ("welcome! aaha login")
            print("__________________________________\n")
            logged_in(a)
        else:
            print ("Password galat h")

def logged_in(a):
    while(True):
        try:
            c = int(input("0.Log Out\n1.Show passwords\n2.Add password\n3.Delete password\n4.Update password\n"))
            print("__________________________________\n")
        except TypeError:
            print("Please enter either the digit 1, 2, 3 or 4")
        else:
            if c == 0:
                print("Logging Out...")
                break
            elif c == 1:
                show_pass(a)
                print("__________________________________\n")
            elif c == 2:
                add_pass(a)
                print("__________________________________\n")
            elif c == 3:
                del_pass(a)
                print("__________________________________\n")
            elif c == 4:
                update_pass(a)
                print("__________________________________\n")
            else:
                print("Wrong choice. NOW DIE!!")
                print("__________________________________\n")

def sign_up(a,b):
    usr_list[a] = b
    pass_list[a] = {}
    data["passwords"] = pass_list
    data["users"] = usr_list
    with open(filename,'w') as usrs:
        json.dump(data,usrs)

def show_pass(a):
    if(pass_list[a]):
        for key,value in pass_list[a].items():
            print(f"{key}\t{value}")
    else:
        print("No saved passwords found.\n")
    
def add_pass(a):
    key = str(input("Enter the key\n")).lower()
    value = str(input("Enter the password\n"))
    pass_list[a][key] = value
    data["passwords"] = pass_list
    update_record()
    print(f"Password for {key} added successfully")

def del_pass(a):
    key = str(input("Enter the key.\n"))
    if key in pass_list[a]:
        value = str(input("Enter account password to continue.\n"))
        if usr_list[a] == value:
            pass_list[a].pop(key)
            data["passwords"] = pass_list
            update_record()
        else:
            print("Wrong password entered. Password not deleted.\n")
    else:
        print(f"Key - {key} does not exist.\n")

def update_pass(a):
    print("Passwords stored for:\n")
    for key in pass_list[a]:
        print(f"{key}")
    inp = str(input("Enter the key\n"))
    old_pass = str(input("Enter the old password.\n"))
    if pass_list[a][inp] == old_pass:
        pass_list[a][inp] = str(input("Enter the new password\n"))
        data["passwords"] = pass_list
        update_record()

def update_acc_pass():
    username = str(input("Enter the username.\n")).lower()
    if username in usr_list:
        old_pass = str(input("Enter the old password.\n"))
        if usr_list[username] == old_pass:
            usr_list[username] = str(input("Enter the new password.\n"))
            data["users"] = usr_list
            update_record()

def del_acc():
    username = str(input("Enter the username.\n"))
    if username in usr_list:
        passw = str(input("Enter the password.\n"))
        if usr_list[username] == passw:
            usr_list.pop(username)
            pass_list.pop(username)
            data["users"] = usr_list
            data["passwords"] = pass_list
            update_record()


def update_record():
    with open(filename,'w') as usrs:
        json.dump(data,usrs)
# main
while(True):
    user_inp = int(input("0.Exit\n1. Log In\n2. Sign Up\n3. Update account password\n4. Delete account\n"))
    if user_inp == 0:
        exit()
    if user_inp == 1:
        print ("Yaha login karein")
        a = str(input("username: "))
        if(a in usr_list):
            b = str(input("pwd: "))
            log_in(a,b)
            print("__________________________________\n")
        else:
            print("Username not registered. Please try again!!")
    elif  user_inp == 2:
        a = str(input("username: "))
        if a in usr_list:
            print("Sorry this Username is already taken. Try some other...")
        else:
            b = str(input("pwd: "))
            sign_up(a,b)
            print("__________________________________\n")
    elif user_inp == 3:
        update_acc_pass()
        print("__________________________________\n")
    elif user_inp == 4:
        del_acc()
        print("__________________________________\n")
    else:
        print ("bhai galti kar diye, chalo bhago")
        exit()
