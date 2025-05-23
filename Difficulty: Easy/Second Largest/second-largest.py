class Solution:
    def getSecondLargest(self, arr):
        length = len(arr)
        if length < 2:
            return None
        
        max1 = float("-inf")
        max2 = float("-inf")
        
        for i in range(length):
            if arr[i] > max1:
                max2 = max1
                max1 = arr[i]
            elif arr[i] > max2 and arr[i] < max1:
                max2 = arr[i]
        
        return max2 if max2 != float("-inf") else -1
