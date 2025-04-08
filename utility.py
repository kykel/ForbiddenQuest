#!/usr/bin/env python
#config file for global variables and stuffs
import os
import time
from contextlib import suppress

class Utility():

    # Class variables
    level = 0
    health = 10
    battles = 0
    name = "Chosen-One"
    playerdmg = [1,4]    # Pause until player input
    def pause():
        return input("\nPress Enter to Continue.\n")

    # Clear/refresh the screen
    def clear():
        return os.system('cls' if os.name == 'nt' else 'clear')

    def validateyesorno():
        #import mainfile
        i = 1
        while i < 2:
            choice = input('Yes or no?\n')
            #print "Your choice:", choice
            if choice == "yes":
                i = 3
                break
            elif choice == "no":
                choice = input("Return to main menu?\nYes or no?\n")
                if choice == 'yes':
                    mainfile.mainmenu()
                else:
                    print("So you've re-thought your decision?")
                    pass
            else:
               print("Invalid input. ")
               exit()

    def universal_menu(menuitems: list, header: str = "") -> str | None:
        """ Generate a generic Menu based on *menuitems*. """
        while True:

            if header:
                print(f"{header}", sep="\n")

            #Skyler's version
            for k, v in enumerate(menuitems, start=1):
                if v == "blank":
                    pass
                else:
                    print(f"{k:d}. {str(v).title()}")
            answer = input("Select an Option (by number or name)\n> ").title()
            with suppress(ValueError, IndexError):
                #return menuitems[int(answer) - 1].title()  # because 0-indexing - used for returning a string
                menusize = len(menuitems)
                if (int(answer)) <= menusize:
                    return (int(answer)-1)
            if answer.title() in menuitems:
                #return answer.title() # for returning a string
                cnt = 1
                for x in menuitems:
                    if x == answer.title():
                        return cnt-1
                    else:
                        cnt += 1

            print("Incorrect answer. Try again.")