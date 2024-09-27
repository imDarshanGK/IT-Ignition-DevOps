# Task
# Objective
# LAB 1 : 
# Write a Python function greet_user(name) that accepts the user's name as a parameter and returns  a greeting message.

# Input:
# The function will accept a single parameter name which is a string.
# Output:
# The function should return "Hello, <name>!" where <name> is the value passed as the parameter.

# Constraint
# The input should be a non-empty string.
# The name will not contain any special characters or numbers.###


def greet_user(name):
    if isinstance(name, str) and name:
        return f"Hello, {name}!"
    else:
        raise ValueError("Input must be a non-empty string.")
