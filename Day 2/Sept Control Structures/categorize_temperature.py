<<<<<<< HEAD
# Task
# Objective
# LAB 3 : Write a Python function categorize_temperature(temp) that takes a temperature (in Celsius) as input and returns:

# "Hot" if the temperature is above 30,
# "Warm" if the temperature is between 20 and 30 (inclusive), 
# "Cool" if the temperature is between 10 and 19 (inclusive),
#  "Cold" if the temperature is below 10.

# Constraint
# The input will be a float between -50.0 and 50.0. 

def categorize_temperature(temp):
    if temp > 30:
        return "Hot"
    elif temp >= 20 and temp <= 30:
        return "War"
    elif temp >=  10 and temp <= 19:
        return "Cool"
    else:
=======
# Task
# Objective
# LAB 3 : Write a Python function categorize_temperature(temp) that takes a temperature (in Celsius) as input and returns:

# "Hot" if the temperature is above 30,
# "Warm" if the temperature is between 20 and 30 (inclusive), 
# "Cool" if the temperature is between 10 and 19 (inclusive),
#  "Cold" if the temperature is below 10.

# Constraint
# The input will be a float between -50.0 and 50.0. 

def categorize_temperature(temp):
    if temp > 30:
        return "Hot"
    elif temp >= 20 and temp <= 30:
        return "War"
    elif temp >=  10 and temp <= 19:
        return "Cool"
    else:
>>>>>>> 2a56d59ae7ee7bfb256aeb7f68efbdeb6709b953
        return "Cold"