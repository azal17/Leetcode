#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)

def toString(r, c):
    return str(r) + ' ' + str(c)

class Solution:
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        s = set()
        
       
        def dfs(row, col, vis, ans, grid, row0, col0):
            vis[row][col] = 1
            ans.append(toString(row - row0, col - col0))
            delrow = [-1, 0, 1, 0]
            delcol = [0, -1, 0, 1]

            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                
                if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                    dfs(nrow, ncol, vis, ans, grid, row0, col0)

        
        for i in range(n): 
            for j in range(m): 
                if vis[i][j] == 0 and grid[i][j] == 1:
                    ans = []
                    dfs(i, j, vis, ans, grid, i, j)
                    s.add(tuple(ans))

        return len(s)
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends