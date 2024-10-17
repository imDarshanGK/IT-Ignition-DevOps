'''
Task
Objective
LAB 4 : 
Write a Python function multiplication_table(number) that takes a number as input and prints its multiplication table from 1 to 10.

Constraint
The input will be an integer between 1 and 20. 
'''

def multiplication_table(number):
    for i in range(1, 11):
        print(f'{number} x {i} = {number * i}')