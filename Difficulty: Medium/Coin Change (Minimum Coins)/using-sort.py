#User function Template for python3
class Solution:
    def minCoins(self, coins, M, sum):
        ans = []
        coins.sort()
        for i in range(M-1,-1,-1):
            while sum >= coins[i]:
                sum -= coins[i]
                ans.append(coins[i])
        return len(ans)
        if sum== 0:
            return len(ans)
        else:
            return -1
