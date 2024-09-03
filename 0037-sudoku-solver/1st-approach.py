# Nested loop for grid search
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isSafe(row: int, col: int, num, board: List[List[str]]):
            for x in range(9):
                if board[x][col] == num:
                    return False
            for x in range(9):
                if board[row][x] == num:
                    return False

            start_row = row - row%3
            start_col= col - col%3
            for i in range(3):
                for j in range(3):
                    if board[ i + start_row ][j + start_col] == num:
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

        
