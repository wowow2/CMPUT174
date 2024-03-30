# simcity2.py

'''
title: Version 2
author: Abbas Rizvi
date: 2024/03/17
'''

def create_grid(filename):
    """
    Create a grid of land values from a file
    """
    grid_list = []
    grid_str = ''
    file = open(filename, 'r')
    f = file.readlines()
    rows = int(f[0].rstrip())
    columns = int(f[1].rstrip())

    file_list = f[2:]
    for i in range(len(file_list)):
        if (i+1) % rows != 0:
            grid_str += file_list[i] + ' '
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

def find_neighbor_values(grid, row=0, col=1):
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

def main():
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City Land Values:")
    display_grid(grid)



main()