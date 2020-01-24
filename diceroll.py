# ROLL THE DICE


import random

#six sided die
def sixsideddie():
    roll = random.randrange(1,6)
    print "You rolled", roll
    return roll

#ten sided die
def tensideddie():
    roll = random.randrange(1,10)
    print "You rolled", roll
    return roll

#twenty sided die
def twentysideddie():
    roll = random.randrange(1,20)
    print "You rolled", roll
    return roll

def main():
    print "Six sided die, ten, or twenty?"
    choice = raw_input("")
    if choice == "six":
        sixsideddie()
    elif choice == "ten":
        tensideddie()
    elif choice == "twenty":
        twentysideddie()
    else:
        print "Not working."


if __name__ == "__main__":
    main()

