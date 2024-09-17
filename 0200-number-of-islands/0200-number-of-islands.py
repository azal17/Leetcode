class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        vis = [[0] * n for _ in range(m)]
        islands = 0

        def dfs(row, col, vis, grid):
            vis[row][col] = 1
            delrow = [-1, 0, 1, 0]
            delcol = [0, -1, 0, 1]

            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if 0 <= nrow < m and 0 <= ncol < n and vis[nrow][ncol] == 0 and grid[nrow][ncol] == '1':
                    dfs(nrow, ncol, vis, grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    dfs(i, j, vis, grid)
                    islands += 1

        return islands