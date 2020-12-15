def log_in(a,b):
    if a in users:
        if users[a] == b:
            print ("welcome! aaha login")
        else:
            print ("Chala ja bsdk")
            exit()
    else:
        print("username does not exist")
        exit()

def sign_up(a,b):
    if a in users:
        print("Doosra naam dhoondh bisi")
    else:
        users[a] = b

user_inp = int(input("1. Log In\n2. Sign Up\n"))
users = {"usr_1":"pass_1","usr_2":"pass_2","usr_3":"pass_3"}
if user_inp == 1:
    print ("Yaha login karein")
    a = str(input("username: "))
    b = str(input("pwd: "))
    log_in(a,b)
elif  user_inp == 2:
    a = str(input("username: "))
    b = str(input("pwd: "))
    sign_up(a,b)
else:
    print ("bhai galti kar diye, chalo bhago")
    exit()