'''
Task
Objective
LAB 2:
Create a class named Employee that contains a private attribute called __salary (a float). 

Implement a method get_salary that prints and returns the current salary, and a method set_salary that updates the salary, but prints the updated salary.

You should create an object of the Employee class and first call the get method, and then the set method.

Expected Output:
get_salary should print the current salary.
set_salary should only update and print the new salary if it's greater than 0.

Constraint
The salary should always be a positive number.
The setter should prevent negative values and zero from being set as the salary.
The getter should return the salary as a floating-point number.
'''

class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def get_salary(self):
        print(f"Current Salary: {self.__salary}")
        return self.__salary
    def set_salary(self, new_salary):
        if new_salary <= 0:
            print("Salary not updated..")
        else:
            self.__salary = float(new_salary)
            print(f"Updated Salary: {self.__salary}")