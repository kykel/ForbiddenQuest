#!/usr/bin/env python
#config file for global variables and stuffs
import os
import time


level = 1
battles = 0
health = 10
playerdmg = [1,8]
name = "Chosen-One"
statslst = []
statslst = [level,battles,health,name]
for i in playerdmg:
    statslst.append(i)
#stat = (playerdmg(0))
#print statslst
'''testingstats = {
    'level': 1,
    'battles': 0,
    'health': 10,
    'playerdmg': [1, 8],
    'name': "Chosen One"
}

stt = []
stt += testingstats.values()
print stt
'''
#essentially my system function to refresh the screen
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

#def pause():
#    return time.sleep(5)

#Function to handle yes, no answers
#def ask(question):
#    answer = input(question)
#    return answer.lower() in ['y', 'yes', 'sure', 'ok', 'k', 'yep']:



#5 second pause
def pause():
    pause = raw_input("\nPress Enter to Continue.\n")

def validateyesorno():
    import mainfile
    i = 1
    while i < 2:
        choice = raw_input('Yes or no?\n')
        #print "Your choice:", choice
        if choice == "yes":
            i = 3
            break
        elif choice == "no":
            choice = raw_input("Return to main menu?\nYes or no?\n")
            if choice == 'yes':
                mainfile.mainmenu()
            else:
                print "So you've re-thought your decision?"
                pass
        else:
           print "Invalid input. "
           exit()
            


