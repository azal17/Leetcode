#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
	    result = []
	    def sub(k: int, sum: int):
	        if k == n:
	            result.append(sum)
	            return
	        sub(k+1,sum+arr[k])
	        sub(k+1,sum)
	    sub(0,0)
	    result.sort()
	    return result
	            
	            
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x, end=" ")
        print("")

# } Driver Code Ends