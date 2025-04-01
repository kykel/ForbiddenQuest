#!/usr/bin/env python

import time
import os

#Custom Imports
import storyline
import combat
import stats
import quests
import config
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
    config.clear()
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
            config.clear()
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
        config.clear()
        storyline.newgame()
    elif choice == '2':
        config.clear()
        memorycard.loadgame()
    elif choice == '3':
        config.clear()
        memorycard.savefile()
    elif choice == '4':
        config.clear()
        exit()
    elif choice == '5':
        print("Which function do you want to jump to:")
        call = input("\n1. quests\n2. combat\n3. storyline\n")
        if call == '1':
            config.clear()
            quests.main()
        elif call == '2':
            config.clear()
            combat.battle(c)
        elif call == '3':
            config.clear()
            storyline.story()
        else:
            config.clear()
            mainmenu()
    else:
        print("Error with your choice. Exiting.")
        time.sleep(5)
        exit()

def validation(x):
    print(type(x))
    

if __name__ == "__main__":
    titlescreen()
