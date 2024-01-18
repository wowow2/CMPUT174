#temperature.py

'''
title: Temperature
author: Abbas Rizvi
date: 2024/01/17
'''

# Input
degrees_celsius = int(input("What is the current temperature in Canada? ")) # Asks the user what temperature it is in Canada, saves it as int

# Processing
degrees_fahrenheit = int(round(((degrees_celsius * 9)/5) + 32)) # Converts user input from C to F, rounds it, saves it as int

# Output
print(f"{degrees_celsius} degrees in Canada would be {degrees_fahrenheit} degrees in Springfield. D'oh! ") # delivers formatted output
