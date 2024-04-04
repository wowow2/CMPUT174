def grid_fall(grid):
    grid[:] = list(map(list, zip(*grid))) # transpose 2D list
    for i in range(len(grid)):
        grid[i] = sorted(grid[i]) # order O and X
    grid[:] = list(map(list, zip(*grid))) # transpose again
def main():
    grid = []
    while (s := input()) != "q":
      grid.append([c for c in s])
    print("Grid originally:")
    [ print(''.join(x)) for x in grid ]
    grid_fall(grid)
    print("Grid after grid_fall:")
    [ print(''.join(x)) for x in grid ]

if __name__ == "__main__":
  main()