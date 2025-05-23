class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        mpp = {i: 0 for i in range(n + 1)}  

        for i in nums:
            mpp[i] = 1

        for i in range(n + 1):
            if mpp[i] == 0:
                return i
