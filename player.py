#!/usr/bin/env python


import random, json
from contextlib import suppress

'''
Later additions (To-do list):
Injury status
Move comments into docstring formats
Add functions for leveling, experience and questlog management
Research pydantic
'''

class Player:
    
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.gold = 10
        self.inventory = {}
        self.keyitems = []
        self.weapon = 'fists'
        self.weapondata = {'name': 'fists', 'damage': 1, 'description': 'Bare knuckles, the way mama intended!'}
        self.max_hp = 10
        self.hp = 10
        self.damage = [1,1]
        self.name = 'Chosen One'
        self.defense = 0
        self.armor = {}
        self.questlog = {}
        self.battle_count = 0
    
    #Returns the amount of damage being done
    def attack(self):
        return random.randint(self.damage[0], self.damage[1])
    
    #Prevents damage and returns heal amount.
    def defend(self):
        defended = random.randint(0,self.defense)
        self.hp += defended
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return defended
    
    #Decrements life and returns life remaining.
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            return 0
        else:
            return self.hp

    #Equips name of new weapon passed in.
    def equip_weapon(self, name):
        if name in self.inventory:
            if self.weapon != 'fists':
                self.unequip_weapon(self.weapon)
            self.weapon = name
            self.weapondata = self.inventory[name]
            self.damage = self.weapondata['damage']
            print(f"'{name}' successfully equipped.\n")
        else:
            print(f"Unable to equip '{name}'. Not found in inventory.\n")

    # Unequips name of weapon passed in.
    def unequip_weapon(self,name):
        if ((name == 'weapon') or (name == self.weapon)):
            self.inventory[self.weapon] = self.weapondata
            self.weapon = 'fists'
            self.weapondata = {'name': 'fists', 'damage': [1, 1], 'description': 'Bare knuckles'}
            self.damage = [1, 1]
            print(f"'{name}' successfully unequipped.\n")
        else:
            print(f"Failed to unequip '{name}'. Not a valid equipped item.\n")

    def show_weapon(self):
        print("#------------------------#")
        print(f"Equipped weapon:\n - {self.weapon}")
        for key,val in self.weapondata.items():
            print("  --",key,":",val)
        print("#------------------------#")

    #Equips article of armor passed in.  
    def equip_armor(self, armor):
        armortypes = ['chest','arms','legs','hands','feet','head','shield']
        if (armor in self.inventory) and ('type' in self.inventory[armor]) and (self.inventory[armor]['type'] in armortypes):
            armordata = self.inventory[armor]
            #Unequip current armor if any.
            for key,value in self.armor.items():
                if value['type'] == armordata['type']:
                    print(f"Already wearing {value['type']} type armor: {value['name']}. Unequipping.")
                    self.unequip_armor(key)
                    break
            self.armor[armor] = armordata
            del self.inventory[armor]
            self.calculate_defense()
            print(f"'{armor}' successfully equipped.")
            print(f"Current Defense: {self.defense}\n")
        else:
            print(f"Cannot equip '{armor}'. Valid armor must be provided with correct type:\n" + " : ".join(armortypes))
    
    #Unequips name of armor passed in.
    def unequip_armor(self, armor):
        if armor in self.armor:
            self.inventory[armor] = self.armor[armor]
            del self.armor[armor]
            self.calculate_defense()
            print(f"'{armor}' successfully unequipped.")
            print(f"Current Defense: {self.defense}\n")
        else:
            print(f"Can't unequip '{armor}'. Not a valid equipped armor.\n")

    # Shows currently equipped armor
    def show_armor(self):
        if len(self.armor) == 0:
            print("No armor currently equipped.\n")
        else:
            print("#------------------------#")
            print("Equipped Armor:")
            for a in self.armor:
                print(f"- {a}")
            print("#------------------------#")

    def show_all_equipment(self):
        self.show_weapon()
        self.show_armor()

    def manage_equipment(self):
        """ Access the player inventory menu """
        header = "#############################\n# Equipment Management Menu #\n#############################"
        #menuitems = ["Show Equipment", "Equip", "Unequip", "Done"]
        menuitems = ["Show Equipment", "Equip Weapon", "Equip Armor", "Unequip Weapon", "Unequip Armor", "Done"]
        calls = [self.show_all_equipment, self.equip_weapon, self.equip_armor, self.unequip_weapon, self.unequip_armor, self.close_menu]
        output = ""
        while output != "Done":
            output = self.universal_menu(menuitems, header)
            print(output)
            if output > 0 and output < 5:
                parts = menuitems[output].split(" ")
                choice = input(f"Which {parts[1].lower()} do you want to {parts[0].lower()}?\n> ")
                output = calls[output](choice)
            else:
                output = calls[output]()
        print("Exiting menu.")
        return input("\nPress enter to continue.\n")

    #Calculates new defense after equipping armor.
    def calculate_defense(self):
        defense = 0
        for key,value in self.armor.items():
            defense += value['defense']
        self.defense = defense
            
    #Adds an item to inventory and calls rename to prevent duplicates.
    def add_item(self, item, itemvalue):
        item = self.rename_item(item)
        if type(itemvalue) == dict:
            itemvalue['name'] = item
        self.inventory[item] = itemvalue
        print(f"'{item}' added to inventory.\n")
        
    #Deletes an item from the inventory
    def remove_item(self, item):
        if item in self.inventory:
            del self.inventory[item]
            print(f"'{item}' removed from inventory.\n")
        else:
            print(f"'{item}' not in inventory.\n")
    
    #Adds a keyitem to the key items list as well as stores it in inventory.
    def add_keyitem(self, item, itemvalue):
        self.keyitems.append(item)
        self.inventory[item] = itemvalue
        print(f"'{item}' added to key items.\n")
    
    #Removes a key item from inventory.
    def remove_keyitem(self, item):
        if item in self.keyitems:
            self.keyitems.remove(item)
            del self.inventory[item]
            print(f"'{item}' removed from keyitems and inventory.\n")
        else:
            print("Key item not acquired.\n")
    
    #Adds gold.    
    def add_gold(self, cnt):
        self.gold += cnt
        print(f"{cnt} gold added.\n")
    
    #Removes specified gold.    
    def remove_gold(self, cnt):
        self.gold -= cnt
        print(f"{cnt} gold removed.\n")
    
    #Buys item passed in for gold passed in.
    def buy(self, gold, item, itemvalue):
        if (self.gold - gold) >= 0:
            self.add_item(item, itemvalue)
            self.gold -= gold
            print(f"'{item}' bought for {gold} gold.\n")
        else:
            print("Not enough gold.\n")
    
    #Sells item passed in for gold passed in.
    def sell(self, item, gold):
        if item in self.inventory:
            del self.inventory[item]
            self.gold += gold
            print(f"'{item}' sold for {gold} gold.\n")
        else:
            print(f"'{item}' not in inventory.\n")
    
    #Prints out inventory.     
    def show_inventory(self):
        if len(self.inventory) == 0:
            print("Inventory currently empty.\n")
        else:
            print("#------------------------#")
            print("Inventory:")
            for i in self.inventory:
                print(f"- {i}")
            print("#------------------------#")
        return input("\nPress enter to continue.\n")

    def player_menu(self):
        header = "###############\n# Player Menu #\n###############"
        menuitems = ["Manage Inventory","Manage Equipment","Show Stats","Done"]
        calls = [self.manage_inventory,self.manage_equipment,self.show_stats,self.close_menu]
        output = ""
        while output != "Done":
            output = calls[self.universal_menu(menuitems,header)]()
        print("Exiting menu.")
        return input("\nPress enter to continue.\n")

    def close_menu(self):
        return "Done"

    def manage_inventory(self):
        """ Access the player inventory menu """
        header = "##################\n# Inventory Menu #\n##################"
        menuitems = ["Show Inventory", "Inspect Item", "Discard Item", "Done"]
        calls = [self.show_inventory,self.inspect_item,self.discard_item,self.close_menu]
        output = ""
        while output != "Done":
            output = calls[self.universal_menu(menuitems,header)]()
        print("Exiting menu.")
        return input("\nPress enter to continue.\n")

    # Skyler's voodoo magic with some updates
    def universal_menu(self, menuitems: list, header: str = "") -> str | None:
        """ Generate a generic Menu based on *menuitems*. """
        while True:

            if header:
                print(f"{header}", sep="\n")

            #Skyler's version
            for k, v in enumerate(menuitems, start=1):
                print(f"{k:d}. {str(v).title()}")
            answer = input("Select an Option (by number or name)\n> ").title()
            with suppress(ValueError, IndexError):
                #return menuitems[int(answer) - 1].title()  # because 0-indexing - used for returning a string
                menusize = len(menuitems)
                if (int(answer)) <= menusize:
                    return (int(answer)-1)
            if answer.title() in menuitems:
                #return answer.title() # for returning a string
                cnt = 1
                for x in menuitems:
                    if x == answer.title():
                        return cnt-1
                    else:
                        cnt += 1

            print("Incorrect answer. Try again.")

    def inspect_item(self):
        choice = input("Which item would you like to inspect more closely:\n> ")
        if choice.title() in self.inventory:
            item = self.inventory[choice.title()]
            for key,val in item.items():
                print(key.title()," : ",val)
        else:
            print("Not in your inventory. You don't have that. Face the facts that you lost it somewhere and move on. Or try again. Whatever. It's your time wasted, not mine.")

    def discard_item(self):
        choice = input("Which item would you like to discard:\n> ")
        if choice.title() in self.inventory:
            item = self.inventory[choice.title()]
            for key, val in item.items():
                print(key.title(), " : ", val)
            decision = input("Are you sure? (yes,no)\n> ")
            if decision.lower() == 'yes':
                del self.inventory[choice.title()]
                print("Alright. It's done. Good riddance. I guess... Hope it wasn't important... *cough* hint hint *cough*")
            elif decision.lower() == 'no':
                print("Oh. Alright then. Thanks for wasting my time.")
            else:
                print("Come on. Stop playing games with me. You either do or you don't. It's a simple 'yes' or 'no' question.")
        else:
            print("You don't even have that! Maybe you should take another look at your inventory, BRO, and stop wasting my time!")

    #Print out all player stats
    def show_stats(self):
        print("Player stats:")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Current Experience: {self.exp}")
        print(f"Gold: {self.gold}")
        print(f"Max HP: {self.max_hp}")
        print(f"Current HP: {self.hp}")
        print(f"Current Defense: {self.defense}")

    # Renames duplicate item.
    def rename_item(self, item):
        while True:
            if item in self.inventory:
                print(f"This item ({item}) already exists in inventory. Please rename.")
                name = input("New Item Name: ")
                return name
            else:
                return item

    #Loads player stats from data dictionary passed in.
    def load_player(self, data):
        try:
            self.level = data['level']
            self.exp = data['exp']
            self.name = data['name']
            self.max_hp = data['max_hp']
            self.hp = data['hp']
            self.max_hp = data['max_hp']
            self.inventory = data['inventory']
            self.keyitems = data['keyitems']
            self.weapon = data['weapon']
            self.weapondata = data['weapondata']
            self.damage = data['damage']
            self.gold = data['gold']
            self.armor = data['armor']
            self.defense = self.calculate_defense()
            self.questlog = data['questlog']
            print(f"Player {self.name} successfully loaded.")
            return input("\nPress enter to continue.\n")
        except Exception as e:
            print("Failed to load character.", e)
            return input("\nPress enter to continue.\n")
    
    #Saves character stats.        
    def character_save(self):
        stats = {}
        stats['name'] = self.name
        stats['level'] = self.level
        stats['exp'] = self.exp
        stats['hp'] = self.hp
        stats['max_hp'] = self.max_hp
        stats['weapon'] = self.weapon
        stats['weapondata'] = self.weapondata
        stats['damage'] = self.damage
        stats['inventory'] = self.inventory
        stats['keyitems'] = self.keyitems
        stats['gold'] = self.gold
        stats['armor'] = self.armor
        stats['questlog'] = self.questlog
        return stats
    
    #Prints out character data.    
    def __str__(self):
        return "Name: {}, Level: {}, Exp: {}, Max HP: {}, Current HP: {}, Weapon: {}, Weapon Data: {}, Damage: {}, Defense: {}, Gold: {}, Armor: {},\n\nKey Items: {}\n\nInventory: {}\n".format(self.name,self.level,self.exp,self.max_hp,self.hp,self.weapon,self.weapondata,self.damage,self.defense,self.gold,self.armor,self.keyitems,self.inventory)


if __name__ == "__main__":
    p = Player()


    #Test inventory functions
    p.show_inventory()
    armor = {'type': 'chest', 'name': "Iron Breastplate", 'defense': 5}
    helmet = {'type': 'head', 'name': "Iron Helmet", 'defense': 2}
    shelmet = {'type': 'head', 'name': "Skull Helmet", 'defense': 1}

    p.add_item('Dagger', {'damage': [1,4], 'name': 'Dagger','description': 'Boring old dagger. The kind you buy from your standard market.'})
    p.add_item('Axe', {'damage': [1, 6], 'name': 'Axe'})
    p.add_item(armor['name'], armor)
    p.add_item(helmet['name'], helmet)
    p.add_item(shelmet['name'], shelmet)
    '''
    p.show_inventory()

    #Test armor functions
    p.equip_armor(shelmet['name'])
    p.equip_armor(armor['name'])
    p.show_armor()
    p.unequip_armor(shelmet['name'])
    p.show_armor()

    #Test Gold functions
    p.add_gold(20)
    p.remove_gold(10)

    #Test weapon functions
    p.equip_weapon('dagger')
    p.show_weapon()
    p.unequip_weapon('dagger')
    p.manage_equipment()

    #Test modified inventory
    p.show_inventory()

    #Test character object printout
    print(f"\nPlayer:\n{p}\n")

    #Test save and Load character
    kail = p.character_save()
    p.load_player(kail)
    p.show_stats()
    '''

    menuitems = ["Show Inventory", "Inspect Item", "Discard Item", "Done"]
    #choice = p.menu(menuitems)
    #print("Your choice:",choice)
    #p.player_menu()
    p.player_menu()
    #print("Your choice:", choice, "represents:", menuitems[choice-1])
    
