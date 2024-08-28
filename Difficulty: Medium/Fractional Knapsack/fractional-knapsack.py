#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        arr.sort(key = lambda x: x.value/x.weight, reverse = True)
        ans  = 0
        
        for i in arr:
            if i.weight <= w:
                ans += i.value
                w -= i.weight
            else:
                ans += (i.value*w)/i.weight
                w = 0
        return ans
                
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


class Item:

    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, w = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        arr = [Item(0, 0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2 * i]
            arr[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(w, arr, n))

# } Driver Code Ends