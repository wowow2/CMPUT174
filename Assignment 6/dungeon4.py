#dungeon4.py

'''
title: dungeon 4
author: Abbas Rizvi
date: 2024/03/26
'''
import copy
MAP_FILE = 'arcadia_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    :param map_file: str
    :return: list[list[str]]
    """
    f = open(map_file, 'r')
    lines = f.readlines()
    grid = []
    f.close()

    # creates 2D list representing the grid
    for i in range(len(lines)):
        grid.append(list(lines[i].rstrip()))

    return grid

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    :param grid: list[list[str]]
    :return: list[int, int]
    """
    pos = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                # finds coordinates for the starting point puts them in a list
                pos.append(i)
                pos.append(j)
    return pos

def get_command() -> str:
    """
    Gets a command from the user.
    :return: str
    """
    command = input("")

    return command

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    :param grid: list[list[str]]
    :param player_position: list[int, int]
    :return: list[int, int]
    """
    display_grid = copy.deepcopy(grid)
    row = player_position[0]
    col = player_position[1]
    display_grid[row][col] = "@" # replaces player position with @ in the copy grid

    # defines what emojis are in the context of the map
    emojis_dict = {
        "-": "🧱",
        "S": "🏠",
        "F": "🏺",
        "*": "🟢",
        "@": '🧝'
    }

    for i in range(len(display_grid)):
        line = ''
        for j in range(len(display_grid[i])):
            display_grid[i][j] = emojis_dict.get(display_grid[i][j]) # converts each entry to emoji counterpart
            line += display_grid[i][j]
        print(line)


def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    :param grid: list[list[str]]
    :return: list[int, int]
    """
    dim = []
    # number of rows and columns
    dim.append(len(grid))
    dim.append((len(grid[0])))

    return dim


def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    :param grid: list[list[str]]
    :param player_position: list[int, int]
    :return: bool
    """
    grid_rows, grid_cols = get_grid_size(grid) # dim of the grid

    grid_row_index = grid_rows-1
    grid_col_index = grid_cols-1

    # if player tries to move off grid return false, else return true
    if grid_row_index < position[0] or grid_col_index < position[1] or position[0] < 0 or position[1]<0:
        return False
    else:
        return True

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    :param grid: list[list[str]]
    :param player_position: list[int, int]
    :return: list
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    # checks all possible movements by checking if positions are in the grid and it is a moveable spot
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
    """
    prints a string with possible moves
    :param directions: list
    :return:
    """
    directions_str = 'You can go '
    for i in range(len(directions)):
        directions_str += f'{directions[i]}, '
    print(directions_str.rstrip().rstrip(','))

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    :param direction: str
    :param player_position: list[int, int]
    :param grid: list[list[str]]
    :return: bool
    """
    flag = True
    row_start = player_position[0]
    col_start = player_position[1]

    if direction == 'north':
        moves = look_around(grid, player_position) #checks to see if move is allowed
        for i in range(len(moves)):
            if moves[i] == 'north':
                player_position[0] = player_position[0]-1 # changes player position after every move
    elif direction == 'south':
        moves = look_around(grid, player_position)
        for i in range(len(moves)):
            if moves[i] == 'south':
                player_position[0] = player_position[0] + 1
    elif direction == 'west':
        moves = look_around(grid, player_position)
        for i in range(len(moves)):
            if moves[i] == 'west':
                player_position[1] = player_position[1] -1
    elif direction == 'east':
        moves = look_around(grid, player_position)
        for i in range(len(moves)):
            if moves[i] == 'east':
                player_position[1] = player_position[1] +1

    # if player position hasnt changed there was no valid move
    if row_start == player_position[0] and col_start == player_position[1]:
        flag = False
    return flag

def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    :param player_position: list[int, int]
    :param grid: list[list[str]]
    :return: bool
    """
    f_pos = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "F": # finds position of F
                f_pos.append(i)
                f_pos.append(j)
    if f_pos[0] == player_position[0] and f_pos[1] == player_position[1]: #checks to see if player position is equal to F
        return True
    else:
        return False

def display_help() -> None:
    """
    Displays a list of commands.
    """
    f = open(HELP_FILE, 'r')
    content = f.read()
    f.close()

    print(content)


def main():
    """
    Main entry point for the game.
    """
    flag = True
    # creates grid and finds player position
    grid = load_map(MAP_FILE)
    pos = find_start(grid)
    while flag:
        # gets set of moves and prompts user for input every iteration
        dir = look_around(grid, pos)
        directions_output(dir)
        escape = get_command()
        if escape == 'escape':
            exit()
        elif escape == 'show map':
            display_map(grid, pos) #display updated grid
        elif escape == 'go north' or escape == 'go south' or escape == 'go east' or escape == 'go west':
            can_move = move(escape.lstrip('go '),pos,grid)
            print(can_move)
            if can_move:
                # is a valid move
                print(f'You moved {escape.lstrip("go ")}')
            else:
                # not a valid move
                print("There is no way there")
            if check_finish(grid, pos):
                # if finish condition is reached the game is over
                print("Congratulations! You have reached the exit!")
                exit()
        elif escape == 'help':
            display_help()
        else:
            print("I dont understand")

if __name__ == '__main__':
    main()

