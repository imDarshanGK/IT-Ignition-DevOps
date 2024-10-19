'''
Task
Objective
LAB 1:
Create a Python class named Book that represents a book with two attributes: title (a string) and author (a string). 

Implement a method named display_info that prints the title and author of the book in the format "Title: <title>, Author: <author>". 

After creating the class, instantiate an object of the Book class and call the display_info method to display the information.

Expected Output:
The display_info method should print the title and author in the format described above.

 Constraint      
The title and author should both be non-empty strings.
The method should not return any value, only print the output.
'''


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")
