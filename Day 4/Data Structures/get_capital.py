'''
Task
Objective
LAB 3 :
Write a Python function get_capital(capitals, country) that takes a dictionary capitals and a string country, and returns the capital of that country.

Constraint
The dictionary will contain up to 5 country-capital pairs.
The country input will be a string with a length between 1 and 30.
'''

def get_capital(capitals, country):
    return capitals[country]  