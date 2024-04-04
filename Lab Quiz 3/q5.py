def clockwise_pos(grid, row, col):
    grid_T = list(map(list, zip(*grid))) # transpose grid to have columns as rows

    # go through all possibilties and apply moves
    if row == 0:
        if col == len(grid_T)-1:
            row += 1
        else:
            col += 1
    elif row == len(grid)-1:
        if col == 0:
            row += 1
        else:
            col += -1
    elif col == 0:
        if row == 0:
            col += 1
        else:
            row += -1
    elif col == len(grid_T)-1:
        if row == len(grid)-1:
            col += -1
        else:
            row += 1

    return (row,col) # return tuple of row, col
def main():
    grid = []
    while (s := input()) != "q":
        grid.append(s.split())
    r, c = [int(x) for x in input().split()]
    r, c = clockwise_pos(grid, r, c)
    print(r, c)

if __name__ == "__main__":
  main()