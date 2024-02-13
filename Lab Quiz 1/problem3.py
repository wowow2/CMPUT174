#problem3.py

'''
title: Problem 3
author: Abbas Rizvi
date: 2024/02/02
'''

divisors = []
integer = int(input())

for i in range(integer+1):
    if i != 0:
        div = integer/i
        if div == int(div):
            div = int(div)
            divisors.append(div)
        else:
            pass

formatted_divisors = ''
divisors = divisors[::-1]
for i in range(len(divisors)):
    formatted_divisors += (str(divisors[i])+' ')
    formatted_divisors.rstrip()

print(formatted_divisors)