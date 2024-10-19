'''
Task
Objective
LAB 2 :
Write a Python function get_second_color(colors) that takes a tuple of colors as input and returns the second color in the tuple.

Constraint
The tuple will contain at least two colors, each as a string.
'''

def get_second_color(colors):
    return colors[1]
colors = ("red","blue","green")
second_color = get_second_color(colors)
print(second_color)