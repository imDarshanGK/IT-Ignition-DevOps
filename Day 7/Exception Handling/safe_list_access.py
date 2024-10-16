'''Task
Objective
LAB 3 :
Write a Python function safe_list_access(my_list, index) that takes a list my_list and an integer index as input and returns the element at the given index. 
If the index is out of range, raise an IndexError and handle it by returning the message "Error: Index out of range."

Constraint
my_list will contain at least 1 integer and at most 200 integers.
index is an integer that can be any value (positive or negative).
'''

def safe_list_access(my_list, index):
    try:
        element = my_list[index]
        return element
    except IndexError:
        return "Error: Index out of range."
