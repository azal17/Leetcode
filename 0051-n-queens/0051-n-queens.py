class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(row: int, col: int, board:  List[List[str]]):
            for i in range(col):
                if board[row][i] =='Q':
                    return False

            i,j = row, col
            while i>= 0 and j>= 0:
                if board[i][j] =='Q':
                    return False
                i -= 1
                j -= 1
            
            i,j = row, col
            while i < n and j>= 0:
                if board[i][j] =='Q':
                    return False
                i += 1
                j -= 1

            return True
            
                


        def boardCreation(n: int):
            return [['.'] * n for _ in range(n)]
        def helper(col: int, board: List[List[str]]):
            if col == n:
                solution = [''.join(board[i]) for i in range(n)] # all solutions
                result.append(solution)

            for row in range(n):
                if isSafe(row,col,board):
                    board[row][col] = 'Q'
                    helper(col+1, board)
                    board[row][col] = '.'



        result = []
        board = boardCreation(n)
        helper(0, board)
        return result
        