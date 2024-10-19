'''
Task
Objective
LAB 5 :
Write a Python class called Laptop that has two attributes: brand (a string) and ram (an integer representing RAM in GB). 

Implement a method upgrade_ram that takes an additional RAM value (integer) and adds it to the existing RAM.  After upgrading, the method prints the updated RAM.

Expected Output:
The upgrade_ram method should print the updated RAM value in the format: "RAM upgraded to <new_ram>GB".

Constraint
The ram attribute must be a positive integer.
The upgrade_ram method should accept only positive integers and should not allow negative or zero values.
'''


class Laptop:
    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram
    def upgrade_ram(self, RAM):
        if isinstance(RAM, int) and RAM > 0:
            self.ram += RAM
            print(f"RAM upgraded to{self.ram}GB..")
        else:
            print("Invalid RAM value")