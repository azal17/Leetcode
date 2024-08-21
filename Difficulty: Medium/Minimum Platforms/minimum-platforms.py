#User function Template for python3

class Solution:    
    
    def minimumPlatform(self,n,arr,dep):
         arr.sort()
         dep.sort()
            
         platforms = 1 
         cnt = 1
         i,j = 1,0
         while i < len(arr) and j <len(dep):
             if arr[i] <= dep[j]:
                 cnt +=1
                 i +=1
             else:
                 cnt -=1
                 j+=1
             platforms = max(platforms, cnt)
         return platforms
         
                     
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends