class Solution(object):
    def sub(self, nums,i,n,prev = 0):
        if i == n:
            return 0
        a = self.sub(nums,i+1,n,prev)
        b=0
        if nums[i]> prev:
            b =  1 + self.sub(nums,i+1,n,nums[i])
        return max(a,b)

    def lengthOfLIS(self, nums):
        n = len(nums)
        return self.sub(nums, 0, n, float('-inf'))
