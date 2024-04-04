'''
Write a Python program that opens and reads a file named letter_scores.txt. The 
contents of letter_scores.txt is several lines with each line containing one 
character and one integer separated by a space. Each line tells you how many 
points the given character is worth when used in a word for a word game, in 
this word game the score of a word is the total of the points each character 
used in it are worth. Any character that does not show up in letter_scores.txt 
is considered to be worth 0 points.

After reading the file your program must read one string from input which will 
be a word and print out how many points that word is worth according to the 
information you read in from letter_scores.txt. Your program should simply 
print out only the integer score of the word read in, and nothing else.
'''

file = open("letter_scores.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

letter_points = {}
for line in lines:
    value = line.strip().split()
    letter = value[0]
    points = int(value[1])
    letter_points[letter] = points
    
word = input()
total = 0

for letter in word:
    if letter in letter_points:
        total += letter_points.get(letter)
        
print(total)