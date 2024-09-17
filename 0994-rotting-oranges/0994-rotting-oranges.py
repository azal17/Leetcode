from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = Queue()
        
        fresh = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.put((i, j))
        
        count = 0
        while not q.empty():
            size = q.qsize()
            for _ in range(size):
                row, col = q.get()
                for r, c in directions:
                    rn, rc = row + r, col + c
                    if 0 <= rn < m and 0 <= rc < n and grid[rn][rc] == 1:
                        grid[rn][rc] = 2
                        fresh -= 1
                        q.put((rn, rc))
            count += 1
        if fresh == 0 and count != 0:
            return count -1
        elif fresh == 0 and count == 0:
            return 0
        elif fresh != 0:
            return -1
