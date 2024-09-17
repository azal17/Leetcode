#T.C = O(mxn), S.C = O(mxn)
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        queue = Queue()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.put((i, j, 0))
        
        maxx = 0
        while not queue.empty():
            row, col, time = queue.get()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh -= 1
                    queue.put((new_row, new_col, time + 1))
                    maxx = time + 1
        
        return maxx if fresh == 0 else -1
