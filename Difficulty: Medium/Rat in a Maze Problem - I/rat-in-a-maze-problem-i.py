from typing import List

class Solution:
    def findPathHelper(self, i: int, j: int, a: List[List[int]], n: int, ans: List[str], move: str, visited: List[List[int]]):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return

        if i + 1 < n and not visited[i + 1][j] and a[i + 1][j] == 1:
            visited[i][j] = 1
            self.findPathHelper(i + 1, j, a, n, ans, move + 'D', visited)
            visited[i][j] = 0
        

        if i - 1 >= 0 and not visited[i - 1][j] and a[i - 1][j] == 1:
            visited[i][j] = 1
            self.findPathHelper(i - 1, j, a, n, ans, move + 'U', visited)
            visited[i][j] = 0
        

        if j + 1 < n and not visited[i][j + 1] and a[i][j + 1] == 1:
            visited[i][j] = 1
            self.findPathHelper(i, j + 1, a, n, ans, move + 'R', visited)
            visited[i][j] = 0
        

        if j - 1 >= 0 and not visited[i][j - 1] and a[i][j - 1] == 1:
            visited[i][j] = 1
            self.findPathHelper(i, j - 1, a, n, ans, move + 'L', visited)
            visited[i][j] = 0

    def findPath(self, m: List[List[int]]) -> List[str]:
        n = len(m)
        ans = []
        visited = [[0 for _ in range(n)] for _ in range(n)]

        if m[0][0] == 1:
            self.findPathHelper(0, 0, m, n, ans, "", visited)
        
        return ans

            
                    
        
        
      


#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends