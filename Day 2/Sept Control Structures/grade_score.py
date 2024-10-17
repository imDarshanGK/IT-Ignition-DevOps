'''
Task
Objective
LAB 2 : Create a Python function grade(score) that takes a student's score (integer) as input and returns a grade as per the following rules:

A: if score >= 90 
B: if score >= 80
C: if score >= 70
D: if score >= 60
F: if score < 60 

Constraint
Input: score must be an integer between 0 and 100 inclusive.
Output: Returns a single character string: 'A', 'B', 'C', 'D', or 'F'.
Errors:
Raise ValueError if score is out of range (0-100).
Raise TypeError if score is not an integer.
'''


def grade(score):
    if not isinstance(score, int):
        raise TypeError("Score must be an integer.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive.")
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'