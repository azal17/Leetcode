#User function Template for python3

class Solution:
    
    def maximumMeetings(self,n,start,end):
        m = list(zip(start,end)) 
        m.sort(key = lambda x: x[1])
        
        count = 0
        last_end = 0
        
        for startt, endd in m:
         # add the start,end list from m
            if startt > last_end:
                count +=1
                last_end = endd
        return count
         


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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends