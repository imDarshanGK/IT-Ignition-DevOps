'''
Task
Objective
LAB 2 :
Write a Python function get_current_datetime() -> dict that returns a dictionary containing:
The current date.
The current time.
The current date and time formatted as YYYY-MM-DD HH:MM:SS.

Constraint
Use the datetime module to get the current date and time.
The function should not accept any arguments.
'''

from datetime import datetime
def get_current_datetime() -> dict:
    now = datetime.now()
    current_date = now.date()
    current_time = now.time()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return {
        "current_date": current_date,
        "current_time": current_time,
        "formatted_datetime": formatted_datetime
    }