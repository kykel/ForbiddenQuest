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
    header = "MAIN MENU"
    menu = ["new game","load game","save current game","exit","blank"]
    calls = [storyline.newgame,memorycard.loadgame,memorycard.savefile,exit,developer_menu]
    output = Utility.universal_menu(menu,header)
    calls[output]()


def developer_menu():
    menu = ["quests","combat","storyline","main manu","exit"]
    calls = [quests.main,combat.battle,storyline.newgame,mainmenu,exit]
    output = Utility.universal_menu(menu,"Welcome to the hidden developer menu, where all things are possible...\nChoose a function to jump to:")
    calls[output]()

def validation(x):
    print(type(x))
    

if __name__ == "__main__":
    titlescreen()
