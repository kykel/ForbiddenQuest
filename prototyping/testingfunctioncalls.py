import time
import config
import items

def tableofcontents():
    choice = raw_input("Where do you want to go?\n1. Mosuleaum.\n2. Rearpath.\n")
    if choice == '1':
        entermosuleaum()
    elif choice == '2':
        rearpath()
    else:
        exit()

def entermosuleaum():
    def sarcophagus():
        print "You push hard against the lid, because, just as always you seem to think 'This' is the brightest idea in the world. Don't worry, I won't laugh when the mummy is gouging your eyes from their sockets." 
        print "The lid slides open, albeit with great difficulty. Dust sprays up into the air and you step back coughing heavily as you choke on it." 
        print "Finally, you look inside and unsurprisingly, there's a dead guy. Or rather, skeleton.\nDon't worry. It doesn't move. At least, not yet..."
        print "Around the skeleton's neck is a sparkling gold chain, a large yellow topaz attached to the chain."
        choice = raw_input("Will you take it?\n(yes or no)\n")
        if choice == 'yes':
            config.clear()
            print "You take the necklace and ..."
            time.sleep(2)
            print "Wait for it..."
            time.sleep(5)
            print "Any moment now..." 
            time.sleep(10)
            print "HAHAHAHA! GOTCHA. Oh, you should have seen your face.\nNothing happens." 
            items.necklace = '1'
            config.pause()
            entermosuleaum()
        elif choice == 'no':
            entermosuleaum()
                    
    print "The mosuleaum is rather empty. Aside from a few small ash earns and a single sarcophagus in the center you see nothing else." 
    choice = raw_input("What do you want to do?\n1. Check urns.\n2. Open sarcophagus.\n3. Return to graveyard.\n")
    if choice == '1':
        print "Aside from collected dust, there is nothing special about the urns.\n"
        entermosuleaum()
    elif choice == '2':
        sarcophagus()        
    elif choice == '3':
        minigraveyard()
        
def rearpath():
            print "The path before you is narrow and ends cornered between the rear wall of the mansion on your left, the cliff's edge on the right, and the sheer glass wall of the atriary at the opposite end.\nAside from the soothing crashing of the waves on the rocks below, there is nothing here."
            choice = raw_input("What do you want to do?\n1. Wander around aimlessly.\n2. Jump off cliff.\n3. Return to graveyard.")
            if choice == '1':
                print "You wander around aimlessly for several minutes when suddenly you find yourself back in the graveyard...\n\nWeird..."
                config.pause()
                minigraveyard()
            elif choice == '2':
                config.clear()
                print "The doctors always told you that you couldn't fly but hey, where's the fun in believing that.\nThis is your moment!\nYou'll show them!"
                config.pause()
                print "You run, spread your fleshy arm wings and you fly!"
                time.sleep(1)
                print "Straight down..."
                time.sleep(2)
                print "And down..."
                time.sleep(5)
                print "Still falling..." 
                time.sleep(5)
                print "And..\n"
                time.sleep(5)
                print "\nNope.\nRocks.\nHehehe.\nFucking moron.\n\nYou've died!\n"
                exit()
            elif choice == '3':
                minigraveyard()

tableofcontents()