# simcity3.py

'''
title: Version 3
author: Abbas Rizvi
date: 2024/03/17
'''
from copy import deepcopy
def create_grid(filename):
    """
    Create a grid of land values from a file
    """
    grid_list = []
    grid_str = ''
    file = open(filename, 'r')
    f = file.readlines()
    rows = int(f[0].rstrip())

    f = f[2:]
    for i in range(len(f)):
        if (i+1) % rows != 0:
            grid_str += f[i] + ' '
        else:
            grid_str += f[i] + " "
            grid_list.append(grid_str.split())
            grid_str = ''

    return grid_list

def display_grid(grid):
    """
    Display a grid of land values
    """
    for i in range(len(grid)):
        output_str = f'{""}'
        for j in range(len(grid[i])):
            output_str += f'{grid[i][j]:>9}'

        print(f"""{output_str:}""")

def find_neighbor_values(grid, row, col):
    """
    Find the neighbors of a cell
    """
    neighbors = []
    coords = [-1,2]
    for i in range(coords[0], coords[1]):
        for j in range(coords[0],coords[1]):
            if row+i != row or col+j != col:
                try:
                    if row +i < 0 or col +j < 0:
                        pass
                    else:
                        neighbors.append(grid[row + i][col + j])
                except IndexError:
                    pass
    neighbors.sort()
    return neighbors

def fill_gaps(grid):
    """
    Fill the gaps in the grid
    Creates a new grid that is a copy of the original grid
    Call find_neighbor_values function to find the neighbors of each cell.
    Find the average of their values and round it to the nearest integer
    Use the average values to fill in the missing values in the new grid.
    Return the new grid
    Do NOT modify the original grid!
    """
    grid_copy = deepcopy(grid)
    for i in range(len(grid_copy)):
        for j in range(len(grid_copy[i])):
            if grid_copy[i][j] == '0':
                avg_list = find_neighbor_values(grid_copy,i,j)
                for k in range(len(avg_list)):
                    avg_list[k] = int(avg_list[k])
                average = sum(avg_list)/len(avg_list)
                grid_copy[i][j] = int(average)

    return grid_copy

def main():
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City land values:")
    display_grid(grid)
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)

if __name__ == "__main__":
    main()
