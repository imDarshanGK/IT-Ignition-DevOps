# Task
# Objective
# LAB 3  :
# Write a Python function file_system_operations() -> dict that performs the following operations using the os module and returns a dictionary with:
# The current working directory.
# A list of files in the current directory.
# A confirmation message after creating a new directory called 'new_folder'.

# Constraint
# Use the os module for all file system operations.
# The function should not accept any arguments.


import os
def file_system_operations() -> dict:
    current_directory = os.getcwd()
    files_list = os.listdir(current_directory)
    new_folder_name = 'new_folder'
    try:
        os.makedirs(new_folder_name, exist_ok=True)
        if os.path.exists(new_folder_name):
            confirmation_message = f"'{new_folder_name}' has been created successfully."
        else:
            confirmation_message = f"Failed to create '{new_folder_name}'."
    except Exception as e:
        confirmation_message = str(e)
    result = {
        'current_working_directory': current_directory,
        'files_in_directory': files_list,
        'new_directory_confirmation': confirmation_message
    }
    return result