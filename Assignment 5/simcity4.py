# simcity4.py

'''
title: Version 4
author: Abbas Rizvi
date: 2024/03/17
Description: Fills in, displays, and analyizes data
'''
from copy import deepcopy
from math import ceil
def create_grid(filename):
    """
    Create a grid of land values from a file
    :param filename: str
    :return: list
    """
    # empty list and string
    grid_list = []
    grid_str = ''

    file = open(filename, 'r')
    f = file.readlines()
    rows = int(f[0].rstrip()) #get values for number of rows, we dont need column value

    f = f[2:] # omits row/column values from file content
    for i in range(len(f)):
        if (i+1) % rows != 0: #this keeps adding to a row until we hit the max, using the fact that the grid is square
            grid_str += f[i] + ' '
        else: # resets the row after max capacity and makes a new row
            grid_str += f[i] + " "
            grid_list.append(grid_str.split())
            grid_str = ''

    return grid_list

def display_grid(grid):
    """
    Display a grid of land values
    :param grid: list
    :return: None
    """
    for i in range(len(grid)): # goes through rows
        output_str = ''
        for j in range(len(grid[i])): #goes through columns
            output_str += f'{grid[i][j]:>9}' # adds entries with a space between them

        print(f"""{output_str}""")

def find_neighbor_values(grid, row, col):
    """

    :param grid: list
    :param row: int
    :param col: int
    :return: list
    """
    neighbors = []

    # finding neighbours from any postion, so we either move one to the left, one to the right or don't move.
    coords = [-1,2]
    for i in range(coords[0], coords[1]):
        for j in range(coords[0],coords[1]):
            if row+i != row or col+j != col: # if moving from row or column
                try:
                    if row +i < 0 or col +j < 0: # tests if moved off grid
                        continue
                    else:
                        neighbors.append(grid[row + i][col + j])
                except IndexError:
                    pass # index error serves as boundary check
    neighbors.sort() # orders list of neighbours
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
    :param grid: list
    :return: list
    """
    grid_copy = deepcopy(grid) # not mutating original
    for i in range(len(grid_copy)):
        for j in range(len(grid_copy[i])):
            if grid_copy[i][j] == '0': # 0 represents blank spaces
                avg_list = find_neighbor_values(grid_copy,i,j)
                for k in range(len(avg_list)):
                    avg_list[k] = int(avg_list[k]) # converts neighbours to int
                average = sum(avg_list)/len(avg_list)
                grid_copy[i][j] = int(average) # mutates the new list not the original

    return grid_copy

def find_max(grid):
    """
    Find the max value in the grid (rounded to the nearest integer)
    :param grid: list
    :return: int
    """
    total_list = [] # makes a list of all entries
    for i in range(len(grid)):
        for j in range(len(grid)):
            total_list.append(int(grid[i][j]))
    maximum = ceil(max(total_list)) # max value
    return maximum

def find_average(grid):
    """
    Find the average value in the grid (rounded to the nearest integer)
    :param grid: list
    :return: int
    """
    total_list = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total_list.append(int(grid[i][j])) # same procedure as previous function
            print(total_list)
    avg = ceil((sum(total_list)/len(total_list))) # rounds up
    return avg

def main():
    """
    Main program.
    """
    grid = create_grid("data_2.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")

if __name__ == "__main__":
    main()
