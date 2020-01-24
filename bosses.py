#Bosses
import random, sys

class monster():
    def __init__(self,name,hp,dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg



class Helga(monster):
    name = "Grand Witch Helga"
    hp = 45
    dmg = random.randrange(5,15)

    def __init__(self):
        pass


class player():
    def __init__(self,name,plhp,dmg):
        self.plname = name
        self.plhp = plhp
        self.pldmg = dmg

    def start(self):
        print "You are born.\n"
        print "You grow up.\n"
        wep = raw_input("Pick a weapon!\n1.Sword\n2.Dagger\n3.Spear\n4.Bow\n")
        if wep == '1':
            wep = 'sword'
            self.pldmg = 7
        elif wep == '2':
            wep = 'dagger'
            self.pldmg = 3
        elif wep == '3':
            wep = 'spear'
            self.pldmg = 5
        else:
            wep = 'bow'
            self.pldmg = 4

        print "You picked a", wep + "."
        #self.attack()


class battle(player, Helga):
    def __init__(self):
        pass

    def attack(self):
        while self.hp > 0 and self.plhp > 0:

            self.choice()
            print "You attack with", self.pldmg, "damage."
            self.hp -= self.pldmg
            print "The enemy has", self.hp, "left."
            print "The", self.name, "attacks with", self.dmg, "damage."
            self.plhp -= self.dmg
            print "You have", self.plhp, "left."
            if self.plhp <= 0:
                print "You've died. Sorry bro!"
                break
            elif self.hp <=0:
                print "You've killed the", self.name, "! Yay! You win!"
                break
            else:
                pass

    def flee(self):
        if self.plhp >0:
            roll = random.randrange(1,7)
            if roll == 1:
                print "You escape by the neck of your hair! Phew!"
                sys.exit(0)
            else:
                print "You fail to escape."
                self.attack()
        else:
            print "You fail to escape!"


    def block(self):
        roll = random.randrange(1,7)
        if roll == 1:
            print "You block successfully!"
            self.choice()
        else:
            pass


    def potion(self):
        self.plhp += 5
        self.attack()

    def choice(self):
        choice = raw_input("What do you want to do?\n'flee'\n'attack'\ndrink 'potion'\n")
        if choice == 'flee' or choice.lower == 'flee':
            self.flee()
        elif choice == 'attack' or choice.lower == 'attack':
            self.attack()
        elif choice == 'drink' or choice == 'potion' or choice.lower == 'drink' or choice.lower == 'potion':
            self.potion()
        else:
            print "Incorrect output. Try again.\n"
            self.choice()










#enemy = Helga()

human = player("Kail",20,2)
#human.start()
fight = battle()
fight.choice()
#fight.attack()
#x = Helga()
#x.attack()