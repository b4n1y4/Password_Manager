import json
import hashlib, binascii
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import getpass
filename = 'C:/user_list.json'
with open(filename) as usrs:
    data = json.load(usrs)
usr_list=data["users"]
pass_list=data["passwords"]
def log_in(a,b):
        if usr_list[a] == convert_to_hash(b):
            print ("welcome! aaha login")
            print("__________________________________\n")
            # logged_in(a)
            return True
        else:
            print ("Password galat h")
            return False
def logged_in(a):
    while(True):
        try:
            c = int(input("0.Log Out\n1.Show passwords\n2.Add password\n3.Delete password\n4.Update password\n5.Update Account Password\n6.Delete account.\n"))
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
            elif c == 5:
                update_acc_pass(a)
                print("__________________________________\n")
            elif c == 6:
                del_acc(a)
                break
                print("__________________________________\n")
            else:
                print("Wrong choice.")
                print("__________________________________\n")           

def sign_up(a,b):
    usr_list[a] = convert_to_hash(b)
    pass_list[a] = {}
    data["passwords"] = pass_list
    data["users"] = usr_list
    update_record()


def show_pass(a):
    if(pass_list[a]):
        for key in pass_list[a]:
            print(f"{key}")
        key = str(input("Enter the key whose password has to be provided\n"))
        if key in pass_list[a]:
            if check_auth(a):
                print("__________________________________\n")
                print(f"Password for {key} is {decrypter(pass_list[a][key])}")
        else:
            print("\nKey not found\n")
    else:
        print("No saved passwords found.\n")  
def add_pass(a):
    key = str(input("Enter the key\n")).lower()
    value = str(getpass.getpass("Enter the password\n"))
    pass_list[a][key] = encrypter(value)
    data["passwords"] = pass_list
    update_record()
    print(f"Password for {key} added successfully")
def del_pass(a):
    key = str(input("Enter the key.\n"))
    if key in pass_list[a]:
        if check_auth(a):
            pass_list[a].pop(key)
            data["passwords"] = pass_list
            update_record()
        else:
            print("Wrong password entered. Password not deleted.\n")
    else:
        print(f"Key - {key} does not exist.\n")
def update_pass(a):
    if pass_list[a]:
        print("Passwords stored for:\n")
        for key in pass_list[a]:
            print(f"{key}")
        inp = str(input("Enter the key\n"))
        old_pass = (str(getpass.getpass("Enter the old password.\n")))
        if decrypter(pass_list[a][inp]) == old_pass:
            pass_list[a][inp] = encrypter(str(getpass.getpass("Enter the new password.\n")))
            if check_auth(a):
                data["passwords"] = pass_list
                update_record()
                print(f"Password for {inp} updated successfully\n")
            else:
                print("Wrong password entered!")
        else:
                print("Wrong password entered!")
    else:
        print(f"Key - {inp} does not exist.\n")
def update_acc_pass(username):
    username = username.lower()
    if check_auth(username):
        usr_list[username] = convert_to_hash(str(getpass.getpass("Enter the new password.\n")))
        data["users"] = usr_list
        update_record()
        print("Account password updated successfully")
    else:
        print("Wrong password entered!")
def del_acc(username):
    username=username.lower()
    if check_auth(username):
        usr_list.pop(username)
        pass_list.pop(username)
        data["users"] = usr_list
        data["passwords"] = pass_list
        update_record()
        print(f"Account - {username} Deleted")
    else:
        print("Wrong password entered")
def update_record():
    with open(filename,'w') as usrs:
        json.dump(data,usrs)
def check_auth(a):
    passw = str(getpass.getpass("Enter the account password\n"))
    if usr_list[a] == convert_to_hash(passw):
        return True
    return False
def convert_to_hash(pwd):
    dk = hashlib.pbkdf2_hmac('sha256',bytes(pwd, 'utf-8'),b'pr45enj1+g4u+4m',500406,16)
    return base64.b64encode(binascii.hexlify(dk)).decode('ascii')
def encrypter(pwd):
    file = open('c:/key.key', 'rb')
    key = file.read()
    file.close()
    encoded = pwd.encode()
    f= Fernet(key)
    encrypted = f.encrypt(encoded)
    del key
    return base64.b64encode(encrypted).decode('ascii')
def decrypter(pwd):
    file = open('c:/key.key', 'rb')
    key = file.read()
    file.close()
    f= Fernet(key)
    pwd = base64.b64decode(pwd)
    decrypted = f.decrypt(pwd)
    del key
    return decrypted.decode()
def check_avl(u):
    if u in usr_list:
        return True
    else:
        return False
#______________________________________________________________________________
def main():
    while(True):
        user_inp = int(input("0.Exit\n1. Log In\n2. Sign Up\n"))
        if user_inp == 0:
            exit()
        if user_inp == 1:
            print ("Yaha login karein")
            a = str(input("username: "))
            if(a in usr_list):
                b = str(getpass.getpass("pwd: "))
                log_in(a,b)
                print("__________________________________\n")
            else:
                print("Username not registered. Please try again!!")
        elif  user_inp == 2:
            a = str(input("username: "))
            if a in usr_list:
                print("Sorry this Username is already taken. Try some other...")
            else:
                b = str(getpass.getpass("pwd: "))
                sign_up(a,b)
                print("__________________________________\n")
        else:
            print ("Enter the correct choice")
if __name__ == "__main__":
    main()

#testing temp branch 
#testing complete - riteshgupta0406