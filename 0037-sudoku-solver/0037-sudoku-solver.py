class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isSafe(row: int, col: int, num, board: List[List[str]]):
            
            
            for x in range(9):
                if board[x][col] == num:
                    return False
                if board[row][x] == num:
                    return False
                if board[3*(row//3) + x//3][3*(col//3) + x%3] == num:
                    return False
            return True




        def solve(board: List[List[str]] ):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in map(str, range(1, 10)):
                            if isSafe(i,j,num,board):
                                board[i][j] = num
                                if solve(board): 
                                    return True
                                board[i][j] = "."
                        return False
            return True
        solve(board)

        