"""
Task
Objective
On the normalized tables created in the previous activity, Create
the following indexes:
A clustered index on the Customer ID column in the Customers

Constraint
Ensure the clustered index is created on the primary key column Customer ID

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

CREATE INDEX idx_product_name ON Products(ProductName);