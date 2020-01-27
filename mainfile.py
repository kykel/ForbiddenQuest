#!/usr/bin/env python2.7

import subprocess
import random
import time
import os
import sys

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
    print x
    time.sleep(.1)

def titlescreen():
    config.clear()
    intro = "W e l c o m e t"
    i = []
    for letter in intro:
        if letter == 't':
            time.sleep(.5)
            print "t o"
            time.sleep(.5)
        else:
            i.append(letter)
            time.sleep(.3)
            config.clear()
            print ''.join(i)

    
    
    title(" ______________         _______   ________  ________    ________")
    title("{              |    ___/       \_/        \/        \__/         \__")
    title(" \     ~~~~~    \  /      ||           ||     ||                    \____")
    title("   \   ||        \ \      ||           ||     ||   __      _          __/")
    title("   /   ||~~~  ___ \/  __  ||~~~  ~  ~~~||  ~~~||  /__\\  |// \\        /")
    title(" /     ||    || || ||/  \\ ||  || | ||  || ||  || |      ||   |   ____>")
    title(" \     ||    ||_|| ||       ~~~  |  ~~~    ~~~    \\__/  ||   |  _>")
    title("{                                                             _]")
    title(" |      _____                                                / ")   
    title("{      ||    |        ___      _    ||                       \___  __  ")  
    title(" \     ||    | |  || /__\\\\   // \\ ~~||~~    ___     __           \/  \   ")   
    title("   \   ||   \\| |  |||    _    \\\\    ||      \   \__/   \             /    ") 
    title(" __/   ||____\\ |__|| \\__// \\__//    ||  _____\           \____        \ ")
    title(" \                     ____            /                      >____   /")
    title(" /                ____/    \__________/                            \  | ")
    title("<~~~~~~~~~~~~~~~~/                                                  ~~>")
    mainmenu()

def mainmenu():
    print "MAIN MENU:\n"
    choice = raw_input("What do you wish to do:\n1. new game\n2. load game\n3. save current game\n4. exit\n")
    if choice == '1':
        config.clear()
        newgame()
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
        print "Which function do you want to jump to:"
        call = raw_input("\n1. quests\n2. combat\n3. storyline\n")
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
        print "Error with your choice. Exiting."
        time.sleep(5)
        exit()



def newgame():
    config.level = 1
    config.playerdmg = [1, 8]
    config.health = 10
    config.battles = 0
    print "Welcome player, to Forbidden Quest; a world of adventure and magic, mystery and secrecy, bravery and betrayal.\n"
    config.pause()
    name = raw_input("Quickly now, so your adventure can begin, what is your name young warrior?\n")
    
    if name == "":
        name = "Chosen-One"
        config.pause()
        pass
    elif name != "":
            try:
                name = int(name)
                "Improper name. Game resetting."
                newgame()
            except:
                pass
    else:
        print "You introduce yourself as:", name, "\n"
    config.name = name
    storyline.story()

 
def validation(x):
    print type(x)
    

if __name__ == "__main__":
    titlescreen()
