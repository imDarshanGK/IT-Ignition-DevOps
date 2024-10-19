'''
Task
Objective
LAB 1 :
Write a Python function create_data_structures() that performs the following tasks:

1. Create a list called my_list containing the numbers [1, 2, 3].
2. Create a tuple called my_tuple containing the strings ("apple", "banana", "cherry").
3. Create a dictionary called my_dict with keys as {"name": "Alice", "age": 25}.
4. Create a set called my_set with values {1, 2, 3}.

Your function should return all four data structures as a tuple in the order: (list, tuple, dictionary, set).

Constraint
The list will contain exactly 3 integers.
The tuple will contain exactly 3 strings.
The dictionary will have two key-value pairs: one string (name) and one integer (age).
The set will contain 3 unique integers.
'''

def create_data_structures():
    my_list =  [1, 2, 3]
    my_tuple = ("apple", "banana", "cherry")
    my_dict = {"name": "Alice", "age": 25}
    my_set =  {1, 2, 3}
    return my_list, my_tuple, my_dict, my_set