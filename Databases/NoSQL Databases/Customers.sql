"""
Task
Objective
Create a collection called Customers in a NoSQL database.
Insert three customer documents into the Customers collection with the following details:
Rahul Sharma, 35, Purchases: ["Laptop", "Phone"]
Vikram Seth, 28, Purchases: ["Tablet", "Headphones"]
Anjali Gowda, 40, Purchases: ["Camera", "Tripod"]

Constraint

No specific schema is required, but documents will include fields for name, age, and purchases (an array).
"""

use ecommerce;

db.Customers.insertMany([
  {
    name: "Rahul Sharma",
    age: 35,
    purchases: ["Laptop", "Phone"]
  },
  {
    name: "Vikram Seth",
    age: 28,
    purchases: ["Tablet", "Headphones"]
  },
  {
    name: "Anjali Gowda",
    age: 40,
    purchases: ["Camera", "Tripod"]
  }
]);

db.Customers.find().pretty();
