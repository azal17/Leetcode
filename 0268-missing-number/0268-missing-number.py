class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = (n*(n+1)) // 2
        actual = sum(nums)
        return summ - actual