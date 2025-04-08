#!/usr/bin/env python

import time
import os

#Custom Imports
import storyline
import combat
import stats
import quests
from utility import Utility
import memorycard


time.sleep(.5)
level = 1
battles = 0
health = 10
playerdmg = [1,8]
c = stats.creaturefunc()
cwd = os.getcwd()
savdir = cwd + "/saves"
gamedir = cwd


def title(x):
    print(x)
    time.sleep(.1)

def titlescreen():
    Utility.clear()
    #intro = "W e l c o m e t"
    intro = ['W ','e ','l ','o ','m ','e ','t']
    i = []
    for letter in intro:
        if letter == 't':
            time.sleep(.5)
            print("t o")
            time.sleep(.5)
        else:
            i.append(letter)
            time.sleep(.3)
            Utility.clear()
            print(''.join(i).strip())

    title = [" ______________         _______   ________  ________    ________",
    "{              |    ___/       \_/        \/        \__/         \__",
    " \     ~~~~~    \  /      ||           ||     ||                    \____",
    "   \   ||        \ \      ||           ||     ||   __      _          __/",
    "   /   ||~~~  ___ \/  __  ||~~~  ~  ~~~||  ~~~||  /__\\  |// \\        /",
    " /     ||    || || ||/  \\ ||  || | ||  || ||  || |      ||   |   ____>",
    " \     ||    ||_|| ||       ~~~  |  ~~~    ~~~    \\__/  ||   |  _>",
    "{                                                             _]",
    " |      _____                                                / ",
    "{      ||    |        ___      _    ||                       \___  __  ",
    " \     ||    | |  || /__\\\\   // \\ ~~||~~    ___     __           \/  \   ",
    "   \   ||   \\| |  |||    _    \\\\    ||      \   \__/   \             /    ",
    " __/   ||____\\ |__|| \\__// \\__//    ||  _____\           \____        \ ",
    " \                     ____            /                      >____   /",
    " /                ____/    \__________/                            \  | ",
    "<~~~~~~~~~~~~~~~~/                                                  ~~>"]
    for line in title:
        print(line)
        time.sleep(.1)

    mainmenu()

def mainmenu():
    print("MAIN MENU:\n")
    choice = input("What do you wish to do:\n1. new game\n2. load game\n3. save current game\n4. exit\n")
    if choice == '1':
        Utility.clear()
        storyline.newgame()
    elif choice == '2':
        Utility.clear()
        memorycard.loadgame()
    elif choice == '3':
        Utility.clear()
        memorycard.savefile()
    elif choice == '4':
        Utility.clear()
        exit()
    elif choice == '5':
        print("Which function do you want to jump to:")
        call = input("\n1. quests\n2. combat\n3. storyline\n")
        if call == '1':
            Utility.clear()
            quests.main()
        elif call == '2':
            Utility.clear()
            combat.battle(c)
        elif call == '3':
            Utility.clear()
            storyline.story()
        else:
            Utility.clear()
            mainmenu()
    else:
        print("Error with your choice. Exiting.")
        time.sleep(5)
        exit()

def validation(x):
    print(type(x))
    

if __name__ == "__main__":
    titlescreen()
