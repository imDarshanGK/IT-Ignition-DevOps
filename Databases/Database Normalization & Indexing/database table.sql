"""
Task

Objective

You are given a sample database table containing the following data:
Columns: 
Order ID, Customer Name, Product Name, Customer Address
Rows:
Row 1: Order ID is 1, Customer Name is Raj Sharma, Product Name is Rice, Customer Address is Delhi.
Row 2: Order ID is 2, Customer Name is Priya Singh, Product Name is Wheat, Customer Address is Mumbai.

Normalize this table by splitting it into two tables:
Customers Table: This table should have the following columns:
 Customer ID (integer, primary key)
 Customer Name (string, maximum length 50)
 Customer Address (string, maximum length 50)
Products Table: This table should have the following columns:
 Product ID (integer, primary key)
 Product Name (string, maximum length 50)

Populate the Customers and Products tables with data from the sample database. Assign unique ID to Customer ID and Product ID.

Constraint
Use appropriate data types for all columns.
Ensure the tables adhere to first normal form (1NF)

"""

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    CustomerAddress VARCHAR(50)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Customers (CustomerID, CustomerName, CustomerAddress)
VALUES
(1, 'Raj Sharma', 'Delhi'),
(2, 'Priya Singh', 'Mumbai');

INSERT INTO Products (ProductID, ProductName, CustomerID)
VALUES
(1, 'Rice', 1),
(2, 'Wheat', 2);

SELECT * FROM Customers;
SELECT * FROM Products;