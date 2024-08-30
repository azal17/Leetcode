#User function Template for python3
import sys

class Solution:
    def minCoinsUtil(self, coins, m, sum, dp):
        if sum == 0:
            return 0
        if dp[sum] != -1:
            return dp[sum]

        res = sys.maxsize
        for i in range(m):
            if coins[i] <= sum:
                sub_res = self.minCoinsUtil(coins, m, sum - coins[i], dp)
                if sub_res != sys.maxsize and sub_res + 1 < res:
                    res = sub_res + 1

        dp[sum] = res
        return res

    def minCoins(self, coins, M, sum):
        dp = [-1] * (sum + 1)
        result = self.minCoinsUtil(coins, M, sum, dp)
        return result if result != sys.maxsize else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        v, m = input().split()
        v, m = int(v), int(m)
        coins = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minCoins(coins, m, v)
        print(ans)

# } Driver Code Ends