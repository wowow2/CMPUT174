# klingon-quiz1.py

'''
title: klingon quiz 1
author: Abbas Rizvi
date: 2024/02/12
'''

## Opening the File
f = open("klingon-english.txt", "r", encoding='utf-8')
lines = (f.readlines())
third_line = lines[2]
third_lines = third_line.split('|') # Splits lines into klingon and english words

input = input("How do you translate computer to Klingon?")

if input == third_lines[0]: # compares input with klingon word
    print("Correct")
else:
    print("Sorry, you're wrong! The correct answer is De'wI'")