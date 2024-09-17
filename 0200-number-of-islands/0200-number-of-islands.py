
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def markingislands(row, col):
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    grid[x][y] = '0'  
                    stack.append((x + 1, y))
                    stack.append((x - 1, y))
                    stack.append((x, y - 1))
                    stack.append((x, y + 1))

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  
                    islands += 1
                    markingislands(i, j)

        return islands
