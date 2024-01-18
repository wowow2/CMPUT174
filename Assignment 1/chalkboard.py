### chalkboard.py

'''
title: chalkboard
author: Abbas Rizvi
date: 2024/01/17
'''

# Gathers and formats input
user_phrase = input('What is the phrase? ') # Asks user for the phrase
user_phrase = user_phrase + ' ' # Adds a space at the end of the recieved string
number_repeat = int(input('How many times do you want to write it? ')) # Asks user how many times they want phrase to be repeated

# Output
print(user_phrase * number_repeat) # Displays output in proper format