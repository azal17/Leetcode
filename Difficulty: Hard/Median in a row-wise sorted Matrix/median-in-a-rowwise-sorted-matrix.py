#User function Template for python3
# nested binary search
class Solution:
    def upp(self, arr, x, n):
        low, high, ans = 0, n - 1, n
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= x:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        
        return ans

    def coun(self, matrix, m, n, x):
        cnt = 0
        for i in range(m):
            cnt += self.upp(matrix[i], x, n)
        return cnt
    
    def median(self, matrix, R, C):
        left = float('inf')
        right = float('-inf')
        
        for i in range(R):
            left = min(left, matrix[i][0])
            right = max(right, matrix[i][C - 1])
        
        req = (R * C) // 2
        while left <= right:
            mid = (left + right) // 2
            smallEqual = self.coun(matrix, R, C, mid)
            
            if smallEqual <= req:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

        
        
                
    	#code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends