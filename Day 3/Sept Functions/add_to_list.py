'''
Task
Objective
LAB 3 :
Write a Python function add_to_list(my_list, item) that takes a list my_list and an item item. The function should append the item to the list and return the updated list.

Constraint
The list will have a maximum length of 10.
The item can be any valid Python data type.
'''

def add_to_list(my_list, item):
    my_list.append(item)
    return my_list