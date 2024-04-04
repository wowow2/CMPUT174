'''
The function clockwise_pos has three parameters grid which is a list of lists 
of characters, r which is an integer that represents a row index of grid, and c 
which is an integer that represents a column index of grid. You are guaranteed 
that the position indicated by (row, col) given to your function is a position 
on the outside border of your grid (that is, it must lay on one of the top row, 
the rightmost column, the bottom row, or the leftmost column). Your function 
should return a tuple with two integers which what the row and column of 
position found by rotating around the outside of your grid one spot from the 
given c and c position.

Rotating clockwise means if the position is at the top of you grid you should 
move right, if the position is at the right edge of your grid you should move 
down, if the position is at the bottom edge of your grid you should be move 
left, and if the position is at the left edge of your grid you should move up. 
The corners are on two edges, at the top right corner you should move down, at 
the bottom right corner you should move left, at the bottom left corner you 
should move up, and at the top left corner you should move right.

The provided code reads in the grid until it sees the character q and then 
reads in the row and column number to call your function with.
'''

def clockwise_pos(grid, row, col):
  # TODO: Fill in this function! All of your
  # code must go in this function, any code
  # you write outside of this function will
  # NOT be tested!
  num_rows = len(grid)
  num_cols = len(grid[0])
  
  if row == 0:
    if col < num_cols - 1:
      return (row, col + 1)
    else:
      return (row + 1, col)
  elif col == num_cols - 1:
    if row < num_rows - 1:
      return (row + 1, col)
    else:
      return (row, col - 1)
  elif row == num_rows - 1:
    if col > 0:
      return (row, col - 1)
    else:
      return (row - 1, col)
  elif col == 0:
    if row > 0:
      return (row - 1, col)
    else:
      return (row, col + 1)

def main():
  grid = []
  while (s := input()) != "q":
    grid.append(s.split())
  r, c = [int(x) for x in input().split()]
  r, c = clockwise_pos(grid, r, c)
  print(r, c)

if __name__ == "__main__":
  main()