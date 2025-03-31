#!/usr/bin/python

#Question I'm trying to solve. Is calling a function directly from a side function better or should I return the function to call back to the parent from the side function.



#Example 2 (UMD workbook examples, pg1)
def yesorno(question, option1, option2, returnoption):
    choice = raw_input(question)
    if choice == '1' or choice == 'yes' or choice.lower == 'yes':
        #return option1() #returning the function to parent
        option1() #calling directly
    elif choice == '2' or choice == 'no' or choice.lower == 'no':
        return option2()
        #option2()
    else:
        "\n\nSomehow, you break your time matrix and a rift opens beside you, a violent maelstrom sucking everything in. Time mages manage to appear and pull you out just in time. Close call... Phew.\n\n"
        returnoption()
        
        

def main():
    print "Welcome.\n"
    yesorno("Where do you want to go?", left, right, main)
    wait=raw_input("This is where you break to trace back the route.")
    yesorno("Where do you want to go?", left, right, main)
    wait=raw_input("This is where you break to trace back the route.")
    
def left():
    print "you went left"
    down()
    
def right():
    print "you went right"
    return down()
    
def down():
    print "Now heading south."
    
main()