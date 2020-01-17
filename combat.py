#!/usr/bin/env python

import time
import random

#Custom Imports
import stats
import quests
import mainfile
import config



def battle(c):
    level = config.level
    health = config.health
    playerdmg = config.playerdmg
    battles = config.battles
    
    config.clear()
    
    print "battles:", battles
    print "level:", level
    print "health:", health
    print "playerdmg:", playerdmg
    print "You are marching long into the afternoon and weariness weighs on you so heavily that you do not notice you're being watched. Something leaps at you from the trees.\n"
    pause = raw_input("Press Enter to Continue.")
    #global health
    #global playerdmg
    HP = health
    creatureHP = c[1]
    #global battles
    print c[4]
    print "You are ambushed by a", c[0], "with", c[1], "life.\n"
    print "     O |      "
    print "    /|\|      'o'|"
    print "     | +      =|=+"
    print "     ^         |"
    print "   _/_\_______/_\ "
    while HP >0 and creatureHP >0:
        battledmg = random.randint(c[2], c[3])
        playerattack = random.randint(playerdmg[0],playerdmg[1])
        print "The", c[0], "strikes you, dealing", battledmg, "damage.\n"
        time.sleep(1)
        HP = HP - battledmg
        creatureHP = creatureHP - playerattack        
        if HP <= 0:
            if c[0] == 'goblin':
                print "You attempt to swing again but your previous wound bleeds profusely and everything quickly grows dizzying. You blink and swallow. You taste blood.\nThe beast lashes out viciously and you miss your parry by an inch, watching knowingly as its weapon plunges into your chest. Suffocation surrounds you, the air growing heavy and the sky growing dark.\nYou've died!\n"
            elif c[0] == 'kobold':
                print "The creature's short spear somehow catches you sharply in the ribs with a sickening crack that immediatly begins spurting blood.\Arrogance is surely to blame. You try to stumble away and the beast hisses at you mockingly. Everything fades to dark, you stumble and fall, face first into the ground. You don't even feel your skull crack on the rock.\nYou've died!\n"
            elif c[0] == 'troll':
                print "You can't breath, the troll's club clearly having punchered a lung on the last hit with one of your broken ribs. You are dizzy, weak, lethargic. You watch helplessly as his club descends upon you. You legacy will be found in his fecal matter later.\nYou've died... obviously.\n"
            elif c[0] == 'dragon':
                print "The field is aflame around you and you feel dizzy and weary from the beast's last strike. As you stumble through the burnt landscape in desperation the creature tracks you from the flames, as though playing with its soon to be meal.\nAll hope seems lost until you stumble to hill side. There is an opening in the flames. You stumble forward, blood leaking painfully from the gash in your side. Freedom seems just before you. You step to the edge of the hill about to collapse and roll down below when suddenly the world turns orange around you.\nFlames engulf you as you scream and flail in agony.\Youv'e died!\n"
            elif c[0] == 'wraith':
                print "You hear it's translusent whispering around you. Fear inches through every part of your being. Your weapon shakes in your hand. Another swipe catches you across the back, just splitting the skin. It's playing with you. You panic and run getting only a few fear when an ear piercing cry echoes out a hot pain cuts across your forearm. You lift your arm to find a bloody stump spraying blood. You attempt to scream just as the shadowy creatures class plunge into your back and evicorapte you into a cloud of unrecognizable organs.\nYou've died!\n"
            elif c[0] == 'wyvern':
                print "You attempt to swing again but the beast catches you blade in its jaws. Before you have chance to respond its tail whips around, tripping you.\nThe last thing you see as its great shadow blocks out the sun is massive white fangs descend upon you.\You've died! Rest in peaces.\n"
            else:
                print "In an attempt to dodge you trip landing on your own blade.\nYou've died, humiliatingly I might add!\n"
            
        elif creatureHP <= 0:
            print "You swing your blade swiftly, striking the", c[0], "with a critical blow of", playerattack, "felling the foul creature.\nYou've survived this fight.\n"
            battles = battles + 1
            print "Battles after victory here:", battles
            loot()
            break
            
        elif creatureHP >= 1 and creatureHP <= 2:
            print "It swings again but you parry swiping low and catching the beast across the gut with a critical strike. The", c[0], "panting and fearful for its dwindling life, flees into the woods,", creatureHP, "life remaining. It escapes for now."
            battles = battles + 1
            print "Battles after victory here:", battles
            break
            
        elif HP > 0:
            print "You have", HP, "life left."
            print "You strike in turn, doing", playerattack, "damage to the", c[0], "but the creature holds its ground,", creatureHP, "life remaining."
         
        else:
            print "you are now out of your loop."
    print "final update of battles in combat:", battles
    config.battles = battles
    print "printing config.battles now:", config.battles
    pause = raw_input("Press Enter to continue.")
    stats.playerstats()

    replay()


def replay():
        answer = raw_input("Would you like to battle again?\n")
        if answer == 'yes':
            c = stats.creaturefunc()
            battle(c)
        elif answer == 'no':
            answer = raw_input("Pick an option:\n1. main menu\n2. go back to quest master\n3. exit\n")
            if answer == '1':
                mainfile.mainmenu()
            if answer == '2':
                quests.main()
            if answer == '3':
                exit()
            else:
                print "I don't know what you were trying to do. Exiting instead...\n"
                time.sleep(3)
                exit()

def loot():
    luck = random.randint(1,20)
    if luck >= 10:
        print "Among the slaughtered carcass of your adversary you find a magnificent blade! Surely this will be good in a fight."
        config.playerdmg = [4,12]
    else:
        print "You find no loot."


