class Solution:

    def __init__(self):
        self.time = 0
        self.vis = None
        self.low = None
        self.d = [0, 1, 0, -1, 0]
        self.arti = False

    def minDays(self, grid):
        n = len(grid)
        m = len(grid[0])
        self.arti = False
        self.vis = [[0] * m for _ in range(n)]
        self.low = [[0] * m for _ in range(n)]
        self.time = 1
        hasArt = False
        found = False

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if found:
                        return 0
                    found = True
                    self.art(i, j, grid, -100, -100)

        if self.time == 1:
            return 0

        if self.time == 2:
            return 1

        if self.arti:
            return 1
        else:
            return 2

    def art(self, row, col, grid, parRow, parCol):
        grid[row][col] = 0
        self.vis[row][col] = self.time
        self.low[row][col] = self.time
        self.time += 1
        child = 0

        for i in range(4):
            x = self.d[i] + row
            y = self.d[i + 1] + col

            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x == parRow and y == parCol) or (self.vis[x][y] == 0 and grid[x][y] == 0):
                continue

            if self.vis[x][y] == 0:
                child += 1
                self.art(x, y, grid, row, col)
                self.low[row][col] = min(self.low[row][col], self.low[x][y])
                if self.low[x][y] >= self.vis[row][col] and (parRow != -100 and parCol != -100):
                    self.arti = True
            else:
                self.low[row][col] = min(self.low[row][col], self.vis[x][y])

        if parRow == -100 and parCol == -100 and child > 1:
            self.arti = True

        