'''
Task
Objective
LAB 1:
Write a Python function divide_numbers(num1, num2) that takes two numbers as input and returns their division. 
If the second number is zero, raise a ZeroDivisionError and handle it by returning the message "Error: Division by zero is not allowed."

Constraint
num1 and num2 are integers between -100 and 100.
You must handle the ZeroDivisionError explicitly.
'''

def divide_numbers(num1, num2):
    if not (-100 <= num1 <= 100) or not (-100 <= num2 <= 100):
        return "Error: Input numbers must be between -100 and 100."
    try:
        division = num1 / num2
        return division
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
