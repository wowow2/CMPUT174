# age4.py

'''
title: Fellowship of the Ring
author: Abbas Rizvi
date: 2024/01/27
Description: This program will compare the age of a character the user entered to the others in the program
'''

# Given data
names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

# Inputs
name_char = input("What is your character's name: ")
age_char = int(input("How old is your character: "))

# if entered age is less than 0, program stops
if age_char < 0:
    print("Invalid age")
    exit()

# Processing
older_char = []
younger_char = []

# traverses both lists and checks if character is older or younger
for i, j in zip(names, ages):
    # data is stored in 2 lists
    if age_char > j:
        older_char.append(i)
    elif age_char < j:
        younger_char.append(i)
    else:
        pass

# Creates a string with the names of characters which are older/younger
older = ''
for i in range(len(older_char)):
    older += older_char[i]+', '

younger = ''
for i in range(len(younger_char)):
    younger += younger_char[i]+ ', '

# Outputs
if len(older_char) > 0:
    print(f'{name_char} is {age_char} years old, and they are older than {older.rstrip().rstrip(",")}.')  # removes extra whitespaces and commas
elif len(younger_char) > 0:
    print(f'{name_char} is {age_char} years old, and they are younger than {younger.rstrip().rstrip(",")}.')
else:
    pass