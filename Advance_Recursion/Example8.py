# Example 8: N-Queen Problem // LeetCode 51
#Better Solution 
def NQueenProblem(n):
    board = ["." * n for i in range(n)]
    Result = []

    def solve(col, board):
        if col == n:
            Result.append(list(board))
            return
        for row in range(n):
            if isSale(row, col, board, n):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                solve(col + 1, board)
                board[row] = board[row][:col] + "." + board[row][col+1:]
        return Result

    return solve(0, board)


def isSale(row, col, board, n):
    dulRow = row
    dulCol = col

    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    row, col = dulRow, dulCol
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1

    row, col = dulRow, dulCol
    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1

    return True


print(NQueenProblem(4))


#Optimal Solution

def SolveNQueens(n):
    Result=[]
    board=["."*n for _ in range(n)]
    leftRow=[0]*n
    upperDiagonal=[0]*(2*n-1)
    lowerDiagonal=[0]*(2*n-1)

    def solve(col,board,leftRow,upperDiagonal,lowerDiagonal,n):
        if col==n:
            Result.append(board[:])
            return
        for row in range(n):
            if (leftRow[row]==0 and upperDiagonal[n-1+col-row]==0 and lowerDiagonal[col+row]==0):

                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                
                leftRow[row]=1
                lowerDiagonal[col+row]=1
                upperDiagonal[n-1+col-row]=1
                
                solve(col+1,board,leftRow,upperDiagonal,lowerDiagonal,n)
                
                board[row]=board[row][:col]+"."+board[row][col+1:]
                
                leftRow[row]=0
                lowerDiagonal[col+row]=0
                upperDiagonal[n-1+col-row]=0
        return Result
    return solve(0,board,leftRow,upperDiagonal,lowerDiagonal,n)   

print(SolveNQueens(4))             
