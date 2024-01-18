# episode.py

'''
title: Episode name Problem
author: Abbas Rizvi
date: 2024/01/17
'''

# Takes raw input from the user
raw_format = input("What is the name of the episode? ")

raw_format = raw_format.split('_') # Splits the given string into more workable pieces

# Picks out relevant data from the list
season = raw_format[0][1:] # season
episode = raw_format[1][1:] # episode
title = raw_format[2] # title

# Formats output in proper form
print(f'Season {season}, Episode {episode}: {title} (The Simpsons)')