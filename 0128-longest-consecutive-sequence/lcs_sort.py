#Memory optimization
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        lastSmaller = float('-inf')
        count = 0
        longest_sequence = 1

        for i in range(n):
            if nums[i] - 1 == lastSmaller:
                count += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                count = 1
                lastSmaller = nums[i]
            longest_sequence = max(longest_sequence, count)
        
        return longest_sequence
