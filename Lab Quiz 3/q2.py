row_column = input('')
row_column = row_column.split()
board = []
set_list = []

def checkEqual():
    equal = True
    for i in range(int(row_column[0])): # asks user for inputs based on number of rows
        row = input('')
        board.append(list(row)) # board is a 2D list of rows/columns
        set_list.append((set(board[i]))) # a list of unique terms in each line in set form
    '''
    for i in range(len(board)):
        if len(board[i]) != row_column[1]:
            return False
    '''
    # check to see to each element in set list is the same
    for i in range(len(set_list)):
        if set_list[0] == set_list[i]:
            equal = True
        else:
            equal = False

    return equal
def checkAdj():
    not_adj = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            try:
                if board[i][j] == board[i+1][j] or board[i][j] == board[i][j+1]: # checks row below and column to the right
                    not_adj = False
                elif board[i][j] == board[i-1][j] and i-1>0: # checks row above if row is not 0
                    not_adj = False
                elif board[i][j] == board[i][j-1] and j-1>0: # checks col to the left if col is not 0
                    not_adj = False
            except IndexError: # if we go off the board except index error
                pass
    return not_adj

if __name__ == '__main__':
    if checkEqual() and checkAdj():
        print("Checkered")
    else:
        print('Not Checkered')






