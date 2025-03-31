#!/usr/bin/python

#First four functions pulled from questcontrolfile.py
# yesorno(4 args)
# funccall(6 args)
# directions(4 args)
# turn()


# CONTROL FILE

def yesorno(choice, option1, option2, returnoption):
    if choice == '1' or choice == 'yes':
        return option1()
    elif choice == '2' or choice == 'no':
        return option2()
    else:
        "\n\nSomehow, you break your time matrix and a rift opens beside you, a violent maelstrom sucking everything in. Time mages manage to appear and pull you out just in time. Close call... Phew.\n\n"
        config.pause()
        config.clear() 
        returnoption()

# This takes your choice and the options that occur from it and ports you back out into the proper function.        
def funccall(choice, option1, option2, option3, option4, returnoption):
    if choice == '1':
        return option1()
    elif choice == '2':
        return option2()
    elif choice == '3':
        return option3()
    elif choice == '4':
        return option4()
    else:
        "\n\nI do apologize but your action has resulted in a temporal fracture. Returning to a safer 'stamp' in time...\n\n"
        config.pause()
        config.clear() 
        returnoption()
    

#DOESN'T WORK PROPERLY - CALLS THE FUNCTIONS AS LOCAL. WANTS GLOBAL. NOT RETURNING TO THE LOCAL FUNCTION
def directions(option1, option2, option3, returnoption):
    direction = raw_input("Which direction do you wish to go?\n(type your answer in all lowercase)\n1. straight\n2. left\n3. right\n")
    if direction.lower() == 'left' or direction == '1':
        return option1()
    elif direction.lower() == 'straight' or direction == '2':
        return option2()
    elif direction.lower() == 'right' or direction == '3':
        return option3()
    else:
        print "\n\nSomehow you've fractured your place in the space time continuum and stepped back in time.... Weird. We may have investigate this...\n\n"
        config.pause()
        config.clear()
        returnoption()

def turn():
    direction = raw_input("Which way do you wish to go?\n1. left\n2. straight\n3. right\n4. go back")
    return direction