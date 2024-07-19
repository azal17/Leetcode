class Solution:
    def countUniquePaths(self, row: int, col: int, numRows: int, numCols: int, memo: List[List[int]]) -> int:
        if row == (numRows - 1) and col == (numCols - 1):
            return 1
        if row >= numRows or col >= numCols:
            return 0
        if memo[row][col] != -1:
            return memo[row][col]
        else:
            memo[row][col] = self.countUniquePaths(row + 1, col, numRows, numCols, memo) + self.countUniquePaths(row, col + 1, numRows, numCols, memo)
            return memo[row][col]

    def uniquePaths(self, numRows: int, numCols: int) -> int:
        memo = [[-1 for _ in range(numCols)] for _ in range(numRows)]
        return self.countUniquePaths(0, 0, numRows, numCols, memo)