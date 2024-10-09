# Task
# Objective
# LAB 5 : Write a Python function pandas_operations() -> dict that performs the following operations using the Pandas library:
# Create a DataFrame with the following data:
# {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
# Filter the DataFrame to include only rows where the Age is greater than 28.
# Calculate the sum of the Age column.
# The function should return a dictionary containing the filtered DataFrame and the sum of ages.

# Constraint
# Use the pandas library for data manipulation.
# The function should not accept any arguments.


import pandas as pd
def pandas_operations() -> dict:
    Data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35]
        }
    frame = pd.DataFrame(Data)
    filtered_data = frame[frame['Age'] > 28]
    age_sum = frame['Age'].sum()
    results = {
        "filtered_data": filtered_data,
        "age_sum": age_sum
    }
    return results
