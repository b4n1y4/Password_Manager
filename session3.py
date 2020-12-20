import json

user_file = 'c:/Users/RITZ/Documents/Python/user_list.json'
with open(user_file) as usrs:
        usr_list = json.load(usrs)

def log_in(a,b):
        if usr_list[a] == b:
            print ("welcome! aaha login")
        else:
            print ("Password galat h")

def sign_up(a,b):
    usr_list[a] = b
    with open(user_file,'w') as usrs:
        json.dump(usr_list,usrs)


user_inp = int(input("1. Log In\n2. Sign Up\n"))
if user_inp == 1:
    print ("Yaha login karein")
    a = str(input("username: "))
    if(a in usr_list):
        b = str(input("pwd: "))
        log_in(a,b)
    else:
        print("Username not registered. Please try again!!")
elif  user_inp == 2:
    a = str(input("username: "))
    if a in usr_list:
        print("Sorry this Username is already taken. Try some other...")
    else:
        b = str(input("pwd: "))
        sign_up(a,b)
else:
    print ("bhai galti kar diye, chalo bhago")
    exit()
