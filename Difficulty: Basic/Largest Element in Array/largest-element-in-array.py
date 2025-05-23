class Solution:
    def largest(self, arr):
      
        maxx = 0
        n = len(arr)
        for i in range(n):
            current = arr[i]
            maxx = max(current, maxx)
        return maxx
        
