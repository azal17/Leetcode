#Kadane's algorithm , no need to calculate the subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = -sys.maxsize - 1
        curr_sum = 0

        for i in range(n):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0

        
        return max_sum


