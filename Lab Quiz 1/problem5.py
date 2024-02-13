#problem5.py

'''
title: Problem 5
author: Abbas Rizvi
date: 2024/02/02
'''

number_e = 0
string = list(input())

for i in range(len(string)):
    if string[i].lower() == "e":
        number_e += 1
    else:
        pass

print(number_e)

