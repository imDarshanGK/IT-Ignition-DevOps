# Task
# Objective
# LAB 1 : Write a Python function is prime_or_even_odd(n) that takes an integer n as input and performs the following:

# If n is a prime number, return True.
# If n is not a prime number, return "Even" if n is even, or "Odd" if n is odd. 

# Constraint
# The input will be an integer between 1 and 1000. 


def is_prime_or_even_odd(n):
    if n < 2:
        return False #not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Even" if n % 2 == 0 else "Odd"
    return True #prime