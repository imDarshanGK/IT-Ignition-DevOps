"""
Task
Objective
Write a query to retrieve all employees who work in the "IT"
department.

Constraint

Use a WHERE clause to filter data based on the Department

"""

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(50),
    Department VARCHAR(50)
);

INSERT INTO Employees (EmployeeID, EmployeeName, Department)
VALUES
(1, 'John Doe', 'IT'),
(2, 'Jane Smith', 'HR'),
(3, 'Emily Johnson', 'IT'),
(4, 'Michael Brown', 'Finance');

SELECT * 
FROM Employees
WHERE Department = 'IT';