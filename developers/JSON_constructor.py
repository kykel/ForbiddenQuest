#!/usr/bin/python3

#JSON Dictionary Constructor for Forbidden Quest

import sys

class Constructor():
    
    def __init__(self, name):
        dict_name = ""
        self.key = ""
        self.dictionary_name = name
        self.master_dict = {}
        self.substorage = []
        
    def menu(self):
        self.key = input("Enter new key name: ")
        self.populate_values()
    
    def populate_values(self):
        option = input("1. String\n2. Integer\n3. Float(decimal)\n4. List\n5. Dictionary\n6. Done\n")
        if option == "1":
            self.store_val(self.string_val())
            self.menu()
        elif option == "2":
            self.store_val(self.int_val(self.string_val()))
            self.menu()
        elif option == "3":
            self.store_val(self.float_val(self.string_val()))
            self.menu()
        elif option == "4":
            self.store_val(self.list_val())
        elif option == "5":
            self.store_val(self.dict_val())
        elif option == "6":
            if len(self.substorage) > 0:
                self.key = self.substorage.pop() #Not self.key. Fix this.
            else:
                sys.exit()
        
        
    def create_key(self):
        key = input("Enter key name: ")
        return key
        
    def string_val(self):
        val = input("Enter value: ")
        return val
    
    def int_val(self, val):
        val = int(val)
        return val
        
    def float_val(self, val):
        val = float(val)
        return val
        
    def list_val(self):
        data = []
        
    def dict_val(self):
        data = {}
        
    def store_val(self, val):
        self.master_dict[self.key] = val
            
        
if __name__ == "__main__":
    dict_name = input("Please enter the name of your JSON dictionary (no extensions): ")
    c = Constructor(dict_name)
    c.menu()