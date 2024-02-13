#problem2.py

'''
title: Problem 2
author: Abbas Rizvi
date: 2024/02/02
'''

multiples = []
size = int(input())
mult = int(input())

for i in range(size+1):
    if i != 0:
        multiples.append(mult*i)

formatted_multiples = ''
for i in range(len(multiples)):
    formatted_multiples += (str(multiples[i])+' ')
    formatted_multiples.rstrip()

print(formatted_multiples)