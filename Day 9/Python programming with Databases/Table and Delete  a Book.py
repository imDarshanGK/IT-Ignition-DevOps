'''
Task 
Objective
LAb 4:  Create Table and Delete a Book

Question Text:
Create a table named Books with the following columns:
           BookID (INT, Primary Key, Auto Increment)
           Title (VARCHAR)
           Author (VARCHAR)
           Genre (VARCHAR)
           YearPublished (INT)

After creating the table, insert the following books:
           "The Alchemist" | "Paulo Coelho" | "Fiction" | 1988
            "1984" | "George Orwell" | "Dystopian" | 1949

Write a SQL query to retrieve all books

Write a SQL query to delete the book with BookID = 2.

Write a SQL query to retrieve all books. It should return only one row with BookID = 1.

Constraint
The table should be created from scratch.
Ensure that the book with BookID = 2 exists before attempting to delete it.
'''

CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Genre VARCHAR(255) NOT NULL,
    YearPublished INT NOT NULL
);

INSERT INTO Books (Title, Author, Genre, YearPublished)
VALUES ('The Alchemist', 'Paulo Coelho', 'Fiction', 1988);
INSERT INTO Books (Title, Author, Genre, YearPublished)
VALUES("1984", "George Orwell", "Dystopian", 1949);

DELETE FROM Books WHERE BookID = 2;

SELECT * FROM Books;