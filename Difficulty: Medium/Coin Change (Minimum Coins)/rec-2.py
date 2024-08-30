#User function Template for python3
import sys
class Solution:
    def minCoins(self, coins, M, total_sum):
 
        if total_sum == 0:
            return 0
        
        ans = sys.maxsize

        for i in range(M):
           
            if coins[i] <= total_sum:
                
                temp = self.minCoins(coins, M, total_sum - coins[i])
                if temp != sys.maxsize and temp + 1 < ans:
                    ans = temp + 1
        return ans


        # code here

