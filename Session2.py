import random

def logic(usr_input,comp):
    global man_score,comp_score
    if usr_input==1 and comp==2:
        comp_score += 1
        print("Computer +1" + "\nYour score : " + str(man_score) + "\nComputer's Score : " + str(comp_score))
    elif usr_input==1 and comp ==3:
        man_score += 1
        print("User +1" + "\nYour score : " + str(man_score) + "\nComputer's Score : " + str(comp_score))
    elif usr_input==2 and comp==1:
        man_score += 1
        print("User +1" + "\nYour score : " + str(man_score) + "\nComputer's Score : " + str(comp_score))
    elif usr_input==2 and comp == 3:
        comp_score += 1
        print("Computer +1" + "\nYour score : " + str(man_score) + "\nComputer's Score : " + str(comp_score))
    elif usr_input==3 and comp==1:
        comp_score +=1
        print("Computer +1" + "\nYour score : " + str(man_score) + "\nComputer's Score : " + str(comp_score))
    elif usr_input==3 and comp==2:
        man_score +=1
        print("User +1" + "\nYour score : " + str(man_score) + "\nComputer's Score : " + str(comp_score))
    else:
        print("No one scored" + "\nYour score : " + str(man_score) + "\nComputer's Score : " + str(comp_score))

# main block

print ("1 = Rock, 2 = Paper, 3 = Scissor")

man_score = 0
comp_score = 0
wrong_tries = 0
choices={'1':'Rock','2':'Paper','3':'Scissors'}
for i in range (0,5):
    usr_input = str(input("Enter your choice : "))
    if(len(usr_input) == 1):
        if(49 <= ord(usr_input) <= 51):
            usr_input = int(usr_input)
            comp = random.randint(1,3)
            print("You chose : "+choices[str(usr_input)]+"\nComputer chose : " + choices[str(comp)])
            logic(usr_input,comp)
            print("_______________________________________________________________")
        else:
            print("Wrong value")
            wrong_tries += 1
            ("_______________________________________________________________")
    else:
        print("Wrong value")
        wrong_tries += 1
        ("_______________________________________________________________")  
if man_score > comp_score:
    print("you win")
elif man_score == comp_score:
    print("Tie! Noone wins")
else:
    print("Computer outsmarted you ")