"""
Task
Objective
Query the collection to find all customers who have purchased a"Laptop."

Constraint

Use a find function to filter data.
"""

db.Customers.find({
  purchases: "Laptop"
}).pretty();
