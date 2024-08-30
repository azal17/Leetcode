#User function Template for python3

class Solution:
    def minCoins(self, coins, M, total_sum):
        coins.sort(reverse=True)
        ans = []

        def helper(i: int, current_sum: int, count: int):

            if current_sum == 0:
                ans.append(count)
                return

            if i == M:
                return

            if coins[i] <= current_sum:

                helper(i, current_sum - coins[i], count + 1)

            helper(i + 1, current_sum, count)
        helper(0, total_sum, 0)

        if ans:
            return min(ans)
        else:
            return -1

                
                
                
                
        
        
    
