#!/usr/bin/env python


import random, json


class Player:
    
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.gold = 10
        self.inventory = {}
        self.keyitems = []
        self.weapon = 'fists'
        self.weapondata = {'name': 'fists', 'damage': 1, 'description': 'Bare knuckles'}
        self.max_hp = 10
        self.hp = 10
        self.damage = [1,1]
        self.name = 'Chosen One'
        self.defense = 0
        self.armor = {}
        self.questlog = {}
    
    #Returns the amount of damage being done    .
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
            print("'{}' successfully equipped.".format(name))
        else:
            print("Unable to equip '{}'. Not found in inventory.".format(name))
    
    #Equips article of armor passed in.  
    def equip_armor(self, armor):
        armortypes = ['chest','arms','legs','hands','feet','head','shield']
        if (armor in self.inventory) and ('type' in self.inventory[armor]) and (self.inventory[armor]['type'] in armortypes):
            armordata = self.inventory[armor]
            #Unequip current armor if any.
            for key,value in self.armor.items():
                if value['type'] == armordata['type']:
                    self.unequip_armor(key)
                    break
            self.armor[armor] = armordata
            del self.inventory[armor]
            self.calculate_defense()
            print("'{}' successfully equipped.".format(armor))
          
                    
                    
        else:
            print("Cannot equip '{}'. Valid armor must be provided with correct type:\n".format(armor) + " : ".join(armortypes))
    
    #Unequips name of armor passed in.
    def unequip_armor(self, armor):
        if armor in self.armor:
            self.inventory[armor] = self.armor[armor]
            del self.armor[armor]
            self.calculate_defense()
            print("'{}' successfully unequipped.".format(armor))
        else:
            print("Can't unequip '{}'. Not a valid equipped armor.".format(armor))
    
    #Unequips name of weapon passed in.        
    def unequip_weapon(self, item):
        if ((item == 'weapon') or (item == self.weapon)):
            self.inventory[self.weapon] = self.weapondata
            self.weapon = 'fists'
            self.weapondata = {'name': 'fists', 'damage': [1,1], 'description': 'Bare knuckles'}
            self.damage = [1,1]
            print("'{}' successfully unequipped.".format(item))
        else:
            print("Failed to unequip '{}'. Not a valid equipped item.".format(item))
    
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
        print("'{}' added to inventory.".format(item))
        
    #Deletes an item from the inventory
    def remove_item(self, item):
        if item in self.inventory:
            del self.inventory[item]
            print("'{}' removed from inventory.".format(item))
        else:
            print("'{}' not in inventory.".format(item))
    
    #Adds a keyitem to the key items list as well as stores it in inventory.
    def add_keyitem(self, item, itemvalue):
        self.keyitems.append(item)
        self.inventory[item] = itemvalue
        print("'{}' added to key items.".format(item))
    
    #Removes a key item from inventory.
    def remove_keyitem(self, item):
        if item in self.keyitems:
            self.keyitems.remove(item)
            del self.inventory[item]
            print("'{}' removed from keyitems and inventory.".format(item))
        else:
            print("Key item not acquired.")
    
    #Adds gold.    
    def add_gold(self, cnt):
        self.gold += cnt
        print("{} gold added.".format(cnt))
    
    #Removes specified gold.    
    def remove_gold(self, cnt):
        self.gold -= cnt
        print("{} gold removed.".format(cnt))
    
    #Buys item passed in for gold passed in.
    def buy(self, gold, item, itemvalue):
        if (self.gold - gold) >= 0:
            self.add_item(item, itemvalue)
            self.gold -= gold
            print("'{}' bought for {} gold.".format(item, gold))
        else:
            print("Not enough gold.")
    
    #Sells item passed in for gold passed in.
    def sell(self, item, gold):
        if item in self.inventory:
            del self.inventory[item]
            self.gold += gold
            print("'{}' sold for {} gold.".format(item, gold))
        else:
            print("'{}' not in inventory.".format(item))
    
    #Prints out inventory.     
    def show_inventory(self):
        print("Inventory:\n")
        for i in self.inventory:
            print("- {}".format(i))
        return input("\nPress enter to continue.\n")
    
    #Loads player stats from data dictionary passed in.
    def load_player(self, data):
        try:
            self.level = data['level']
            self.name = data['name']
            self.hp = data['hp']
            self.max_hp = data['max_hp']
            self.inventory = data['inventory']
            self.keyitems = data['keyitems']
            self.weapondata = data['weapondata']
            self.gold = data['gold']
            self.armor = data['armor']
            self.defense = self.calculate_defense()
            self.questlog = data['questlog']
            self.exp = data['exp']
            try:
                self.damage = self.weapondata['damage']
                self.weapon = self.weapondata['name']
            except Exception as e:
                pass
            print("Player {} successfully loaded.".format(self.name))
        except Exception as e:
            print("Failed to load character.", e)
    
    #Renames duplicate item.
    def rename_item(self, item):
        while True:
            if item in self.inventory:
                print("This item ({}) already exists in inventory. Please rename.".format(item))
                name = input("New Item Name: ")
                return name  
            else:
                return item
    
    #Saves character stats.        
    def character_save(self):
        stats = {}
        stats['name'] = self.name
        stats['level'] = self.level
        stats['hp'] = self.hp
        stats['max_hp'] = self.max_hp
        stats['weapondata'] = self.weapondata
        stats['inventory'] = self.inventory
        stats['keyitems'] = self.keyitems
        stats['gold'] = self.gold
        stats['armor'] = self.armor
        stats['questlog'] = self.questlog
        stats['exp'] = self.exp
        return stats
    
    #Prints out character data.    
    def __str__(self):
        return "Name: {}, Level: {}, HP: {}, Weapon: {}, Damage: {}, Defense: {}, Gold: {}, Armor: {},\n\nKey Items: {}\n\nInventory: {}\n".format(self.name,self.level,self.hp,self.weapon,self.damage,self.defense,self.gold,self.armor,self.keyitems,self.inventory)


if __name__ == "__main__":
    p = Player()

    
    armor = {'type': 'chest', 'name': "Iron Breastplate", 'defense': 5}
    helmet = {'type': 'head', 'name': "Iron Helmet", 'defense': 2}
    shelmet = {'type': 'head', 'name': "Skull Helmet", 'defense': 1}
    
    p.add_item('dagger', {'damage': [1,4], 'name': 'dagger'})
    p.add_item('dagger', {'damage': [1,4], 'name': 'dagger'})
    p.add_item(armor['name'], armor)
    p.add_item(helmet['name'], helmet)
    p.add_item(shelmet['name'], shelmet)
    
    p.equip_weapon('Shiny dagger')
    p.unequip_weapon('Shiny dagger')
    
    p.unequip_weapon('dagger')
    p.equip_weapon('dagger')
    p.equip_weapon('Shiny dagger')
    
    p.equip_armor(armor['name'])
    p.equip_armor(helmet['name'])
    p.equip_armor(shelmet['name'])
    
    p.equip_armor('dagger')
    
    
