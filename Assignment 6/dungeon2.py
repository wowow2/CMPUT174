#dungeon2.py

'''
title: dungeon 2
author: Abbas Rizvi
date: 2024/03/26
'''

MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    f = open(map_file, 'r')
    lines = f.readlines()
    grid = []

    for i in range(len(lines)):
        grid.append(list(lines[i].rstrip()))

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
    return pos

def get_command() -> str:
    """
    Gets a command from the user.
    """
    command = input("")

    return command

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    for i in range(len(grid)):
        line = ''
        for j in range(len(grid[i])):
            if grid[player_position[0]][player_position[1]] == grid[i][j]:
                line+= "@"
            else:
             line += grid[i][j]
        print(line)


def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    dim = []
    dim.append(len(grid))
    dim.append((len(grid[0])))

    return dim


def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)

    grid_row_index = grid_rows-1
    grid_col_index = grid_cols-1

    if grid_row_index < position[0] or grid_col_index < position[1] or position[0] < 0 or position[1]<0:
        return False
    else:
        return True

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')

    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')

    if is_inside_grid(grid, [row, col-1]) and grid[row][col-1] in allowed_objects:
        directions.append('west')

    if is_inside_grid(grid, [row, col+1]) and grid[row][col+1] in allowed_objects:
        directions.append('east')

    return directions

def directions_output(directions):
    directions_str = ''
    for i in range(len(directions)):
        directions_str += f'You can go {directions[i]}'
    print(directions_str)

def main():
    """
    Main entry point for the game.
    """
    flag = True
    while flag:
        grid = load_map(MAP_FILE)
        pos = find_start(grid)
        dir = look_around(grid, pos)
        directions_output(dir)
        escape = get_command()
        if escape == 'escape':
            exit()
        elif escape == 'show map':
            display_map(grid, pos)
        else:
            print("I dont understand")
            main()


if __name__ == '__main__':
    main()

