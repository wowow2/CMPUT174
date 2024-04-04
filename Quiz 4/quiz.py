'''
def count_occurrences(alist):
    count = {}
    for item in alist:
        if item in count:
            count[item] = count[item] + 1
        else:
            count[item] = 1
    return count

print(count_occurrences([]))
'''

'''
def create_grade_book(names, scores):
    grade_book = {}
    for index in range(len(names)):
        grade_book[names[index]] = scores[index]
    return grade_book

print(create_grade_book(['Fred','Bob','Mike'], [56,72,83]))
'''
import random

def place_ghosts(board,ghosts):
    m = len(board)
    n = len(board[0])

    ghost_locations = []

    for ghost in ghosts:
        placed = False
        while not placed:
            row = random.randint(0,m-1)
            col =