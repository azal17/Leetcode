from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isSafe(board: List[List[str]], row: int, col: int, num: str) -> bool:
 
            for x in range(9):
                if board[row][x] == num:
                    return False


            for x in range(9):
                if board[x][col] == num:
                    return False


            startRow = row - row % 3
            startCol = col - col % 3
            for i in range(3):
                for j in range(3):
                    if board[i + startRow][j + startCol] == num:
                        return False

            return True

        def solve(board: List[List[str]]) -> bool:
            
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in map(str, range(1, 10)):
                            if isSafe(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = '.'

                        return False

            return True

        solve(board)
