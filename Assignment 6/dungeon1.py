#dungeon1.py

'''
title: dungeon 1
author: Abbas Rizvi
date: 2024/03/26
'''

MAP_FILE = 'arcadia_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    f = open(map_file, 'r')
    lines = f.readlines()
    grid = []

    for i in range(len(lines)):
        grid.append(list(lines[i].rstrip()))
    print(grid)
    return grid

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    pos = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                pos.append(i)
                pos.append(j)
    print(f'Starting Position: {pos}')
    return pos

def get_command() -> str:
    """
    Gets a command from the user.
    """
    escape = input("")
    flag = True
    while flag:
        if escape == 'escape':
            flag = False
        else:
            print("I do not understand")
            escape = input("")
    return escape

def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE)
    find_start(grid)
    escape = get_command()
    if escape == 'escape':
        exit()

if __name__ == '__main__':
    main()

