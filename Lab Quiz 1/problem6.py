#problem6.py

'''
title: Problem 6
author: Abbas Rizvi
date: 2024/02/02
'''

same_pos = 0
word1 = list(input())
word2 = list(input())

for i, j in zip(word1, word2):
    if i == j:
        same_pos += 1
    else:
        pass

print(same_pos)