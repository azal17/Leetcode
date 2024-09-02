class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(row: int, col: int, board: List[List[str]]) -> bool:
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def boardCreation(n: int) -> List[List[str]]:
            return [['.'] * n for _ in range(n)]

        def helper(row: int, board: List[List[str]]):
            if row == n:
                solution = [''.join(board[i]) for i in range(n)]
                result.append(solution)
                return

            for col in range(n):
                if isSafe(row, col, board):
                    board[row][col] = 'Q'
                    helper(row + 1, board)  
                    board[row][col] = '.'  

        result = []
        board = boardCreation(n)

        helper(0, board)
        
        return result
