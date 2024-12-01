"""
Task
Objective
Create a table called Employees with columns for Name, Age,
and Department. Define appropriate data types for each field.
Insert three employees into the Employees table with the
following details:
Anjali, 30, HR
Vikram, 25, IT
Rahul, 28, Finance

Constraint

Name: A string with a maximum length of 50 characters.
Age: An integer.
Department: A string with a maximum length of 50 characters.
Insert each employee as a separate SQL statement
"""

CREATE TABLE Employees (
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(50)
);

INSERT INTO Employees (Name, Age, Department) VALUES ('Anjali', 30, 'HR');
INSERT INTO Employees (Name, Age, Department) VALUES ('Vikram', 25, 'IT');
INSERT INTO Employees (Name, Age, Department) VALUES ('Rahul', 28, 'Finance');
