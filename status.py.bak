import os
import config


#Status (Sick, poisen, etc.)
zombie = 10
undeadflag = 0
poisen = 15
counter = 0

def cntrinc(num):
    global counter
    counter = counter + num
    #print "counter:", counter
    return counter



def undead(x):
    if undeadflag == 1:
        if counter == 1:
            pass
        elif counter <= 3:
            print "Your wound stings a little.\n"
        elif counter == 4:
            print "As you go to take a step forward your head suddenly grows lightheaded and you reach out to steady yourself on something nearby.\nPhew. That was close. Maybe you should drink more water.\n"
        elif counter == 5:
            print "You take a deep breath. Suddenly you're feeling naseaus. Maybe something you ate?\n"
        elif counter == 6:
            print "Your lightheadedness seems to be the least of your worries now. Fighting back vomiting, you stop a moment to catch your breath. Is it just me or is it getting a little chilly?\n"
        elif counter <= 8:
            print "Your previous bouts of lightheadedness and nausea are nothing compared to how you're starting to feel now. Your muscles ache, your skin burns while the rest of you freezes.\nPanic is starting to set in and already you're trying to think of where you can find the closest healer.\n"
        elif counter == 9:
            print "Your ears are buzzing and your headache has surpassed severe to debiliating. You know you're stumbling but all sense of direction has turned into a haze. Your vision grows cloudy and you're not even sure when your limbs started going numb.\nIt's hard to concentrate on anything more than a single footstep."
            print "You feel tears stinging your ears, blurring your darkening path.\n'Please! Somebody. Anybody. Help me! Please, god, help me!\n"
        elif counter == zombie:
            print "You're on the ground. You don't how you got there. You're not even sure where you are, who you are.\nThere is a taste of copper in the back of your throat, and the insatiable burn of hunger in your stomach is the only thing keeping you crawling desperately forward.\nEverything you see is gray, color left you long ago."
            print "You shuffle, with difficulty to your feet and stumble forward. A sound nearby is calling you forward. Large dark objects stand still as you hobble past them. Trees?\nYou see something. Light."
            print "You stumble forward to the flickering, glowing ambiance. But it's not the glow you walk toward. Rather, toward the bundled heap on the ground.\nYou trip or fall, not sure which into it and suddenly it lets out a cry of fear and anguish. You lunge forward grabbing something soft and fleshy with your teeth and tear."
            print "She screams horrified just as warm liquid sprays across your face and down your neck.\nHer gurgled struggling 'excites' you?"
            print "Wait...\nWTF?!\nYou're a fucking zombie?\nA FUCKING ZOMBIE!\nI was narrating a fucking zombie!\nOmg.... I'm gonna be sick.\nWow...\nUmm...\nTough luck!\nYou've died."
    else:
        pass

#print "counter:", counter
#cntrinc()
#print "counter:", counter