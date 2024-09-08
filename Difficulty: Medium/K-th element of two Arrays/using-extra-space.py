#User function Template for python3
#extra-space of m, TC = O(n+m)
class Solution:
    def kthElement(self, z, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        
        arr1.extend([0] * m)
  
        i, j, k = n - 1, m - 1, n + m - 1

        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1

        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1
            
        while arr1[-1] == 0 and len(arr1) > m+n:
            nums1.pop() 
        return arr1[z-1]

        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
