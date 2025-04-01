#!/usr/bin/python3

#JSON Dictionary Constructor for Forbidden Quest

import sys

class Constructor():
    
    def __init__(self, name):
        self.key = ""
        self.dictionary_name = name
        self.master_dict = {}
        self.substorage = []
        self.running_storage = ""
        
        
    def menu(self):
        self.key = self.create_key()
        self.populate_values()
    
    def populate_values(self):
        option = input("1. String\n2. Integer\n3. Float(decimal)\n4. List\n5. Dictionary\n6. Done\n")
        if option == "1":
            self.store_val(self.string_val())
        elif option == "2":
            self.store_val(self.int_val(self.string_val()))
        elif option == "3":
            self.store_val(self.float_val(self.string_val()))
        elif option == "4":
            self.list_val()
        #still working dictionary and list
        elif option == "5":
            self.dict_val()
        elif option == "6":
            pass
        
        
    def create_key(self):
        return input("Enter key name: ")
        
    def string_val(self):
        return input("Enter value: ")
    
    def int_val(self, val):
        return int(val)
        
    def float_val(self, val):
        return float(val)
        
    def list_val(self):
        self.running_storage = []
        
    def dict_val(self):
        self.running_storage = {}
        
    def store_val(self, val):
        self.master_dict[self.key] = val
        self.menu()
        
        
            
        
if __name__ == "__main__":
    dict_name = input("Please enter the name of your JSON dictionary (no extensions): ")
    c = Constructor(dict_name)
    c.menu()