row_column = input('')
row_column = row_column.split()
board = []
set_list = []

def checkEqual():
    equal = True
    for i in range(int(row_column[0])):
        row = input('')
        board.append(list(row))
        set_list.append((set(board[i])))

    for i in range(len(set_list)):
        if set_list[0] == set_list[i]:
            equal = True
        else:
            equal = False

    return equal
def checkAdj():
    adj = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            try:
                if board[i][j] == board[i+1][j] or board[i][j] == board[i][j+1]:
                    adj = False
                elif board[i][j] == board[i-1][j] and i-1>0:
                    adj = False
                elif board[i][j] == board[i][j-1] and j-1>0:
                    adj = False
            except IndexError:
                pass
    return adj

if __name__ == '__main__':
    if checkEqual() and checkAdj():
        print("Checkered")
    else:
        print('Not Checkered')






