def isSafe(row, col, board, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for j in range(9):
        if board[i][col] == num:
            return False
    startrow = 3 * (row // 3)
    startcol = 3 * (col // 3)
    for x in range(startrow, startrow + 3):
        for y in range(startcol, startcol + 3):
            if board[x][y] == num:
                return False
    return True

#optimised approach
def isSafe2(row, col, board, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for j in range(9):
        if board[j][col] == num:
            return False
    for i in range(9):
        row = 3 * (row // 3) + i // 3
        col = 3 * (col // 3) + i % 3
        if board[row][col] == num:
            return False
    return True



def SudokuSolver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if isSafe2(row, col, board,num):
                        board[row][col] = num
                        if SudokuSolver(board):
                            return True
                        board[row][col] = 0
                return False
    return True
def printBoard(board):
    for row in board:
        print(*row)

board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

if SudokuSolver(board):
    printBoard(board)
else:
    print("No solution exist.")
