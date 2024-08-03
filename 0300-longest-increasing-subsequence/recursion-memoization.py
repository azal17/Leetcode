# Memoization = stores the results to avoid redundancy
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        d = {}

        def sub(i,prev):
            if i == n:
                return 0
            
            if (i,prev) in d:
                return d[(i,prev)]
            
            a = sub(i+1,prev)

            b = 0
            if nums[i]> prev:
                b =1+ sub(i+1, nums[i])
        
            ans = max(a,b)
            d[(i, prev)] = ans
            return ans
            
        return sub(0,float('-inf'))
