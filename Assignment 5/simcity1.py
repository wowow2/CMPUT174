# simcity1.py

'''
title: Version 1
author: Abbas Rizvi
date: 2024/03/16
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


def main():
    """
    Main program.
    """
    grid = create_grid("data_1.txt")
    print("Sim City Land Values:")
    display_grid(grid)

main()