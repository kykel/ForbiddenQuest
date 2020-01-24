import mainfile
import config
import os
import subprocess

cwd = os.getcwd()
savdir = cwd + "/saves"
gamedir = cwd + "/"

def savefile():
    os.chdir(savdir)
    config.clear()
    print "|=================================================================|"
    print "| Hello and welcome to your handy dandy time mage archival bank.  |"
    print "|    Would you like to 'time' stamp your current progress?        |"
    print "|=================================================================|"
    config.validateyesorno()
    name = config.name
    def selectingsave(x):
        print "Opening your save file: (", x + ".txt", ") now."
        choice = raw_input("\nIs this the correct save file?\n")
        if choice == 'yes':
            return x
        elif choice == 'no':
            name = raw_input("What is the name of your file then?\n")
            return selectingsave(name)
        else:
            print "A temporal flux has happened in the space time continuum. I'm afraid we've lost our time mage.\nI sincerely apologize for the inconvenience.\nIf you'll wait one moment we'll put you in contact with another time mage who is surely more qualified to assist you.\n"
            time.sleep(3)
            savefile()

    name = selectingsave(name)
    if os.path.exists(name + '.txt'):
        handle = open(name + '.txt', 'r+w')
        print "Save file opened.\n"
        print "Reading out old save file contents now."
        for line in handle:
            print line
        print "\nAre you sure you want to overwrite this file?"
        config.validateyesorno()
        handle.seek(0)
    else:
        print "This file doesn't exist. Creating new save file now."
        handle = open(name + '.txt', 'w+r')
        time.sleep(1)

    config.pause()

    try:
        print "Writing new save file now:\n"
        handle.seek(0)
        handle.truncate()
        handle.write("Name: " + config.name + "\n")
        handle.write("level: " + str(config.level) + " ")
        handle.write("battles: " + str(config.battles) + " ")
        handle.write("health: " + str(config.health) + " ")
        handle.write("playerdmg: " + str(config.playerdmg[0]) + " ")
        handle.write("playerdmg: " + str(config.playerdmg[1]) + " ")
        print "Save complete.\n"
        print "Restoring you back to your time line now. Have a pleasant day now!"
    except:
        print "\nSAVE FAILED! DEBUG AND TRY AGAIN!\n"

    time.sleep(2)
    handle.close()
    config.pause()
    os.chdir(gamedir)
    mainfile.mainmenu()



def loadgame():
    os.chdir(savdir)
    def loading():
        i = 0
        load = "Loading."
        while i < 6:
            print load + "\n"
            load = load + "."
            i = i + 1
            time.sleep(1)

    config.clear()
    print "|=====================================================================|"
    print "|                                                                     |"
    print "|   Hello and welcome to your handy dandy time mage archival bank.    |"
    print "|    Would you like to retrieve a previously frozen 'time' stamp?     |"
    print "|                                                                     |"
    print "|=====================================================================|"
    config.validateyesorno()
    #loading()
    subprocess.call("ls")
    loadfile = raw_input("Enter the name of your loadfile: ") + '.txt'
    handle = open(loadfile)
    print "STAT READOFF OF FILE:\n"
    buffer = []
    data = []
    for line in handle:
        line = line.split()
        for i in line:
            try:
                buffer.append(str(i))
                data.append(int(i))
            except:
                pass
                #print "print the exception:\n", i

    print "Printing buffer: ", buffer
    print "Printing data: ", data
    config.name = buffer[1]
    config.level = data[0]
    config.battles = data[1]
    config.health = data[2]
    config.playerdmg[0] = data[3]
    config.playerdmg[1] = data[4]
    handle.close()
    config.pause()
    os.chdir(gamedir)
    mainfile.mainmenu()
