# Task
# Objective
# LAB 2 : Write a Python function calculate_age(birth_year) that takes the birth year as input and returns the current age based on the current year 2023.
# Input:
# The function takes an integer birth_year as input.
# Output:
# The function returns an integer representing the user's age.

# Constraint
# The input birth_year will be a positive integer between 1900 and 2023.
# The output should be a non-negative integer.

def calculate_age(birth_year):
    current_year = 2023
    if isinstance(birth_year, int) and 1900 <= birth_year <= current_year:
        age = current_year - birth_year
        return age
    else:
        raise ValueError("Input must be a positive integer between 1900 and 2023.")
