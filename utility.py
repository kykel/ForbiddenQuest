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

    def __init__(self):
        pass

    @staticmethod
    def pause(self):
        return input("\nPress Enter to Continue.\n")

    # Clear/refresh the screen
    @staticmethod
    def clear():
        return os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
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

    @staticmethod
    def yesorno(self, question, option1, option2, returnoption=""):
        while True:
            choice = input(question)
            if choice == '1' or choice.lower == 'yes':
                return option1
            elif choice == '2' or choice.lower == 'no':
                return option2
            else:
                print("\n\nSomehow, you break your time matrix and a rift opens beside you, a violent maelstrom sucking everything in. Time mages manage to appear and pull you out just in time. Close call... Phew.\nYou find yourself back where you started. Time seems to have rolled back around you.\n")
                pause()
                clear()

    @staticmethod
    def universal_menu(menuitems: list, header: str = "") -> str | None:
        """ Generate a generic Menu based on *menuitems*. """
        menuitems_standardized = []
        for x in menuitems:
            menuitems_standardized.append(x.lower())

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
                menusize = len(menuitems)
                if (int(answer)) <= menusize:
                    return (int(answer)-1)

            if answer.lower() in menuitems_standardized:
                print(answer)
                cnt = 1
                for x in menuitems_standardized:
                    if x.lower() == answer.lower():
                        return cnt-1
                    else:
                        cnt += 1

            print("Incorrect answer. Try again.")