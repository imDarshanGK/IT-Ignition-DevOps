# Task
# Objective
# LAB 1 :
# Write a Python function math_operations(num: int) -> dict that takes a user input  integer num and returns a dictionary containing:
# The square root of num.
# The sine of 90 degrees.
# The factorial of num.

# Constraint
# num will be a non-negative integer between 1 and 100.
# For sine calculation, convert degrees to radians using the math.radians() function.
# Use the math module to perform these operations.


import math
def math_operations(num: int) -> dict:
    if not(1<= num <=100):
        return ValueError("1 to 100")
    results = {
        "square_root": math.sqrt(num),
        "sine_90": math.sin(math.radians(90)),
        "factorial": math.factorial(num)
    }
    return results