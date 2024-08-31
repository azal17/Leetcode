#T.C = O(n/2), S.C = O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        for i in range(0, len(nums) - 1, 2):  
            if nums[i] != nums[i + 1]:
                return nums[i]  
        return nums[-1]
