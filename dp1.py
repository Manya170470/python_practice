def isSafe(row, col, board, n):
    #upper diagonal check
    #have to safe r and c in temp variables so that it doesnot chnage for upcoming while loop
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == "Q":
            return False
        r -= 1
        c -= 1

    #left check
    #have to reset r and c again so that the value is what we have passed in the function, not the one which is from previous while loop
    r, c = row, col
    while c >= 0:
        if board[r][c] == "Q":
            return False
        c -= 1 

    #lower diagonal check
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == "Q":
            return False
        r += 1
        c -= 1
    return True 

def nQueens1(col, board, ans, n):
    if col == n:
        temp = []
        for row in board:
            temp.append("".join(row))
        ans.append(temp)
        return
    for row in range(n):
        if isSafe(row, col, board, n):
            board[row][col] = "Q"
            nQueens1(col+1, board, ans, n)
            board[row][col] = "."

def SolvenQueens1(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    ans = []
    nQueens1(0, board, ans, n)
    return ans 

n = 4
result = SolvenQueens1(n)
for solution in result:
    for row in solution:
        print(row)
    print()

