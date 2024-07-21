class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n =len(nums)
        result = [-1, -1]
        hash = {}

        for i in range(n):
            num = nums[i]
            m = target -num

            if m in hash:
                result[0] = hash[m]
                result[1] = i
                return result
            hash[num] = i
        return result
