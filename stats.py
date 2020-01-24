#!/usr/bin/env python
import random

#Custom Imports
import mainfile
import config

level = config.level
playerdmg = config.playerdmg
name = config.name

def playerstats():
    level = config.level
    battles = config.battles
    health = config.health

    print "\n\n"
    print "PLAYER STAT READOUT:\n--------------------\n"
    print "Battles won:", battles
    print "Current level:", level
    print "Max health:", health
    print "Player damage:", config.playerdmg
    print "\n\n"

    exp = battles * 2

    print "You've currently won in:", battles, "battles so your current total experience is:", exp


    #Determine level experience
    if level <= 10 and level >=1:
        levelup = exp / 5

    elif level > 10:
        levelup = exp / 10

    #LEVELING UP
    if level == levelup:
        level = level + 1
        health = health + 2
        print "You've leveled up! New level:", level
        print "Your health has gone up. You now have", health, "total life."
    elif level > levelup:
        print "Current level:", level
    elif level < levelup:
        print "You have a problem. Your level should never be below your level up."
    else:
        print "You messed something up. You should not be here."

    config.level = level
    config.health = health
    config.battles = battles


#This function is complete!    ##############################################################################################################################
def creaturefunc():

    #dictionary of stats
    stats = {
            "kobold":[8,1,3,"Shortly ahead a bush rustles. You think nothing of it, a mistake as just as your reach the bush a kobold leaps out chattering and swinging at you."],
            "large-spider":[10,1,5,"For a time you walk, lost in your thoughts until you realize that now you're actually lost. It's then you hear the noise. You stop and listen. There it is again, closer this time. And then, as you look up, the canopy is alive with spiders and one is coming right for you."],
            "goblin":[12,1,5,"Years of being on the trail has left you atune to your surroundings so it doesn't take long to realize you're being followed. You lean down, pretending to tie your boot when seemingly out of nowhere a goblin appears. At least you were ready."],
            "orc":[15,1,8,"Orc's are not the most intelligent of savage creatures. So you aren't entirely surprised when the creature notices your presence and shouting his guttoral war cry lunges at you. At least the goblin you fought last week was smart enough to keep the element of surprise."],
            "ogre":[18,1,10,"You see the ogre long before you but knowing ogres are particularly dumber than their counterparts you figure throwing a limb into the nearby bushes will distract him. Needless to say, you were surprised when you realized that there was another ogre opposite you, who upon hearing a noise came bouldering in its direction. Right at you..."],
            "troll":[20,1,10,"He's big, ugly and mean. You figure, you're in deep shit..."],
            "basilisk":[25,1,14,"You trip walking through the woods. Standing up frustrated you turn to see the stick you tripped over is moving. It's only as the head of the creature slithers out from the bushes do you realize you mistake. It rears, and strikes."],
            "wyvern":[30,1,18,"Up ahead you hear a scream. Alarmed you run forward only to find the person, dead on the ground in a mangled bloody heap. In the bushes something moves, footsteps stomping heavily. Suddenly a large lizard like head lifts up from the other side, blood red eyes locked on you. It roars fiercly and lunges!"],
            "dragon":[40,1,30,"As you leisurly strole through the woods you begin to notice something odd. It's quite, too quiet. You begin to survey the trees, fearful of having walked into a spider wood but no webs comb through the trees.\nIt's then you hear it. The woosh. Wings. And then the crash. You try to run but I mean, come on! REally? You aren't outrunning a dragon. Just give up. If you're lucky it'll eat you quickly."],
            "wraith":[50,1,42,"You are marching through the woods when you notice that everything seems to be dieing around you. The grass is wilting and drying out, the leaves falling from the trees, limbs and truncks warping and turning black. Something is terribly wrong. A hiss echoes through the air, more whisper than snakelike though. Something brushes past you and you turn but nothing is there. The air flickers. Dear god! What have you walked into?"],
            "demi-god":[75,25,60,"Suddenly, the ground begins to quake... Trees crack and splinter around you, sending shards the size of your sword through the air. You dive to the ground just in time to dodge one and cover your neck, praying to the gods. 'Hahaha! Prayer will not help you hear child!' You look up to see a glowing figure standing over you, power emanating so powerfully from him the very air vibrates. 'I am a son of Valicifar, god of war. And I challenge you!"],
            "god":[100,25,100,"All around you time slows down. The leaves stop moving, the wind stops blowing. You already know what's happening. You've killed enough demi-gods at this point to know the presence of one more. As the being crashes to the ground before you you draw your sword. Only as he stands up you realize this is no demi-god. Valicifar himself has come to avenge his sons. Yep.... You're fucked. Don't brother praying to the gods, I don't think they're listening on this one."],
            }

    #Selects a creature to battle at random. DON"T TOUCH, IT WORKS!
    if level <= 3:
        currentbattle = ['goblin', 'large-spider', 'kobold']

    elif level <= 6:
        currentbattle = ['goblin', 'large-spider', 'kobold', 'orc', 'ogre']

    elif level <= 10:
        currentbattle = ['goblin', 'large-spider', 'kobold', 'orc', 'ogre', 'troll', 'basilisk', 'wyvern', 'dragon']

    elif level > 10:
        currentbattle ['goblin', 'large-spider', 'kobold', 'orc', 'ogre', 'troll', 'basilisk', 'wyvern', 'dragon', 'wraith','demi-god','god']

    #currentbattle = ['goblin','troll','kobold','wyvern','dragon','wraith']

    creature = random.choice(currentbattle)
    #This line selects the stats for the particular creature you are fighting.
    battlestats = stats[creature]
    battledmg = random.randint(battlestats[1],battlestats[2])

    return creature, battlestats[0], battlestats[1], battlestats[2], battlestats[3] #creature, creatureHP, battlemin, battlemax, description



#c = creaturefunc()
