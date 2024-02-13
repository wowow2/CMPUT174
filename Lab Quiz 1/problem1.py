#problem1.py

'''
title: Problem 1
author: Abbas Rizvi
date: 2024/02/02
'''

int_list = []

integer = input()

while integer != "q":
    integer = int(integer)
    int_list.append(integer)
    integer = input()

if integer == "q":
    print(max(int_list))
