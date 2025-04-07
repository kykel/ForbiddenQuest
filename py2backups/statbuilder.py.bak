import sys
import random

level = 1
strength = 0
dex = 0
con = 0
intel = 0
luck = 0


def dice6():
    global level
    global strength
    global intel
    global dex
    global con
    global luck
    while level <= 99:
        roll = random.randrange(1,7)
        #print "You roll:", roll
        for i in range(1,roll + 1):
            #print "This is i:", i
            if strength <= 100 and strength == luck:
                strength = strength + 1
            elif dex <= 100 and dex == luck:
                dex = dex + 1
            elif intel <= 100 and intel == luck:
                intel = intel + 1
            elif con <= 100 and con == luck:
                con = con + 1
            else:
                luck = luck + 1
            #roll = roll - 1
        level = level + 1
    print "Current level:", level, "and current stats:\nSTR:", strength, "\nDEX:", dex, "\nINT:", intel, "\nCON:", con, "\nLUCK:", luck
      
    
def tensideddie():
    roll = random.randrange(1,11)
    #print "You rolled", roll 
    return roll 
    
def startingstats():
    strength = tensideddie()
    print "Strength:", strength 
    dexterity = tensideddie()
    print "Dexterity:", dexterity
    Intelligence = tensideddie()
    print "Intelligence:", Intelligence
    Const = tensideddie()
    print "Constitution:", Const 
    Luck = tensideddie()
    print "Luck:", Luck
    
    


if __name__ == '__main__':
    startingstats()