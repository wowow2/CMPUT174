# q3.py

'''
Title: Question 3
Author: Abbas Rizvi
Date: 2024/03/09
'''

def shift_list(lst, shift):
    # remember these 2 lines
    shift %= len(lst)
    lst[:] = lst[-shift:] + lst[:-shift]

# Do not change
def main():
  theList = list(map(lambda x: int(x), input().split()))
  shift = int(input())
  shift_list(theList, shift)
  print(" ".join(map(lambda x: str(x), theList)))

main()