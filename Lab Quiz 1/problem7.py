#problem7.py

'''
title: Problem 7
author: Abbas Rizvi
date: 2024/02/02
'''

word = list(input())

first_letter = word.pop(0)
word.append(first_letter)

pig_latin = ''
for i in range(len(word)):
    pig_latin +=word[i]

pig_latin += 'ay'

print(pig_latin)

